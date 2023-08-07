# coding: utf-8
"""This module contains application controllers."""
from __future__ import annotations

import asyncio
import json
import os
import signal
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator, Dict, List, Mapping
from uuid import uuid4

import async_timeout as at
from aioredis import ConnectionPool, Redis
from aioredis.client import PubSub
from aioredis.exceptions import RedisError as AIORedisError
from fastapi import status
from fastapi.responses import JSONResponse

from piaf.api.config import Settings
from piaf.api.exceptions import (
    DuplicatedPlatformNameError,
    InternalServerError,
    RedisConnectionNotInitialized,
    RedisError,
    RedisUnavailableError,
    UnknownPlatformError,
)
from piaf.api.impl.process import AgentPlatformProcess
from piaf.api.models import AgentPlatformModel


class RedisController:
    """
    Control a redis database.

    This controller maintains a connection pool bound to the Redis instance and can provide sessions (connections) to perform database operations.
    """

    def __init__(self, settings: Settings) -> None:
        """
        Create a new :class:`RedisController` instance.

        To bind the connections pool to the Redis database, you must call the :meth:`RedisController.connect` coroutine.

        :param settings: application settings, used to configure the connection pool
        """
        self._settings = settings
        self._pool: ConnectionPool | None = None

    async def connect(self) -> None:
        """
        Bind the connections pool to the Redis database and test it.

        :raise RedisUnavailableError: Can't reach the Redis database
        :raise RedisError: If any error occurs
        """
        options: Dict[str, Any] = {
            "decode_responses": True,
            "max_connections": self._settings.redis_max_connections,
        }
        if self._settings.redis_user and self._settings.redis_password:
            options.update(
                {
                    "username": self._settings.redis_user,
                    "password": self._settings.redis_password,
                }
            )
        if self._settings.redis_db:
            options["db"] = self._settings.redis_db

        self._pool = ConnectionPool.from_url(
            f"{self._settings.redis_scheme}://{self._settings.redis_host}", **options
        )
        async with self.session() as session:
            await session.ping()  # Ping to test the connection

    async def close(self) -> None:
        """Close the connections pool and disconnect all active connections."""
        if self._pool is not None:
            await self._pool.disconnect()

    @asynccontextmanager
    async def session(self) -> AsyncGenerator[Redis, None]:
        """
        Get a Redis session to the database.

        The session will be closed automatically after being used.

        :raise RedisConnectionNotInitialized: The connections pool is not bound, did you called :meth:`RedisController.connect` ?
        :raise RedisUnavailableError: The is an issue with the connection
        :raise RedisError: an error occurred while using the connection
        """
        if self._pool is None:
            raise RedisConnectionNotInitialized()

        try:
            session = Redis(connection_pool=self._pool)
            yield session
        except ConnectionError as e:
            raise RedisUnavailableError() from e
        except AIORedisError as e:
            raise RedisError() from e
        finally:
            if session is not None:
                await session.close()

    def __eq__(self, other: Any) -> bool:
        """
        Equality check.

        :param other: the other object
        :return: `True` if both are equal (same pool and settings), `False` otherwise.
        """
        if not isinstance(other, type(self)):
            return False
        return self._pool == other._pool and self._settings == other._settings

    def __hash__(self) -> int:
        """Get this instance's hash code."""
        return hash((self._pool, self._settings))


class PlatformController:
    """
    Controls platforms.

    This controller will allow you to manipulate platforms : creation, deletion, listing and sending tasks.
    """

    PLATFORMS_REDIS_SET = "platforms"
    PLATFORM_PREFIX_HASHSET = "platform:"

    def __init__(self, settings: Settings, session: Redis) -> None:
        """
        Create a new :class:`PlatformController`.

        :param settings: application settings to configure new platforms.
        :param session: an active Redis session
        """
        self._settings = settings
        self._session = session

    async def create_platform(self, ptf: AgentPlatformModel) -> None:
        """
        Try to spawn a new platform.

        :param ptf: the platform description supplied by the user
        :raise DuplicatedPlatformName: the supplied platform's name is already taken
        """
        if await self._session.sismember(self.PLATFORMS_REDIS_SET, ptf.name):
            raise DuplicatedPlatformNameError(ptf.name)

        # Subscribe to events coming from the future platform
        try:
            pubsub: PubSub = self._session.pubsub(ignore_subscribe_messages=True)
            await pubsub.subscribe(f"channels:{ptf.name}:events:.platform.agents.api")

            # Launch the platform
            info = self._spawn_process(ptf)

            # Wait until the platform is ready (ie the APIAgent is up)
            async for msg in pubsub.listen():
                record: Dict[str, Any] = json.loads(msg["data"])
                if record["event"]["type"] == "agent_creation":
                    break
        finally:
            await pubsub.close()

        # Store information about the platform in the redis database
        await self._session.sadd(self.PLATFORMS_REDIS_SET, ptf.name)
        await self._session.hset(self.PLATFORM_PREFIX_HASHSET + ptf.name, mapping=info)

    def _spawn_process(self, ptf: AgentPlatformModel) -> Dict[str, Any]:
        """
        Spawn a new agent platform as a process.

        :param ptf: description of the platform to create
        :return: a mapping describing the platform : the name, the type (process) and the process's pid
        """
        process = AgentPlatformProcess(ptf.name, self._settings)
        process.start()

        return {"type": "process", "name": ptf.name, "pid": process.pid}

    def _spawn_docker(self, ptf: AgentPlatformModel) -> Dict[str, Any]:
        """
        Spawn a new agent platform as a docker container.

        :param ptf: description of the platform to create
        :return: a mapping describing the platform : the name, the type (docker) and the container's hash
        """
        raise NotImplementedError()

    async def stop(self, name: str) -> None:
        """
        Stop and delete the platform identified by the provided description.

        :param name: the platform's name
        :raise UnknownPlatformError: there is no platform matching the provided description
        """
        if not (await self._session.sismember(self.PLATFORMS_REDIS_SET, name)):
            raise UnknownPlatformError(name)

        try:
            # Subscribe to platform events
            pubsub: PubSub = self._session.pubsub(ignore_subscribe_messages=True)
            await pubsub.subscribe(f"channels:{name}:events:.platform")

            # Publish the task to stop the platform
            await self._session.publish(
                f"channels:{name}:from-api",
                json.dumps({"task_type": "StopPlatformTask", "id": str(uuid4())}),
            )

            # Wait until a 'platform-death' event is received
            async for msg in pubsub.listen():
                record: Dict[str, Any] = json.loads(msg["data"])
                if (
                    record["event"]["type"] == "state_change"
                    and record["event"]["data"]["to"] == "STOPPED"
                ):
                    break
        except Exception as e:
            raise InternalServerError() from e
        finally:
            await pubsub.close()

        # Delete record from database
        record = await self._session.hgetall(self.PLATFORM_PREFIX_HASHSET + name)
        await self._session.delete(self.PLATFORM_PREFIX_HASHSET + name)
        await self._session.srem(self.PLATFORMS_REDIS_SET, name)

    async def kill(self, name: str) -> None:
        """
        Kill the provided platform without letting it finishing properly.

        :param name: name of the platform
        :raise UnknownPlatformError: there is no platform matching the provided description
        """
        if not (await self._session.sismember(self.PLATFORMS_REDIS_SET, name)):
            raise UnknownPlatformError(name)

        # Get the platform's description
        record: Dict[str, Any] = await self._session.hgetall(
            self.PLATFORM_PREFIX_HASHSET + name
        )
        if record["type"] == "process":
            await self._kill_process(record)
        else:
            await self._kill_docker(record)

        # Delete record from database
        await self._session.delete(self.PLATFORM_PREFIX_HASHSET + name)
        await self._session.srem(self.PLATFORMS_REDIS_SET, name)

    async def _kill_process(self, description: Dict[str, Any]) -> None:
        """
        Kill a platform running in a dedicated process.

        :param description: description of the platform to kill. It should contain a 'type' entry set to 'process' and a 'pid' entry set to the process's pid.
        """
        os.kill(int(description["pid"]), signal.SIGTERM)

    async def _kill_docker(self, description: Dict[str, Any]) -> None:
        """
        Kill a platform running in a docker container.

        :param description: description of the platform to kill. It should contain a 'type' entry set
        to 'docker' and a 'hash' entry set to the container's hash.
        """
        raise NotImplementedError()

    async def get_all_platforms(self) -> List[Mapping[str, str]]:
        """
        Interrogate the Redis database to get all the running platforms.

        :return: a list of platform names
        """
        records = await self._session.smembers(self.PLATFORMS_REDIS_SET)
        return [{"name": ptf} for ptf in records]

    async def process_task(
        self,
        ptf_name: str,
        task: Dict[str, Any],
        timeout: float = 5,
    ) -> JSONResponse:
        """
        Send the given task to the APIAgent in the specified platform.

        If the platform doesn't exists, then returns an HTTP 404 response. Otherwise the task is submitted to the platform and the result is returned.

        :param ptf_name: name of the platform
        :param task: a JSON-compatible dict describing the task to submit
        :param platform_ctrl: the platform controller
        :param timeout: time (in seconds) given to the task for its execution
        :return: a :class:`JSONRequest` with the result or the error.
        """
        # Ensure platform exists
        platforms = await self.get_all_platforms()
        if ptf_name not in (ptf["name"] for ptf in platforms):
            return JSONResponse(
                content={"details": f"Unknown platform '{ptf_name}'"},
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        # Subscribe
        pubsub = self._session.pubsub(ignore_subscribe_messages=True)
        await pubsub.subscribe(f"channels:{ptf_name}:to-api")

        # Wait for reply
        try:
            async with at.timeout(timeout):

                # Send task here (retry until delivered to the API agent or timeout)
                while (
                    await self._session.publish(
                        f"channels:{ptf_name}:from-api", json.dumps(task)
                    )
                    == 0
                ):
                    await asyncio.sleep(0.1)

                # Await response
                async for msg in pubsub.listen():
                    reply = json.loads(msg["data"])
                    if reply["id"] == task["id"]:
                        break
        except Exception as e:
            raise InternalServerError() from e
        finally:
            await pubsub.close()

        # Return result as a valid response
        if reply["error"] is not None:
            raise InternalServerError() from reply["error"]
        return JSONResponse(reply["data"])
