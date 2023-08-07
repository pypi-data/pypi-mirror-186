# coding: utf-8
"""
A small program testing the DF capabilities.

This module defines a service called :class:`FIPAWebService` which can send HTML pages from the `FIPA Website(http://fipa.org)`_
"""
from __future__ import annotations
import asyncio
from http.client import HTTPConnection, HTTPResponse

from piaf.agent import Agent
from piaf.behavior import Behavior
from piaf.service import DFAgentDescription, DFService, ServiceDescription
from piaf.comm import AID, MT_CONVERSATION_ID, ACLMessage, Performative
from piaf.ptf import AgentPlatformFacade
from piaf.util import (
    FIPARequestProtocolBehavior,
    agree_message_from_request,
    inform_message_from_request,
    not_understood_message_from_request,
)


class FIPAWebPageService(Agent):
    """
    A service which sends the first 200 characters of FIPA website page.

    The service supports the FIPA Request protocol. The message content is expected to be the page path, in str format.
    """

    def __init__(self, aid: AID, platform: AgentPlatformFacade):
        super().__init__(aid, platform)

        # Initialize behaviors
        self.add_behavior(FIPAWebPageRequestProtocolBehavior(self))
        self.add_behavior(RegisterFIPAWebPageServiceBehavior(self))


class FIPAWebPageRequestProtocolBehavior(FIPARequestProtocolBehavior):
    """
    This behavior handle incoming request and retrieves the requested page.

    It supports the full Request Protocol and sends an Agree message before sending the Inform message.
    """

    def __init__(self, agent: Agent):
        """
        Initialize the behavior.

        It will create an HTTP connection to the FIPA website.
        """
        super().__init__(agent)

        self.connection: HTTPConnection = HTTPConnection("fipa.org")
        self.lock = asyncio.Lock()

    def check_message(self, msg: ACLMessage) -> bool:
        """
        Check if the given message is valid, i.e. the agent understands the content.

        If not, then replies with a NOT_UNDERSTOOD message with a reason.

        :param msg: message to check
        :return: `True` if the message is valid, `False` otherwise.
        """
        if not isinstance(msg.content, str):
            self.agent.send(
                not_understood_message_from_request(
                    msg, "Content is expected to be an str value."
                )
            )
            return False
        return True

    async def on_valid_request(self, msg: ACLMessage) -> None:
        """
        Behavior executed once we are sure the received message is valid.

        First it sends an AGREE message and then it uses an internal :class:`HTTPConnection` to request the
        the full page at the given path.

        :param msg: the valid message
        """
        self.agent.send(agree_message_from_request(msg))
        async with self.lock:
            response = self._retrieve_page(msg.content)
            self.agent.send(inform_message_from_request(msg, response.read(200)))
            response.read()  # Read all so we can re-use the connection for the next time. May take time.

    def _retrieve_page(self, url: str) -> HTTPResponse:
        """
        Given a relative path, use the internal connection to the FIPA website to issue a GET request and return the received response.

        :param url: page path, starting with '/'.
        """
        self.connection.request("GET", url)
        return self.connection.getresponse()


class RegisterFIPAWebPageServiceBehavior(Behavior):
    """
    A one-shot behavior which registers our :class:`FIPAWebPageService` to the DF agent.
    """

    async def action(self) -> None:
        register_msg = (
            ACLMessage.Builder()
            .performative(Performative.REQUEST)
            .conversation_id("fipa-web-page-service")
            .receiver(AID(f"DF@{self.agent.aid.hap_name}"))
            .content(
                [
                    DFService.REGISTER_FUNC,
                    DFAgentDescription(
                        self.agent.aid,
                        services=(
                            ServiceDescription(
                                "Fipa web page service",
                                protocols=("fipa-request",),
                            ),
                        ),
                        protocols={"fipa-request"},
                    ),
                ]
            )
            .build()
        )

        self.agent.send(register_msg)


class TestingAgent(Agent):
    """
    A testing agent requesting the FIPA00023 specification.
    """

    def __init__(self, aid: AID, platform: AgentPlatformFacade):
        super().__init__(aid, platform)

        self.add_behavior(AskFIPA00023Behavior(self))


class AskFIPA00023Behavior(Behavior):
    """
    Request the FIPA00023 specification page to the first FIPA web service found.

    It uses the DF agent to search an agent providing the service and if such agent exists, it then sends a
    request to retrieve the page.
    """

    PAGE = "/specs/fipa00023/SC00023K.html"
    FIND_CONV = "find-fipa-web-page-service"
    ASK_CONV = "ask-page-fipa00023"

    def __init__(self, agent: Agent):
        super().__init__(agent)
        self.is_done = False

    def done(self) -> bool:
        return self.is_done

    async def action(self) -> None:
        # Find FIPAWebPageService
        find = (
            ACLMessage.Builder()
            .performative(Performative.REQUEST)
            .conversation_id(self.FIND_CONV)
            .receiver(AID(f"DF@{self.agent.aid.hap_name}"))
            .content(
                [
                    DFService.SEARCH_FUNC,
                    DFAgentDescription(
                        services=(
                            ServiceDescription(
                                "Fipa web page service",
                                protocols=("fipa-request",),
                            ),
                        ),
                    ),
                ]
            )
            .build()
        )
        self.agent.send(find)

        # Wait until we get the response
        _ = await self.agent.receive(MT_CONVERSATION_ID(self.FIND_CONV))
        response = await self.agent.receive(MT_CONVERSATION_ID(self.FIND_CONV))

        # Extract service aid
        # According to DF spect, content is a tuple (request content, reponse)
        # The response is a list of matching agents, we take the first one
        if len(response.acl_message.content[1]) == 0:
            self.agent.logger.info("Service not available yet.")
            return
        service_aid = response.acl_message.content[1][0].name
        self.is_done = True

        # Contact service and ask page
        ask = (
            ACLMessage.Builder()
            .performative(Performative.REQUEST)
            .conversation_id(self.ASK_CONV)
            .receiver(service_aid)
            .content(self.PAGE)
            .build()
        )
        self.agent.send(ask)

        # Wait until we get the response
        _ = await self.agent.receive(MT_CONVERSATION_ID(self.ASK_CONV))
        response = await self.agent.receive(MT_CONVERSATION_ID(self.ASK_CONV))

        # Display the first 200 chars
        self.agent.logger.info(
            f"[{self.agent.aid.short_name}]: {response.acl_message.content}"
        )


if __name__ == "__main__":
    import logging
    import piaf.launcher as pl

    # Configure logging level and handler to see things
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())

    # Create the platform launcher
    launcher = pl.PlatformLauncher("localhost")

    # Add both DF FIPA services
    launcher.add_service(pl.ServiceDescription("DF", DFService))
    launcher.add_service(pl.ServiceDescription("FIPAService", FIPAWebPageService))

    # Add testing agents
    for i in range(10):
        launcher.add_agent(pl.AgentDescription(f"testing-{i}", TestingAgent))

    # The program will run until you hit Ctrl+C
    launcher.run()
