# coding: utf-8
"""This module contains a set of helper objects."""
from __future__ import annotations

import asyncio
import importlib
import json
from contextlib import asynccontextmanager
from enum import Enum
from multiprocessing import Process
from typing import TYPE_CHECKING, Any, AsyncGenerator, Dict, List, Tuple, Union, cast

import aioredis
from aioredis import ConnectionPool, Redis

from piaf.agent import Agent
from piaf.api.config import Settings
from piaf.api.exceptions import RedisConnectionNotInitialized, RedisError
from piaf.behavior import Behavior
from piaf.comm import AID, ACLMessage
from piaf.audit import Event, EventRecord, Subscriber, Topic
from piaf.launcher import PlatformLauncher, ServiceDescription
from piaf.ptf import AgentPlatform, AgentPlatformFacade, Extension
from piaf.service import AMSAgentDescription

if TYPE_CHECKING:
    from aioredis.client import PubSub


class APIAgent(Agent):
    """
    A special agent that can communicate with the web API through a Redis connection.

    The agent will first try to connect to the redis database and then will listen to incoming tasks. Tasks execution results are sent back to the web API.
    """

    def __init__(self, aid: AID, platform: AgentPlatformFacade):
        """
        Initialize a new :class:`APIAgent` instance.

        :param aid: the agent's :class:`AID`
        :param platform: a reference to the underlying platform
        """
        super().__init__(aid, platform)
        self.add_behavior(ExecuteTasksBehavior(self))


class ExecuteTasksBehavior(Behavior):
    """
    Pull tasks from the redis channel and execute each one sequentially.

    This behavior requires an open connection to the redis database and a channel listening on the input tasks queue.
    """

    def __init__(self, agent: APIAgent):
        """
        Initialize a new :class:`ExecuteTasksBehavior` instance.

        :param agent: the owner
        """
        super().__init__(agent)

    async def action(self) -> None:
        """
        Wait for incoming tasks and execute each one sequentially.

        Incoming tasks should have the following structure::

            {
                "task_type": "[module.]class",
                "id": "id_of_the_task",
                ...
            }

        Tasks' class are dynamically imported from the specified module or :mod:`piaf.api.tasks` if no module is specified. Results are sent back in json into the response queue. The structure of a response is the following::

            {
                "id": "id-of-the-request",
                "data": whatever is returned by the task's execution or null,
                "error": error message if the execution failed, null otherwise
            }


        """
        async with self.db_session_and_channel() as (client, channel):
            await channel.subscribe(f"channels:{self.agent.aid.hap_name}:from-api")
            async for task in channel.listen():
                json_task: Dict[str, Any] = json.loads(task["data"])
                data = json_task["task_type"]
                split_data = data.rsplit(".", maxsplit=1)

                if len(split_data) == 1:
                    module_name = "piaf.api.impl.tasks"
                    klass_name = split_data[0]
                else:
                    module_name, klass_name = split_data
                module = importlib.import_module(module_name)

                try:
                    klass = getattr(module, klass_name)
                    id_ = json_task["id"]
                    result = await klass.from_json(json_task).execute(self.agent)

                    data = json.dumps(
                        {"id": id_, "data": result, "error": None},
                        default=serialize_piaf_object,
                    )

                    await client.publish(
                        f"channels:{self.agent.aid.hap_name}:to-api",
                        data,
                    )

                except Exception as e:
                    self.agent.logger.exception("Unable to run task.", exc_info=e)
                    await client.publish(
                        f"channels:{self.agent.aid.hap_name}:to-api",
                        json.dumps({"id": id_, "data": None, "error": str(e)}),
                    )

    @asynccontextmanager
    async def db_session_and_channel(
        self,
    ) -> AsyncGenerator[Tuple[Redis, PubSub], None]:
        """
        Work with a Redis client and a channel.

        If the wrapper task is cancelled, this context manager will catch any error, close both the channel and the client and then re-raise it.
        """
        client: None | Redis = None
        channel: None | PubSub = None
        try:
            connection_pool = cast(
                RedisConnectionPoolExtension, self.agent._platform.extensions["redis"]
            )
            client = connection_pool.client
            channel = client.pubsub(ignore_subscribe_messages=True)
            yield client, channel
        finally:
            if channel is not None:
                await channel.close()
            if client is not None:
                await client.close()

    def done(self) -> bool:
        """
        One shot behavior, always return `True`.

        :return: `True`
        """
        return True


class EventsToRedis(Subscriber):
    """
    Subscribe to all events and send them into the redis database.

    This subscriber requires the :class:`RedisConnectionPoolExtension` extension to be loaded in order to send events to the Redis database.
    """

    def __init__(self, platform: AgentPlatform) -> None:
        """
        Create a new :class:`EventToRedis` instance.

        :param platform: the agent platform
        """
        super().__init__()
        self.hap_name = platform.name
        self._platform = platform
        self.redis: None | Redis = None

    async def on_event(self, event_record: EventRecord) -> None:
        """
        Re-publish the event on each queue it is published.

        :param event_record: the record
        """
        if self.redis is None:
            self.redis = cast(
                RedisConnectionPoolExtension, self._platform.extensions["redis"]
            ).client

        json_record = json.dumps(event_record, default=serialize_piaf_object)
        tasks = []
        for channel in event_record.topics:
            tasks.append(
                self.redis.publish(
                    f"channels:{self.hap_name}:events:{channel}", json_record
                )
            )

        results = await asyncio.gather(
            *tasks, return_exceptions=True
        )  # fixme: ignored for now

    async def close(self):
        """
        Close this subscriber.

        It releases the associated Redis connection properly.
        """
        if self.redis is not None:
            await self.redis.close()


#: A type that represents all JSON-compatible types
JSONType = Union[str, int, float, bool, None, List[Any], Dict[str, Any]]


def serialize_piaf_object(
    o: Any,
) -> JSONType:
    """
    Given a `piaf` object, convert it into a JSON-compatible object.

    :param o: the piaf object to serialize
    :return: a JSON-compatible object
    :raise TypeError: the object can't be serialized
    """
    if isinstance(o, AID):
        return {
            "name": o.name,
            "shortname": o.short_name,
            "addresses": o.addresses,
            "resolvers": [serialize_piaf_object(r) for r in o.resolvers],
        }
    if isinstance(o, Enum):
        return o.name
    if isinstance(o, AMSAgentDescription):
        return {
            "aid": serialize_piaf_object(o.name),
            "state": serialize_piaf_object(o.state),
            "owner": o.ownership,
        }
    if isinstance(o, EventRecord):
        return {
            "event": serialize_piaf_object(o.event),
            "topics": [serialize_piaf_object(topic) for topic in o.topics],
            "timestamp": o.timestamp,
        }
    if isinstance(o, Event):
        return {
            "source": o.source,
            "type": o.type,
            "data": json.loads(json.dumps(o.data, default=serialize_piaf_object)),
        }
    if isinstance(o, Topic):
        return str(o)
    if isinstance(o, ACLMessage):
        return {
            k: json.loads(json.dumps(v, default=serialize_piaf_object))
            for k, v in o.__dict__.items()
        }
    return f"Unserializable object: {type(o)}"


class RedisConnectionPoolExtension(Extension):
    """
    An extension providing a pool of Redis connections.

    The user is responsible of closing its session (connection) once the work is finished.
    """

    def __init__(
        self, settings: Settings
    ) -> None:  # TODO: use custom settings, not app ones
        """
        Create a new :class:`RedisConnectionPoolExtension` instance.

        The pool is not bound.

        :param settings: application settings used to setup the pool.
        """
        self._settings = settings
        self._pool: ConnectionPool | None

    async def on_start(self) -> None:
        """
        Initialize the pool and test the connection.

        :raise RedisError: Unable to establish a connection to Redis.
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

        self._pool = aioredis.ConnectionPool.from_url(
            f"{self._settings.redis_scheme}://{self._settings.redis_host}", **options
        )

        try:
            client: Redis = self.client
            await client.ping()  # Ping to test the connection
            await client.close()
        except Exception as e:
            await client.close()
            if self._pool is not None:
                await self._pool.disconnect()
            raise RedisError() from e

    async def on_stop(self) -> None:
        """Disconnect all connections and close the pool."""
        if self._pool is not None:
            await self._pool.disconnect()

    @property
    def client(self) -> Redis:
        """
        Get a Redis session.

        :raise RedisConnectionNotInitialized: the pool is not bound yet.
        :return: a session
        """
        if self._pool is None:
            raise RedisConnectionNotInitialized()
        return Redis(connection_pool=self._pool)


class AgentPlatformProcess(Process):
    """A customized process that runs a :class:`piaf.ptf.AgentPlatform` on a local asynchronous loop."""

    def __init__(self, name: str, settings: Settings) -> None:
        """
        Create a new instance.

        :param name: name of the platform, which will also be the name of the thread.
        """
        super().__init__(name=name, daemon=True)
        self._settings = settings

    def run(self) -> None:
        """
        Create the asynchronous loop and launch the platform.

        The platform will start with an agent called 'api', which can receive tasks
        from a web interface to execute. For now, logs are streamed in the parent's
        console (if any).
        """
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        import logging

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("{processName} - {levelname:<8}:{message}", style="{")
        )
        logger.addHandler(handler)

        self.launcher = PlatformLauncher(self.name)
        self.launcher.add_extension(
            "redis", RedisConnectionPoolExtension(self._settings)
        )
        self.launcher.add_service(ServiceDescription("api", APIAgent))

        self.launcher.ptf.evt_manager.subscribe_to(
            EventsToRedis(self.launcher.ptf),
            Topic.from_str(""),
        )

        self.launcher.run()
