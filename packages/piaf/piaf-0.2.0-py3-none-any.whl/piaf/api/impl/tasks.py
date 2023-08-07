# coding: utf-8
"""A collection of predefined tasks to interact from the WebAPI with a simulation."""
from __future__ import annotations

import abc
import asyncio
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, Iterable, List, Tuple
from uuid import UUID, uuid4

from piaf.agent import AgentState
from piaf.comm import AID, MT_CONVERSATION_ID, ACLMessage, Performative
from piaf.service import AgentCreationDescription, AMSAgentDescription, AMSService

if TYPE_CHECKING:
    from piaf.agent import Agent
    from piaf.api.impl.process import APIAgent


class Task(metaclass=abc.ABCMeta):
    """
    An abstraction of a task.

    Each task gets a unique ID number so a response can later be associated. Concrete class should implement two methods:

    - :meth:`Task.from_json` which creates an instance from a JSON-like structure
    - :meth:`Task.execute` which does the actual work
    """

    @staticmethod
    @abc.abstractmethod
    def from_json(json_repr: Dict[str, Any]) -> Task:
        """
        Unpack the given JSON object into a :class:`Task`.

        :param json_repr: the JSON object
        :return: a :class:`Task` object or one of its subclasses
        """
        raise NotImplementedError()

    def __init__(self) -> None:
        """
        Initialize a new :class:`Task` object.

        It generates a new UUID4 an set it as the task's ID.
        """
        self._id: UUID = uuid4()

    @property
    def id(self) -> UUID:
        """
        Get this task's ID.

        :return: an UUID
        """
        return self._id

    @abc.abstractmethod
    async def execute(self, agent: APIAgent) -> Any:
        """
        Realize the work the task is supposed to do.

        :param agent: the :class:`APIAgent` that is executing the task
        :return: whatever the task returns
        """
        raise NotImplementedError()


@dataclass(frozen=True, eq=True)
class TaskResult:
    """
    A small dataclass that stores a task's execution result.

    This class has three fields:

    - error: stores an exception if the execution failed
    - result: the task's execution result, if any
    - task_id: the task's id this result is linked to

    """

    error: BaseException | None
    result: Any
    task_id: UUID


class CreateAgentTask(Task):
    """
    A task that creates a new agent in the platform.

    Given an :class:`piaf.service.AgentCreationDescription` serialized in a JSON object, this task asks the AMS to create and initialize an agent.

    On a successful execution, the task returns the AID of the created agent.
    """

    @staticmethod
    def from_json(json_repr: Dict[str, Any]) -> CreateAgentTask:
        """
        Create a new :class:`CreateAgentTask` from the given JSON object.

        The object must have the following fields:

        - class_name: qualified name of the agent's class
        - agent_name: short name of the agent
        - args: extra arguments given to the agent's constructor
        - is_service: tell if the agent should have a full access to the platform
        """
        return CreateAgentTask(json_repr)

    def __init__(self, agent: Dict[str, Any]) -> None:
        """Initialize a new :class:`CreateAgentTask` with the given JSON object."""
        super().__init__()
        self.agent = agent

    async def execute(self, agent: APIAgent) -> AID:
        """
        Ask the AMS to create an initialize a new agent in the platform.

        :param agent: the :class:`APIAgent` that executes the request
        :return: the AID of the created agent
        :raise Exception: the AMS refuse to create the agent or fail at it
        """
        req: ACLMessage = (
            ACLMessage.Builder()
            .performative(Performative.REQUEST)
            .conversation_id(str(uuid4()))
            .receiver(AID(f"ams@{agent.aid.hap_name}"))
            .content(
                [
                    AMSService.CREATE_AGENT_FUNC,
                    AgentCreationDescription(
                        self.agent["class_name"],
                        self.agent["agent_name"],
                        self.agent["args"],
                        self.agent["is_service"],
                    ),
                ]
            )
            .build()
        )
        agent.send(req)

        # Wait response
        agree_or_refuse = await agent.receive(MT_CONVERSATION_ID(req.conversation_id))
        if agree_or_refuse.acl_message.performative == Performative.REFUSE:
            raise Exception(agree_or_refuse.acl_message.content)

        # Wait result
        result = await agent.receive(MT_CONVERSATION_ID(req.conversation_id))
        if result.acl_message.performative == Performative.FAILURE:
            raise Exception(result.acl_message.content)

        return result.acl_message.content[1]  # type: ignore


class GetAgentsTask(Task):
    """
    A task that queries the AMS about agents in the platform.

    Two filters are available:

    - state: if set, filters out agent that have a different state from the one provided
    - name: filters out agents that don't have the provided string in their short name

    On a successful execution, the task returns a list of :class:`piaf.service.AMSAgentDescription`.
    """

    @staticmethod
    def from_json(json_repr: Dict[str, Any]) -> GetAgentsTask:
        """
        Creates a new :class:`GetAgentsTask` from the given JSON object.

        It uses only the `filters` field, which must contain two entries:

        - `state`: if not `None`, must be the string representation of one of the constants in :class:`piaf.agent.AgentState`
        - `name`: a string to filter out agents by their short name

        """
        return GetAgentsTask(json_repr["filters"])

    def __init__(self, filters: Dict[str, Any]) -> None:
        """
        Initialize a new :class:`GetAgentsTask` instance.

        :param filters: a JSON object that contains the two required fields
        """
        super().__init__()
        self.filters = filters

    async def execute(self, agent: APIAgent) -> List[AMSAgentDescription]:
        """
        Ask the AMS the list of agents in the platform an apply filters.

        :param agent: the APIAgent executing the task
        :return: a list of :class:`piaf.service.AMSAgentDescription`
        :raise Exception: the AMS refuse to perform the request or fail at it
        """
        state = (
            None if self.filters["state"] is None else AgentState[self.filters["state"]]
        )
        req: ACLMessage = (
            ACLMessage.Builder()
            .performative(Performative.REQUEST)
            .conversation_id(str(uuid4()))
            .receiver(AID(f"ams@{agent.aid.hap_name}"))
            .content(
                [
                    AMSService.SEARCH_FUNC,
                    AMSAgentDescription(state=state),  # Filter state
                ]
            )
            .build()
        )
        agent.send(req)

        # Wait response
        agree_or_refuse = await agent.receive(MT_CONVERSATION_ID(req.conversation_id))
        if agree_or_refuse.acl_message.performative == Performative.REFUSE:
            raise Exception(agree_or_refuse.acl_message.content)

        # Wait result
        result = await agent.receive(MT_CONVERSATION_ID(req.conversation_id))
        if result.acl_message.performative == Performative.FAILURE:
            raise Exception(result.acl_message.content)

        # Filter using 'name'
        agents: List[AMSAgentDescription] = result.acl_message.content[1]
        return [
            agent for agent in agents if self.filters["name"] in agent.name.short_name
        ]


class ChangeAgentStateTask(Task):
    """
    A task that can manipulate the state of an agent through the AMS.

    It asks the AMS to update the agent's state and return nothing on success.
    """

    @staticmethod
    def from_json(json_repr: Dict[str, Any]) -> ChangeAgentStateTask:
        """
        Initialize a new :class:`ChangeAgentStateTask` object from the given JSON object.

        It expects the following fields:

        - name: the agent's short name
        - state: the string representation of the desired state

        """
        return ChangeAgentStateTask(json_repr["name"], json_repr["state"])

    def __init__(self, name: str, state: str) -> None:
        """
        Initialize the new :class:`ChangeAgentStateTask` instance.

        :param name: the agent's short name
        :param state: the new state, as a string
        """
        super().__init__()
        self._name = name
        self._state = state

    async def execute(self, agent: APIAgent) -> None:
        """
        Call the MODIFY function of the AMS in order to change the agent's state.

        :param agent: the agent executing the task.
        :raise Exception: the AMS refused or failed to modify the state
        """
        req: ACLMessage = (
            ACLMessage.Builder()
            .performative(Performative.REQUEST)
            .conversation_id(str(uuid4()))
            .receiver(AID(f"ams@{agent.aid.hap_name}"))
            .content(
                [
                    AMSService.MODIFY_FUNC,
                    AMSAgentDescription(
                        name=AID(f"{self._name}@{agent.aid.hap_name}"),
                        state=AgentState[self._state],
                    ),
                ]
            )
            .build()
        )
        agent.send(req)

        # Wait response
        agree_or_refuse = await agent.receive(MT_CONVERSATION_ID(req.conversation_id))
        if agree_or_refuse.acl_message.performative == Performative.REFUSE:
            raise Exception(agree_or_refuse.acl_message.content)

        # Wait result (expect an inform)
        result = await agent.receive(MT_CONVERSATION_ID(req.conversation_id))
        if result.acl_message.performative == Performative.FAILURE:
            raise Exception(result.acl_message.content)


class StopPlatformTask(Task):
    """
    A task to stop the platform as soon as possible.

    The agent will close its Redis connection and make the platform stop. Both actions are spawned in a dedicated task to be executed later.
    """

    @staticmethod
    def from_json(ignored: Dict[str, Any]) -> StopPlatformTask:
        """
        Initialize a new :class:`StopPlatformTask` object from the given JSON object.

        It expects no dedicated fields.
        """
        return StopPlatformTask()

    async def execute(self, agent: APIAgent) -> None:
        """Schedule the Redis connection closing and the platform death."""
        asyncio.create_task(agent._platform.stop())


class RetrieveAgentMemoryTask(Task):
    """
    A task to export a snapshot of an agent's memory.

    Only public, non-callable field are included.
    """

    @staticmethod
    def from_json(json_repr: Dict[str, Any]) -> RetrieveAgentMemoryTask:
        """
        Initialize a new :class:`RetrieveAgentMemoryTask` with the provided information.

        It requires one field named `aid`, which itself must contain a `name` field containing the target's fully-qualified name.
        """
        return RetrieveAgentMemoryTask(AID(json_repr["aid"]["name"]))

    def __init__(self, target: AID) -> None:
        """
        Initialize a new :class:`RetrieveAgentMemoryTask`.

        :param target: the AID of the targeted agent
        """
        self.target = target

    async def execute(self, agent: APIAgent) -> Dict[str, Any]:
        try:
            ctx = agent._platform.agent_manager._contexts[self.target]
            target: Agent = ctx.agent

            attrs: Iterable[Tuple[str, Any]] = (
                (attr_name, getattr(target, attr_name)) for attr_name in dir(target)
            )
            memory: Dict[str, Any] = {
                attr: value for (attr, value) in attrs if self._filter_attr(attr, value)
            }
            return {"target": self.target, "memory": memory}

        except KeyError:
            raise Exception(f"No agent with AID={self.target}")

    def _filter_attr(self, attr_name: str, attr_value: Any) -> bool:
        """
        Given an attribute name and value, decide if it should be included in the memory snapshot.

        Excluded attributes are:

        - private attributes (starting with '_')
        - callables (exclude methods)
        - piaf non serializable attributes: state_sync, logger and mailbox

        :param attr_name: name of the attribute
        :param attr_value: value of the attribute
        :return: `True` if the attribute can be included in the memory snapshot, `False` otherwise.
        """
        return (
            (attr_name not in ("state_sync", "logger", "mailbox"))
            and (not attr_name.startswith("_"))
            and (not callable(attr_value))
        )


class SendMessageTask(Task):
    """
    A task that sends, using the given agent's identity, the given message.

    If the sender identity doesn't exist, then the task raises an exception.
    """

    @staticmethod
    def from_json(json_repr: Dict[str, Any]) -> SendMessageTask:
        """
        Initialize a new :class:`SendMessageTask` with the provided information.

        It requires two fields:

        - `sender`, which must contain at least a `name` field containing the full name of the sender agent
        - `msg`, which must contain four fields:
            - `performative`: the message's performative
            - `receivers`: a list of AIDs
            - `conversation_id`: an optional conversation ID
            - `content`: the message content

        """
        msg: Dict[str, Any] = json_repr["msg"]
        sender: AID = AID(json_repr["sender"])
        return SendMessageTask(
            sender,
            ACLMessage.Builder()
            .performative(msg["performative"])
            .receiver([AID(r["name"]) for r in msg["receivers"]])
            .conversation_id(
                msg["conversation_id"]
                if msg.get("conversation_id", None) is not None
                else uuid4()
            )
            .content(msg["content"])
            .build(),
        )

    def __init__(self, sender: AID, msg: ACLMessage) -> None:
        """
        Instantiate a new :class:`SendMessageTask` using the provided sender and the provided message.

        :param sender: which agent is going to send the message
        :param msg: the message to send
        """
        self.sender = sender
        self.msg = msg

    async def execute(self, agent: APIAgent) -> Any:
        try:
            ctx = agent._platform.agent_manager._contexts[self.sender]
            target: Agent = ctx.agent

            target.send(self.msg)

        except KeyError:
            raise Exception(f"No agent with AID={self.sender}")
