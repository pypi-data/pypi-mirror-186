# coding: utf-8
# /usr/bin/env python3
"""
The :mod:`piaf.service` module defines a set of services the platform may offer to running agents.

Except the :class:`AMSService` service, if you want to activate a service you have to start it like a regular agent.
The only key difference is that services have a privileged access to the platform. To enable this special access, you
must set the `is_service` parameter in :meth:`piaf.ptf.AgentManager.create` method to `True`.
"""
from __future__ import annotations

import importlib
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Sequence, Set, Tuple

from piaf.agent import Agent, AgentState
from piaf.behavior import Behavior
from piaf.comm import AID, MT_NOT, MT_OR, MT_PERFORMATIVE, ACLMessage, Performative
from piaf.exceptions import DuplicatedNameException
from piaf.util import *

if TYPE_CHECKING:
    import piaf.comm
    import piaf.ptf


class AMSService(Agent):
    """
    Special agent providing Agent Management Services.

    The AMS is a required component of the agent platform. It allows others agents to query the platform capabilities
    and other agents AIDs.

    The AMS uses the underlying platform to discover registered agents.

    .. warning:: For now, the AMS agent only supports the search, the modify and the create-agent requests.

    Specification: http://fipa.org/specs/fipa00023/SC00023K.html
    """

    SEARCH_FUNC = "search"
    CREATE_AGENT_FUNC = "create_agent"
    MODIFY_FUNC = "modify"

    def __init__(self, aid: piaf.comm.AID, platform: piaf.ptf.AgentPlatformFacade):
        """
        Create a new AMS Agent with the provided information.

        :param aid: this agent's identifier
        :param platform: the platform where this AMS agent is deployed
        """
        super().__init__(aid, platform)

        # Add behaviors
        self.add_behavior(_AMSRequestBehavior(self))
        self.add_behavior(_HandleInvalidMessageBehavior(self))


class _BaseRequestBehavior(FIPARequestProtocolBehavior, metaclass=ABCMeta):
    """Base implementation for request protocol handling by both the  AMS and the DF."""

    #: Acceptable messages for this Request protocol
    VALID_MSG_TEMPLATE = MT_OR(
        MT_PERFORMATIVE(Performative.REQUEST), MT_PERFORMATIVE(Performative.CANCEL)
    )

    def check_message(self, msg: ACLMessage) -> bool:
        """
        Check the content of the provided message.

        * Not a sequence      -> NOT_UNDERSTOOD, unsupported-value
        * Length == 0         -> REFUSE, missing-parameter
        * First param not str -> REFUSE, unrecognized-parameter-value

        :param msg: message to check
        :return: True if message is ok, False otherwise
        """
        content = msg.content
        result = False

        if not isinstance(content, (List, tuple)):
            self.agent.send(
                not_understood_message_from_request(msg, "Unsupported value: content")
            )

        elif len(content) == 0:
            self.agent.send(
                refuse_message_from_request(msg, "Missing parameter: function_name")
            )

        elif not isinstance(content[0], str):
            self.agent.send(
                refuse_message_from_request(
                    msg, f"Unrecognized parameter value: function_name, {content[0]}"
                )
            )

        else:
            result = True

        return result

    @property
    def msg_template(self) -> piaf.comm.MessageTemplate:
        return _BaseRequestBehavior.VALID_MSG_TEMPLATE


class _AMSRequestBehavior(_BaseRequestBehavior):
    """Custom implementation of the class:`FIPARequestProtocolBehavior` for the AMS agent."""

    async def on_valid_request(self, msg: ACLMessage) -> None:
        """
        Depending on the message content, the AMS agent is executing the request.

        For now, only the SEARCH function is supported.

        :param msg: the request message to handle
        """
        # If function is the search function
        if msg.content[0] == AMSService.SEARCH_FUNC:
            await self._handle_search_request(msg)

        # If function is the create-agent function
        elif msg.content[0] == AMSService.CREATE_AGENT_FUNC:
            await self._handle_create_agent_request(msg)

        # If function is the modify function
        elif msg.content[0] == AMSService.MODIFY_FUNC:
            await self._handle_modify_request(msg)

        # Unsupported function
        else:
            self.agent.send(
                refuse_message_from_request(
                    msg, f"Unsupported function: {msg.content[0]}"
                )
            )

    async def _handle_search_request(self, msg: ACLMessage) -> None:
        """Execute the `search` function if possible and send the reply."""
        # At least the mandatory parameter ams-agent-description
        if len(msg.content) < 2:
            self.agent.send(
                refuse_message_from_request(
                    msg, "Missing argument: ams-agent-description"
                )
            )
            return

        # At most 2 parameters : ams-agent-description and the optional parameter search-constraints
        if len(msg.content) > 3:
            self.agent.send(
                refuse_message_from_request(msg, "Unexpected argument count")
            )
            return

        # ams-agent-description must be a AMSAgentDescription
        if not isinstance(msg.content[1], AMSAgentDescription):
            self.agent.send(
                refuse_message_from_request(
                    msg,
                    f"Unrecognised parameter value: ams-agent-description, {msg.content[1]}",
                )
            )
            return

        # If present, search-constraints parameter must be a SearchConstraints
        if len(msg.content) == 3 and not isinstance(msg.content[2], SearchConstraints):
            self.agent.send(
                refuse_message_from_request(
                    msg,
                    f"Unrecognised parameter value: search-constraints, {msg.content[2]}",
                )
            )
            return

        ams_agent_description = msg.content[1]
        am = self.agent._platform.agent_manager
        agents = am.get_agents(ams_agent_description.state)
        agt_descriptions = []

        # Perform the search
        self.agent.send(agree_message_from_request(msg))

        if ams_agent_description.name is not None:
            if ams_agent_description.name in agents:
                agt_descriptions.append(
                    AMSAgentDescription(
                        ams_agent_description.name,
                        None,
                        am.get_state(ams_agent_description.name),
                    )
                )

        else:
            agt_descriptions = [
                AMSAgentDescription(agent, None, am.get_state(agent))
                for agent in agents
            ]

        # Constrain if applicable
        if len(msg.content) == 3:
            max_results = msg.content[2].max_results
            if max_results is not None:
                agt_descriptions = agt_descriptions[:max_results]

        # Send the result
        self.agent.send(
            inform_message_from_request(msg, [msg.content, agt_descriptions])
        )

    async def _handle_create_agent_request(self, msg: ACLMessage) -> None:
        # At least the mandatory parameter agent-creation-description
        if len(msg.content) < 2:
            self.agent.send(
                refuse_message_from_request(
                    msg, "Missing argument: agent-creation-description"
                )
            )
            return

        # At most 1 parameter : agent-creation-description
        if len(msg.content) > 2:
            self.agent.send(
                refuse_message_from_request(msg, "Unexpected argument count")
            )
            return

        # agent-creation-description must be a AgentCreationDescription
        if not isinstance(msg.content[1], AgentCreationDescription):
            self.agent.send(
                refuse_message_from_request(
                    msg,
                    f"Unrecognised parameter value: agent-creation-description, {msg.content[1]}",
                )
            )
            return

        # Agree request
        self.agent.send(agree_message_from_request(msg))

        # Try to instantiate the class
        description: AgentCreationDescription = msg.content[1]

        class_path = description.class_name.split(".")
        if len(class_path) <= 1:
            self.agent.send(failure_message_from_request(msg, "No module provided."))
            return

        module_name = ".".join(class_path[:-1])
        class_name = class_path[-1]

        try:
            module = importlib.import_module(module_name)
            agent_class = getattr(module, class_name)
        except ModuleNotFoundError:
            self.agent.send(
                failure_message_from_request(msg, f"No module named '{module_name}'")
            )
            return
        except AttributeError:
            self.agent.send(
                failure_message_from_request(
                    msg,
                    f"No agent class named '{class_name}' in module '{module_name}'",
                )
            )
            return

        try:
            if description.args is not None:
                aid = await self.agent._platform.agent_manager.create(
                    agent_class,
                    description.agent_name,
                    description.is_service,
                    description.args,
                )
            else:
                aid = await self.agent._platform.agent_manager.create(
                    agent_class,
                    description.agent_name,
                    description.is_service,
                )
            await self.agent._platform.agent_manager.invoke(aid)
            self.agent.send(inform_message_from_request(msg, [msg.content, aid]))
        except DuplicatedNameException as e:
            self.agent.send(
                failure_message_from_request(
                    msg,
                    str(e),
                )
            )
        except Exception as e:
            self.agent.send(
                failure_message_from_request(msg, f"Internal error: {str(e)}")
            )

    async def _handle_modify_request(self, msg: ACLMessage) -> None:
        """Handle an incoming modification request."""
        content: List[str | Any] = msg.content
        if len(content) < 2:
            self.agent.send(
                refuse_message_from_request(
                    msg, "Missing parameter: ams-agent-description"
                )
            )
            return

        if len(content) > 2:
            self.agent.send(
                refuse_message_from_request(msg, "Unexpected argument count")
            )
            return

        ams_agent_description = content[1]
        if not isinstance(ams_agent_description, AMSAgentDescription):
            self.agent.send(
                refuse_message_from_request(
                    msg,
                    f"Unrecognised parameter value: agent-creation-description, {ams_agent_description}",
                )
            )
            return

        self.agent.send(agree_message_from_request(msg))

        # This feature is deactivated because otherwise the modify function has very little interest.
        # Once the ownership is implemented, it could become interesting to limit agent state modification to both the agent itself and its owner
        # if (
        #     ams_agent_description.name is not None
        #     and ams_agent_description.name != msg.sender
        # ):
        #     self.agent.send(failure_message_from_request(msg, "Unauthorized"))
        #     return

        if ams_agent_description.ownership is not None:
            self.agent.send(failure_message_from_request(msg, "Unsupported: ownership"))
            return

        state = ams_agent_description.state

        if state is None:
            self.agent.send(failure_message_from_request(msg, "Missing new state"))
            return

        if state not in [
            AgentState.ACTIVE,
            AgentState.SUSPENDED,
            AgentState.UNKNOWN,
        ]:
            self.agent.send(
                failure_message_from_request(msg, f"Unsupported state: {state}")
            )
            return

        am: piaf.ptf.AgentManager = self.agent._platform.agent_manager

        # Compute AID (if omitted, use the sender)
        aid: AID = ams_agent_description.name  # type: ignore
        if aid is None:
            aid = msg.sender

        try:
            if state == AgentState.ACTIVE:
                await am.resume(aid)
            elif state == AgentState.SUSPENDED:
                await am.suspend(aid)
            else:
                await am.quit(aid)
            self.agent.send(inform_message_from_request(msg, msg.content))
        except Exception as e:
            self.agent.send(failure_message_from_request(msg, str(e)))


class _HandleInvalidMessageBehavior(Behavior):
    """
    Handle all messages not matching the template defined in :class:`_BaseRequestBehavior`.

    If such message is found then this behavior sends a `NOT_UNDERSTOOD` message.
    """

    def done(self) -> bool:
        """Infinite behavior."""
        return False

    async def action(self) -> None:
        """Wait for messages and send `NOT_UNDERSTOOD` message."""
        msg = await self.agent.receive(MT_NOT(_BaseRequestBehavior.VALID_MSG_TEMPLATE))
        self.agent.send(
            not_understood_message_from_request(
                msg.acl_message, f"Unsupported Act: {msg.acl_message.performative}"
            )
        )


@dataclass(eq=True, frozen=True)
class AMSAgentDescription:
    """
    :class:`AMSAgentDescription` objects are returned when querying the AMS agent about agents in the platform.

    Fields are:

    - **name**: the :class:`AID` of the agent
    - **ownership**: who owns it
    - **state**: the agent current state (at the time the AMS queried it)

    It is part of the fipa-agent-management ontology. See http://fipa.org/specs/fipa00023/SC00023K.html.
    """

    name: None | AID = None
    ownership: None | str = None
    state: None | AgentState = None


@dataclass(eq=True, frozen=True)
class AgentPlatformService:
    """
    Description of a platform service.

    Fields are:

    - **name**: name of the service
    - **type**: type of the service. For example: "fipa.mtp.http"
    - **addresses**: a sequence of urls where to access the service

    It is part of the fipa-agent-management ontology. See http://fipa.org/specs/fipa00023/SC00023K.html.
    """

    name: str
    type: str
    addresses: Sequence[str]


@dataclass(eq=True, frozen=True)
class AgentPlatformDescription:
    """
    Description of the AgentPlatform.

    Fields are:

    - **name**: the name of the agent platform
    - **ap_services**: a set of services this platform provides

    It is part of the fipa-agent-management ontology. See http://fipa.org/specs/fipa00023/SC00023K.html.
    """

    name: str
    ap_services: Set[AgentPlatformService]


@dataclass(eq=True, frozen=True)
class Property:
    """
    :class:`Property` objects are usefull for specifying parameter/value pairs.

    Part of the fipa-agent-management ontology. See http://fipa.org/specs/fipa00023/SC00023K.html.
    """

    name: str
    value: Any


@dataclass(eq=True, frozen=True)
class AgentCreationDescription:
    """
    Each object of type :class:`AgentCreationDescription` describes how to create and invoke an agent using the AMS service.

    .. note:: Not part of the official fipa-agent-management ontology but rather an extension to support agent creation like
        described in the specification at http://fipa.org/specs/fipa00023/SC00023K.html.
    """

    class_name: str
    agent_name: str
    args: List[Any] | None = None
    is_service: bool = True


class DFService(Agent):
    """
    The DFService acts like yellow pages

    This service stores agent capabilities on demand (meaning that each agent must register itself to this service). It
    supports all operations defined in the fipa specification :

    - register: register a new agent description
    - deregister: remove an agent description
    - search: perform a search (with a search pattern and constraints) against all records
    - modify: modify an existing record

    .. note:: The DFService currently doesn't support the federated DF mechanism desfined in fipa specification.
    """

    REGISTER_FUNC = "register"
    DEREGISTER_FUNC = "deregister"
    SEARCH_FUNC = "search"
    MODIFY_FUNC = "modify"

    def __init__(self, aid: piaf.comm.AID, platform: piaf.ptf.AgentPlatform):
        super().__init__(aid, platform)

        # Store agents and services descriptions
        self.storage: Dict[AID, DFAgentDescription] = {}

        self.add_behavior(_HandleInvalidMessageBehavior(self))
        self.add_behavior(_DFRequestBehavior(self))


class _DFRequestBehavior(_BaseRequestBehavior):
    async def on_valid_request(self, msg: ACLMessage) -> None:
        """
        Depending on the message content, the DF agent is executing the request.

        For now, only the REGISTER function is supported.

        :param msg: the request message to handle
        """
        # If function is the register function
        if msg.content[0] == DFService.REGISTER_FUNC:
            await self._handle_registration_request(msg, True)

        # If function is the deregister function
        elif msg.content[0] == DFService.DEREGISTER_FUNC:
            await self._handle_registration_request(msg, False)

        # If function is the search function
        elif msg.content[0] == DFService.SEARCH_FUNC:
            await self._handle_search_request(msg)

        # If function is the modify function
        elif msg.content[0] == DFService.MODIFY_FUNC:
            await self._handle_modify_request(msg)

        # Unsupported function
        else:
            self.agent.send(
                refuse_message_from_request(
                    msg, f"Unsupported function: {msg.content[0]}"
                )
            )

    async def _handle_registration_request(
        self, msg: ACLMessage, register: bool
    ) -> None:
        """
        Handle a register / deregister request.

        :param msg: the request
        :param register: whether this is a register request (`True`)  or a deregister one (`False`)
        """
        # Expected arity is 1
        try:
            df_agt_description = msg.content[1]
        except IndexError:
            self.agent.send(
                refuse_message_from_request(
                    msg, "Missing argument: df agent description"
                )
            )
            return

        # Parameter type should be DFAgentDescription
        if not isinstance(df_agt_description, DFAgentDescription):
            self.agent.send(
                refuse_message_from_request(
                    msg,
                    f"Unrecognised parameter value: df agent description, {df_agt_description}",
                )
            )
            return

        # Message is well formed, we can handle it
        self.agent.send(agree_message_from_request(msg))

        if register:
            # Agent must not be registered
            if df_agt_description.name in self.agent.storage:
                self.agent.send(failure_message_from_request(msg, "Already registered"))
                return

            # Everything is ok, we can process the registration
            self.agent.storage[df_agt_description.name] = df_agt_description
            self.agent.send(inform_message_from_request(msg, msg.content))
        else:
            # Agent must be registered
            if df_agt_description.name not in self.agent.storage:
                self.agent.send(failure_message_from_request(msg, "Not registered"))
                return

            # Everything is ok, we can process the deregister request
            del self.agent.storage[df_agt_description.name]
            self.agent.send(inform_message_from_request(msg, msg.content))

    async def _handle_search_request(self, msg: ACLMessage) -> None:
        """
        Handle a search request.

        Message content must contains at least one parameter called df-agent-description and eventually another one
        called search-constraints. If the conditions are not met, then a REFUSE message is sent with the appropriate
        error class.

        Otherwise, two messages are sent: an AGREE, followed by an inform containing the result.

        This implementation doesn't support the federated DF feature for now. As a result, max-depth and search-id
        constraints are ignored.

        :param msg: message containing the search request
        """
        # At least the mandatory parameter df-agent-description
        if len(msg.content) < 2:
            self.agent.send(
                refuse_message_from_request(
                    msg, "Missing argument: df-agent-description"
                )
            )
            return

        # At most 2 parameters : df-agent-description and the optional parameter search-constraints
        if len(msg.content) > 3:
            self.agent.send(
                refuse_message_from_request(msg, "Unexpected argument count")
            )
            return

        # df-agent-description must be a DFAgentDescription
        if not isinstance(msg.content[1], DFAgentDescription):
            self.agent.send(
                refuse_message_from_request(
                    msg,
                    f"Unrecognised parameter value: df-agent-description, {msg.content[1]}",
                )
            )
            return

        # If present, search-constraints parameter must be a SearchConstraints
        if len(msg.content) == 3 and not isinstance(msg.content[2], SearchConstraints):
            self.agent.send(
                refuse_message_from_request(
                    msg,
                    f"Unrecognised parameter value: search-constraints, {msg.content[2]}",
                )
            )
            return

        # Everything is fine, we can handle the request
        self.agent.send(agree_message_from_request(msg))

        result = self._filter_descriptions(msg.content[1])

        # Constraint result
        if len(msg.content) == 3:
            constraints: "SearchConstraints" = msg.content[2]
            if constraints.max_results is not None:
                result = result[: constraints.max_results]

        self.agent.send(inform_message_from_request(msg, [msg.content, result]))

    async def _handle_modify_request(self, msg: ACLMessage) -> None:
        """
        Handle a modify request.

        Expect one argument named df-agent-description of type :class:`DFAgentDescription` which is the new description
        for the sender agent. If an agent tries to modify the description of an other agent, a failure message will be
        sent.

        :param msg: modify request
        """
        # At least the mandatory parameter df-agent-description
        if len(msg.content) < 2:
            self.agent.send(
                refuse_message_from_request(
                    msg, "Missing argument: df-agent-description"
                )
            )
            return

        # At most 2 parameters : df-agent-description and the optional parameter search-constraints
        if len(msg.content) > 2:
            self.agent.send(
                refuse_message_from_request(msg, "Unexpected argument count")
            )
            return

        # df-agent-description must be a DFAgentDescription
        if not isinstance(msg.content[1], DFAgentDescription):
            self.agent.send(
                refuse_message_from_request(
                    msg,
                    f"Unrecognised parameter value: df-agent-description, {msg.content[1]}",
                )
            )
            return

        # Everything is fine, we can handle the request
        self.agent.send(agree_message_from_request(msg))

        # If sender is modifying description of another agent, failure
        if msg.content[1].name != msg.sender:
            self.agent.send(failure_message_from_request(msg, "Unauthorized"))
            return

        # If record doesn't exist, then failure
        if msg.content[1].name not in self.agent.storage:
            self.agent.send(failure_message_from_request(msg, "Not registered"))
            return

        # Otherwise perform the change
        self.agent.storage[msg.content[1].name] = msg.content[1]
        self.agent.send(inform_message_from_request(msg, msg.content))

    def _filter_descriptions(
        self, filter_description: DFAgentDescription
    ) -> List[DFAgentDescription]:
        """
        Filter all registered descriptions given the filter.

        :param filter_description: filter against registered descriptions will be tested
        """
        return list(
            filter(
                lambda e: _match_description(e, filter_description),
                self.agent.storage.values(),
            )
        )


def _match_description(
    description: DFAgentDescription, description_filter: DFAgentDescription
) -> bool:
    """
    Decide if the given `description` match the provided filter.

    :param description: description to be filtered
    :param description_filter: filter to test the description against
    :return: `True` if the description matches, `False` otherwise
    """
    return (
        (description_filter.name is None or description.name == description_filter.name)
        and (
            description_filter.services is None
            or set(description_filter.services) <= set(description.services)
        )
        and (
            description_filter.protocols is None
            or set(description_filter.protocols) <= set(description.protocols)
        )
        and (
            description_filter.ontologies is None
            or set(description_filter.ontologies) <= set(description.ontologies)
        )
        and (
            description_filter.languages is None
            or set(description_filter.languages) <= set(description.languages)
        )
        and (
            description_filter.lease_time is None
            or description_filter.lease_time == description.lease_time
        )
        and (
            description_filter.scope is None
            or description_filter.scope == description.scope
        )
    )


@dataclass(eq=True, frozen=True)
class ServiceDescription:
    """
    Description of each service registered with the DF.

    Available properties are:

    - **name**: name of the service
    - **type**: a string describing what kind of service it is. For example : "fipa-df"
    - **protocols**: protocols this agent supports. For example: "fipa-request"
    - **ontologies**: ontologies this agent understands. For example: "fipa-agent-management"
    - **languages**: languages this agent understands. For example: "fipa-sl0"
    - **ownership**: the owner of the service
    - **properties**: a set of properties

    It is part of the fipa-agent-management ontology. See http://fipa.org/specs/fipa00023/SC00023K.html.
    """

    name: str | None = None
    type: str | None = None
    protocols: Tuple[str, ...] = ()
    ontologies: Tuple[str, ...] = ()
    languages: Tuple[str, ...] = ()
    ownership: str | None = None
    properties: Tuple[Property, ...] = ()


@dataclass(eq=True, frozen=True)
class DFAgentDescription:
    """
    Description that can be registered with the DF service.

    - **name**: :class:`AID` of the agent
    - **services**: A set of services this agent supports
    - **protocols**: A list of interaction protocols this agent supports
    - **ontologies**:  A list of ontologies this agent supports. For example: "fipa-agent-management"
    - **languages**: A list of languages (for example "fipa-sl0") this agent knows.
    - **lease-time**: The duration or time at which the lease for this registration will expire
    - **scope**: Visibility of the record. Can be either local or global (default is global)

    This object is part of the fipa-agent-management ontology. See http://fipa.org/specs/fipa00023/SC00023K.html.
    """

    name: AID | None = None
    services: Tuple[ServiceDescription, ...] = ()
    protocols: Tuple[str, ...] = ()
    ontologies: Tuple[str, ...] = ()
    languages: Tuple[str, ...] = ()
    lease_time: datetime | None = None
    scope: str = "global"


@dataclass(eq=True, frozen=True)
class SearchConstraints:
    """
    This object is used to constraint the results of a search (either in the AMS or DF).

    It contains the following fields:

    - **max_depth**: if the DF agent supports federation, use this parameter to limit the request propagation.
    - **max_results**: limit the number of results returned by the request
    - **search_id**: assign a globally unique identifier for this search request

    Part of the fipa-agent-management ontology, see http://fipa.org/specs/fipa00023/SC00023K.html
    """

    max_depth: int | None = None
    max_results: int | None = None
    search_id: str | None = None
