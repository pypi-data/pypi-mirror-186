# coding: utf-8
"""
The base module for the Web API part of piaf.

It contains the `FastAPI` application and it imports routes from the :mod:`piaf.api.routes` module.
The application server can be launched using `uvicorn` (or any other production server).
"""
from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import piaf
from piaf.api.dependencies import get_redis_ctrl, get_settings
from piaf.api.routes import app_v1

# Main application
description = """
The Piaf platforms API let you create, manage and delete Piaf platforms.

The API exposes several endpoints related to platforms (create, delete and get running platforms) and agents (create, delete, get state, ...).

Websocket
---------

In addition to the following routes, this API exposes a websocket allowing applications to (un)subscribe to/from event topics. The dedicated route is `ws://{server}/platforms/{ptf_name}/ws` and it is a double-sided websocket carrying JSON data. The client can send the following:

    {
        method: "[un]subscribe",
        topic: ".some.topic"
    }

Once an event is emitted on the subscribed topic, the client receives through the websocket a JSON representation of the `EventRecord`:

    {
        "event": {
            "source": "some_source",
            "type": "some_type",
            "data": ...
        },
        "timestamp": 1663923272,
        "topics": [".platform.agents", ".platform.agents.ams"]
    }

**Warning**: Contrary to how events are dispatched inside the piaf platform, events are not dispatched to topic's parents. It means that listening on `.platform` won't catch events emitted on `.platform.agents` for example.
"""

app = FastAPI(
    title="Piaf platforms management API",
    description=description,
    version=piaf.__version__,
    license_info={"name": "MIT", "url": "https://mit-license.org/"},
    openapi_tags=[
        {"name": "Platform", "description": "Operations with platforms."},
        {"name": "Agent", "description": "Manage agents in a particular platform."},
    ],
)

# Configure CORS
settings = get_settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=settings.cors_credentials,
    allow_methods=settings.cors_methods,
    allow_headers=settings.cors_headers,
)

# API version 1
app.include_router(app_v1, prefix="/v1")


@app.on_event("startup")
async def initialize_connection() -> None:
    """Initialize the Redis connection used by the WebAPI."""
    await get_redis_ctrl().connect()


@app.on_event("shutdown")
async def close_connection() -> None:
    """Close the Redis connection before stopping the server."""
    await get_redis_ctrl().close()
