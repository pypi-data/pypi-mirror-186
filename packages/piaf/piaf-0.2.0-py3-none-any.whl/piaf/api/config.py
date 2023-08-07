# coding: utf-8
"""Configuration module."""
from __future__ import annotations

from typing import Any, Tuple

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # CORS configuration
    cors_origins: Tuple[str] = ("*",)
    cors_methods: Tuple[str] = ("*",)
    cors_headers: Tuple[str] = ("*",)
    cors_credentials: bool = True

    # Redis database configuration
    redis_host: str
    redis_user: str
    redis_password: str
    redis_db: int = 0
    redis_max_connections: int = 10
    redis_scheme: str = "redis"

    class Config:
        """Extra configuration."""

        env_file = ".env"

    def __eq__(self, other: Any) -> bool:
        """
        Equality.

        :param other: the other object
        :return: `True` if all attributes are equal, `False` otherwise.
        """
        if not isinstance(other, type(self)):
            return False
        return all(
            getattr(other, name) == getattr(self, name) for name in self.__dict__
        )

    def __hash__(self) -> int:
        """Get this instance's hash code."""
        return hash(tuple(val for val in self.__dict__.values()))
