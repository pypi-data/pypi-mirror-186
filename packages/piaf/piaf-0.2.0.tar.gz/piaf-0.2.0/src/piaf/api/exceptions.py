# coding: utf-8
"""All exceptions and errors that can occur in the WebAPI."""
from __future__ import annotations

from typing import Any, Dict

from fastapi import HTTPException


class BadRequestException(HTTPException):
    """Base exception for all client-related errors (4XX)."""

    def __init__(
        self, code: int = 400, detail: Any = None, headers: Dict[str, Any] | None = None
    ) -> None:
        """
        Create a new :class:`BadRequestException` instance.

        :param code: HTTP code, must be 4XX (default is 400)
        :param detail: optional detail about what happened
        :param headers: additional headers
        """
        super().__init__(code, detail, headers)


class InternalServerError(HTTPException):
    """Base exception for all server-related errors (5XX)."""

    def __init__(
        self, code: int = 500, detail: Any = None, headers: Dict[str, Any] | None = None
    ) -> None:
        """
        Create a new :class:`InternalServerError` instance.

        :param code: HTTP code, must be 5XX (default is 500)
        :param detail: optional detail about what happened
        :param headers: additional headers
        """
        super().__init__(500, detail, headers)


class DuplicatedPlatformNameError(BadRequestException):
    """Client error indicating the provided platform's name already exists."""

    def __init__(self, name: str) -> None:
        """
        Create a new :class:`DuplicatedPlatformNameError` instance.

        :param name: the duplicated name.
        """
        super().__init__(detail=f"Duplicated platform name {name}")


class UnknownPlatformError(BadRequestException):
    """Client error telling there is no platform named like asked."""

    def __init__(self, name: str) -> None:
        """
        Create a new :class:`UnknownPlatformError` instance.

        :param name: the provided platform's name
        """
        super().__init__(detail=f"Unknown platform with name {name}")


class RedisError(InternalServerError):
    """Base class for Redis-related errors."""

    pass


class RedisUnavailableError(RedisError):
    """A server error telling the Redis database can't be reached for some reason."""

    def __init__(self) -> None:
        """Create a new :class:`RedisUnavailableError` instance."""
        super().__init__(detail="Can't reach the Redis database.")


class RedisConnectionNotInitialized(RedisError):
    """A server error telling the connection is not initialized yet."""

    def __init__(self) -> None:
        """Create a new :class:`RedisConnectionNotInitialized` instance."""
        super().__init__(detail="No Redis connection initialized.")
