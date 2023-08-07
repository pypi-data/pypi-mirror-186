# coding: utf-8
"""
Declare all dependencies in one place.

Dependencies replacement (mainly for test) will be easier.
"""

from functools import lru_cache
from typing import AsyncGenerator

from aioredis import Redis
from fastapi import Depends

from piaf.api.config import Settings
from piaf.api.controllers import PlatformController, RedisController


@lru_cache()
def get_settings() -> Settings:
    """
    Get the application settings.

    :return: application settings
    """
    return Settings()


@lru_cache()
def get_redis_ctrl() -> RedisController:
    """
    Get the application's :class:`RedisController`.

    :return: the redis controller
    """
    ctrl = RedisController(get_settings())
    return ctrl


async def get_redis_session(
    redis_ctrl: RedisController = Depends(get_redis_ctrl),
) -> AsyncGenerator[Redis, None]:
    """
    Yield a session and manage the connection / closing lifecycle.

    :param redis_ctrl: the Redis controller (injected)
    """
    async with redis_ctrl.session() as session:
        yield session


async def get_platform_ctrl(
    settings: Settings = Depends(get_settings),
    redis_session: Redis = Depends(get_redis_session),
) -> PlatformController:
    """
    Get a new :class:`PlatformController` instance.

    :param settings: application settings (injected)
    :param redis_session: a Redis database session (injected)
    """
    return PlatformController(settings, redis_session)
