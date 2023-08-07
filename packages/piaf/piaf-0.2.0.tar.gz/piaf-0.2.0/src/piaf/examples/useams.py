# coding: utf-8
"""
A small program testing the AMS capabilities.

The scenario is the following:

1. Ten receiving agents and one broadcaster are created
2. The broadcaster one perform a request to find active agents
3. It sends a `Hello World` message to inform agents of its presence
4. The receiving agents display the message

It is possible that not all agents receives the message, since the broadcaster dies just after having sent its message
to at least one active agent. So, if some receivers where not ready at the time the broadcaster queried the AMS, those
agents won't receive the message.
"""
from __future__ import annotations
import asyncio
from typing import TYPE_CHECKING, List

from piaf.agent import Agent, AgentState
from piaf.service import AMSService, AMSAgentDescription
from piaf.comm import (
    MT_CONVERSATION_ID,
    ACLMessage,
    Message,
    MessageTemplate,
    Performative,
    AID,
)
from piaf.behavior import Behavior

if TYPE_CHECKING:
    from piaf.ptf import AgentPlatform, AgentPlatformFacade


class SendHello(Behavior):
    """
    One shot behavior to say hello to all active agents.

    Use the AMS to search active agents and send an `INFORM` message. The behavior is over when at least one agent is
    returned by the AMS.
    """

    def __init__(self, agent: Agent):
        super().__init__(agent)
        self.is_done = False

    def done(self) -> bool:
        return self.is_done

    async def action(self) -> None:
        """
        Behavior `action` method.

        1. Contact AMS and ask all active agents
        2. If AMS respond with INFORM
            1. Loop over received :class:`AMSAgentDescription` objects
            2. If neither owner nor the AMS, send hello

        """
        # First, create a message to query the AMS
        msg = (
            ACLMessage.Builder()
            .performative(Performative.REQUEST)
            .receiver(AID(f"ams@{self.agent.aid.hap_name}"))
            .conversation_id(f"{self.agent.aid.name}-sendhello")
            .content(
                [
                    AMSService.SEARCH_FUNC,
                    AMSAgentDescription(None, None, AgentState.ACTIVE),
                ]
            )
            .build()
        )
        self.agent.send(msg)

        # Wait a reply. First it should receive an AGREE, then an INFORM with the query response
        mt: MessageTemplate = MT_CONVERSATION_ID(msg.conversation_id)
        reply: Message = await self.agent.receive(mt)
        if reply.acl_message.performative != Performative.AGREE:
            return

        # If it succeeded, loop over content
        reply = await self.agent.receive(mt)
        if reply.acl_message.performative == Performative.INFORM:

            # Extract content
            content: List[AMSAgentDescription] = reply.acl_message.content[1]

            # No remaining agent, try again later
            if not content:
                asyncio.sleep(1)
                return

            # At least one active agent is a receiver
            for agt_description in content:
                other_aid = agt_description.name

                # If the description is neither agent nor the AMS, send hello !
                if other_aid != self.agent.aid and other_aid.short_name != "ams":
                    self.agent.send(
                        ACLMessage.Builder()
                        .performative(Performative.INFORM)
                        .receiver(other_aid)
                        .conversation_id(
                            f"{self.agent.aid.name}-sendhello-{other_aid.name}"
                        )
                        .content("Hello friend!")
                        .build()
                    )
                    self.is_done = True


class DisplayReceivedMessage(Behavior):
    """One shot behavior displaying the first received message."""

    async def action(self) -> None:
        """Use the agent's logger to display the first received message."""
        msg = await self.agent.receive()
        self.agent.logger.info(
            f"From {msg.acl_message.sender}: {msg.acl_message.content}"
        )


class BroadcastAgent(Agent):
    """
    Simple agent broadcasting a 'Hello' message to other active agents.

    The broadcast is performed when the agent is invoked. Agent dies immediately after.
    """

    def __init__(
        self,
        aid: AID,
        platform: AgentPlatformFacade | AgentPlatform,
    ):
        super().__init__(aid, platform)

        self.add_behavior(SendHello(self))


class DisplayAgent(Agent):
    """A simple agent displaying the first received message and dying right after that."""

    def __init__(self, aid: AID, platform: AgentPlatformFacade | AgentPlatform):
        super().__init__(aid, platform)

        self.add_behavior(DisplayReceivedMessage(self))


if __name__ == "__main__":
    import logging
    from piaf.launcher import AgentDescription, PlatformLauncher

    # Configure logging level and handler to see things
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())

    # Create the platform launcher
    launcher = PlatformLauncher("localhost")

    # Add agents
    for i in range(10):
        launcher.add_agent(AgentDescription(f"DA-{i}", DisplayAgent))
    launcher.add_agent(AgentDescription("BA", BroadcastAgent))

    # The program will run until you hit Ctrl+C
    launcher.run()
