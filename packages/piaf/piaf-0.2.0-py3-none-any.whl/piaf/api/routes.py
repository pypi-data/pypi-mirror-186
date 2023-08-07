# coding: utf-8
"""The mod:`piaf.api.routes` modules defines all routes available in the Web API."""
from __future__ import annotations

import asyncio
import json
from typing import TYPE_CHECKING, Any, Dict, List, Union
from uuid import uuid4

import async_timeout as at
from aioredis import Redis
from fastapi import (
    APIRouter,
    Depends,
    Path,
    Query,
    Response,
    WebSocket,
    WebSocketDisconnect,
    status,
)

from piaf.agent import AgentState
from piaf.api.controllers import PlatformController
from piaf.api.dependencies import get_platform_ctrl, get_redis_session
from piaf.api.exceptions import InternalServerError
from piaf.api.models import (
    ACLMessageModel,
    AgentCreationDescriptionModel,
    AgentMemoryModel,
    AgentPlatformModel,
    AgentStateModel,
    AIDModel,
    AMSAgentDescriptionModel,
    ExceptionModel,
)
from piaf.audit import Topic

if TYPE_CHECKING:
    from aioredis.client import PubSub

# V1 router
app_v1 = APIRouter(prefix="/platforms")


@app_v1.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_description="The platform is created",
    response_model=AgentPlatformModel,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "model": ExceptionModel,
            "description": "The operation can't be performed.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Duplicated platform name my-awesome-platform"
                    }
                }
            },
        }
    },
    tags=["Platform"],
)
async def create_platform(
    ptf: AgentPlatformModel,
    platform_ctrl: PlatformController = Depends(get_platform_ctrl),
):
    """
    Create a new AgentPlatform with the provided name.

    **Body**: a description of the platform to be created.
    """
    try:
        async with at.timeout(5):
            await platform_ctrl.create_platform(ptf)
            return ptf
    except asyncio.TimeoutError as e:
        raise InternalServerError() from e


@app_v1.delete(
    "/{name}",
    response_description="The platform is deleted",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "model": ExceptionModel,
            "description": "The operation can't be performed.",
        },
    },
    tags=["Platform"],
)
async def delete_platform(
    name: str = Path(description="The platform's name", example="my-awesome-platform"),
    platform_ctrl: PlatformController = Depends(get_platform_ctrl),
):
    """Stop and delete the desired platform."""
    try:
        async with at.timeout(5):
            await platform_ctrl.stop(name)
    except asyncio.TimeoutError:
        await platform_ctrl.kill(name)


@app_v1.get(
    "",
    response_description="Successfully returns the list of active platforms",
    response_model=List[AgentPlatformModel],
    tags=["Platform"],
)
async def get_platforms(
    platform_ctrl: PlatformController = Depends(get_platform_ctrl),
):
    """Get all the running platforms this application is aware of."""
    return await platform_ctrl.get_all_platforms()


@app_v1.post(
    "/{name}/agents",
    status_code=status.HTTP_201_CREATED,
    response_model=AIDModel,
    response_description="The agent is created",
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "model": ExceptionModel,
            "description": "The operation can't be performed.",
        },
    },
    tags=["Agent"],
)
async def create_agent(
    agent: AgentCreationDescriptionModel,
    name: str = Path(description="The platform's name", example="my-awesome-platform"),
    platform_ctrl: PlatformController = Depends(get_platform_ctrl),
):
    """
    Create and invoke an agent into the specified platform.

    **Body** the description of the agent to create
    """
    task = {"task_type": "CreateAgentTask", "id": str(uuid4())}
    task.update(agent.dict())
    return await platform_ctrl.process_task(name, task)


@app_v1.get(
    "/{ptf_name}/agents",
    response_description="Successfully returns the list of agents",
    response_model=List[AMSAgentDescriptionModel],
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "model": ExceptionModel,
            "description": "The operation can't be performed.",
        },
    },
    tags=["Agent"],
)
async def get_agents(
    ptf_name: str = Path(
        description="The platform's name", example="my-awesome-platform"
    ),
    state: Union[None, AgentState] = Query(
        default=None,
        description="Optionally filter results by only keeping agents with the given state.",
        example="ACTIVE",
    ),
    name: Union[None, str] = Query(
        default=None,
        description="Optionally filter results by only keeping agents whose name contains the provided string.",
        example="agent",
    ),
    platform_ctrl: PlatformController = Depends(get_platform_ctrl),
):
    """Retrieve for the given platform all the agents matching the criteria."""
    task = {
        "task_type": "GetAgentsTask",
        "filters": {
            "state": state.name if state is not None else None,
            "name": name if name is not None else "",
        },
        "id": str(uuid4()),
    }
    return await platform_ctrl.process_task(ptf_name, task)


@app_v1.delete(
    "/{ptf_name}/agents/{name}",
    response_description="The agent is deleted",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "model": ExceptionModel,
            "description": "The operation can't be performed.",
        },
    },
    tags=["Agent"],
)
async def delete_agent(
    ptf_name: str = Path(
        description="The platform's name", example="my-awesome-platform"
    ),
    name: str = Path(
        description="The name of the agent to delete.", example="Custom-1"
    ),
    platform_ctrl: PlatformController = Depends(get_platform_ctrl),
):
    """Delete an agent from the given platform."""
    task = {
        "task_type": "ChangeAgentStateTask",
        "name": name,
        "state": "UNKNOWN",
        "id": str(uuid4()),
    }
    return await platform_ctrl.process_task(ptf_name, task)


@app_v1.get(
    "/{ptf_name}/agents/{name}",
    response_model=AgentMemoryModel,
    response_description="Successfully returns the agent's memory",
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "model": ExceptionModel,
            "description": "The operation can't be performed.",
        },
    },
    tags=["Agent"],
)
async def get_agent_memory(
    ptf_name: str = Path(
        description="The platform's name", example="my-awesome-platform"
    ),
    name: str = Path(description="The name of the agent.", example="Custom-1"),
    platform_ctrl: PlatformController = Depends(get_platform_ctrl),
):
    """Get a snapshot of the current agent's memory."""
    task = {
        "task_type": "RetrieveAgentMemoryTask",
        "aid": {"name": f"{name}@{ptf_name}"},
        "id": str(uuid4()),
    }
    return await platform_ctrl.process_task(ptf_name, task)


@app_v1.post(
    "/{ptf_name}/agents/{name}/messages",
    status_code=status.HTTP_201_CREATED,
    response_description="Successfully sent the message",
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "model": ExceptionModel,
            "description": "The operation can't be performed.",
        },
    },
    tags=["Agent"],
)
async def send_message(
    msg: ACLMessageModel,
    ptf_name: str = Path(
        description="The platform's name", example="my-awesome-platform"
    ),
    name: str = Path(description="The name of the agent.", example="Custom-1"),
    platform_ctrl: PlatformController = Depends(get_platform_ctrl),
):
    """Send a message on the behalf of a specific agent."""
    task = {
        "task_type": "SendMessageTask",
        "id": str(uuid4()),
        "msg": json.loads(msg.json()),
        "sender": f"{name}@{ptf_name}",
    }
    return await platform_ctrl.process_task(ptf_name, task)


@app_v1.put(
    "/{ptf_name}/agents/{name}/state",
    response_description="Successfully updated the agent's state",
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "model": ExceptionModel,
            "description": "The operation can't be performed.",
        },
    },
    tags=["Agent"],
)
async def update_agent_state(
    state: AgentStateModel,
    ptf_name: str = Path(
        description="The platform's name", example="my-awesome-platform"
    ),
    name: str = Path(description="The name of the agent.", example="Custom-1"),
    platform_ctrl: PlatformController = Depends(get_platform_ctrl),
):
    """Replace an agent's state by the provided one."""
    task = {
        "task_type": "ChangeAgentStateTask",
        "name": name,
        "state": state.state.name,
        "id": str(uuid4()),
    }
    return await platform_ctrl.process_task(ptf_name, task)


@app_v1.websocket("/{ptf_name}/ws")
async def topic_listener(
    ptf_name: str,
    websocket: WebSocket,
    redis_session: Redis = Depends(get_redis_session),
) -> None:
    """
    Get a websocket that can listen on the platform's event.

    The websocket supports two methods:

    - subscribe: subscribe to a particular topic
    - unsubscribe: unsubscribe from a particular topic

    Here is the Json object::

        {
            method: "[un]subscribe",
            topic: ".some.topic"
        }

    .. warning:: Contrary to how events are dispatched inside the piaf platform, events are not dispatched to topic's parents. It means that listening on `.platform` won't catch events emitted on `.platform.agents` for example.

    :param ptf_name: the platform's name
    :param websocket: injected by FastAPI
    :param redis_session: a Redis session, injected by FastAPI
    """

    try:
        await websocket.accept()
        pubsub: PubSub = redis_session.pubsub()
        first_sub: bool = True

        while True:
            try:
                data: Dict[str, Any] = await websocket.receive_json()
            except WebSocketDisconnect:
                break

            topic = Topic.from_str(data["topic"])
            if data["method"] == "subscribe":
                await pubsub.subscribe(f"channels:{ptf_name}:events:{topic}")

            if data["method"] == "unsubscribe":
                await pubsub.unsubscribe(f"channels:{ptf_name}:events:{topic}")

            if first_sub:
                task = asyncio.create_task(yield_events(pubsub, websocket))
                first_sub = False
    finally:
        task.cancel()
        await pubsub.close()


async def yield_events(pubsub: PubSub, ws: WebSocket) -> None:
    """
    Asynchronous task that keeps listening on the provided pubsub and yielding downloaded data to the provided websocket.

    :param pubsub: redis publish/subscribe object
    :param ws: websocket
    """
    while True:
        record = await pubsub.get_message(ignore_subscribe_messages=True, timeout=2)
        if record is not None:
            await ws.send_json(json.loads(record["data"]))
        await asyncio.sleep(0)
