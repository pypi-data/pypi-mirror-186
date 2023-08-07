"""
Part of the "two-platforms" test.

This module contains everything to setup and run the first platform. Once invoked, it will
create a platform named "ptf1" and one agent, called "my-agent".

The agent will try to send a message to an agent on the second platform. To do so, it will
first contact the ptf2 AMS periodically until the AMS tells the agent is up and running. Then
it can send the message!

.. note: In order to run this example, you will have to setup an AMQP server. Using Docker and RabbitMQ,
    you can easily launch the example: `docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management-alpine`

Once the server is ready, just run `python ptf2.py` in one terminal and then `python ptf1.py` in another. If the example
works, you should see in the ptf2 terminal the message sent by the ptf1 agent.
"""
from __future__ import annotations
import asyncio
from typing import Any

from piaf.agent import Agent, AgentState
from piaf.ptf import AgentPlatformFacade
from piaf.service import AMSService, AMSAgentDescription
from piaf.behavior import Behavior, FSMBehavior, SuicideBehavior
from piaf.comm import (
    AID,
    MT_AND,
    MT_CONVERSATION_ID,
    MT_OR,
    MT_PERFORMATIVE,
    ACLMessage,
    Message,
    Performative,
)


class SendMsgBehavior(Behavior):
    """A simple behavior that sends messages."""

    def __init__(self, agent: Agent, msg: Message) -> None:
        """
        Create a new :class:`SendMsgBehavior`.

        :param agent: the agent running this behavior
        :param msg: the message to send
        """
        super().__init__(agent)
        self.msg = msg

    async def action(self):
        """Send the message."""
        self.agent.send(self.msg)


class FindOtherAgent(Behavior):
    """
    A simple behavior which runs until the other agent (the one living on the other
    platform) is available.
    """

    def __init__(self, agent: Agent, ams: AID) -> None:
        """
        Initialize the behavior.

        It expects the agent (like any behavior) and the AID of the other agent.
        :param agent: the agent
        :param aid: other agent's AID
        """
        super().__init__(agent)
        self.ams: AID = ams
        self.found = True

    async def action(self) -> None:
        # Contact other platform to ask if the other agent is ready
        self.agent.logger.info("Sending lookup request.")
        conv = "find_agent"
        req = (
            ACLMessage.Builder()
            .performative(Performative.REQUEST)
            .receiver(self.ams)
            .conversation_id(conv)
            .content(
                [
                    AMSService.SEARCH_FUNC,
                    AMSAgentDescription(
                        name=AID(f"other@{self.ams.hap_name}"), state=AgentState.ACTIVE
                    ),
                ]
            )
            .build()
        )
        self.agent.send(req)

        # Read response
        reply = await self.agent.receive(
            MT_AND(
                MT_CONVERSATION_ID(conv),
                MT_OR(
                    MT_PERFORMATIVE(Performative.AGREE),
                    MT_PERFORMATIVE(Performative.REFUSE),
                    MT_PERFORMATIVE(Performative.FAILURE),
                ),
            )
        )
        if reply.acl_message.performative != Performative.AGREE:
            self.logger.error("AMS refused my request :(")
            self.found = False
            await asyncio.sleep(1)
            return

        self.agent.logger.info("AMS replied with AGREE")
        resp = await self.agent.receive(MT_CONVERSATION_ID(conv))

        # If not found, then sleep a bit and set found to false
        if len(resp.acl_message.content[1]) == 0:
            self.agent.logger.info("Other agent is not ready, sleep a bit ...")
            await asyncio.sleep(1)
            self.found = False
            return

    def result(self) -> Any:
        """
        Return if the AMS replied with the other agent's AID.

        :return: `True` if the other agent is up and ready
        """
        return self.found


class MyAgent(Agent):
    """
    The agent that will query the remote platform.

    Internally, it uses an FSMBehavior to execute the :class:`FindOtherAgent`,
    :class:`SendMsgBehavior` and `TerminateAgentBehavior` in the right order.
    """

    def __init__(self, aid: AID, platform: AgentPlatformFacade, other: AID):
        """
        Initialize a new instance of the agent.

        :param aid: agent's aid
        :param platform: the platform on which the agent will run
        :param other: the other agent's AID
        """
        super().__init__(aid, platform)

        msg = (
            ACLMessage.Builder()
            .performative(Performative.INFORM)
            .receiver(other)
            .content("Hello from PTF1!")
            .build()
        )

        fsm = FSMBehavior(self)
        self.add_behavior(fsm)

        fsm.add_state(
            "FIND", FindOtherAgent, args=[AID(f"ams@ptf2", ["amqp://ptf2/acc"])]
        )
        fsm.add_state("SEND", SendMsgBehavior, args=[msg])
        fsm.add_state("DEATH", SuicideBehavior, final=True)
        fsm.set_initial_state("FIND")

        fsm.add_transition("FIND", "FIND", lambda found: not found)
        fsm.add_transition("FIND", "SEND", lambda found: found)
        fsm.add_transition("SEND", "DEATH", lambda e: True)


if __name__ == "__main__":
    import logging
    from piaf.launcher import AgentDescription, PlatformLauncher
    from piaf.comm.mtp.amqp import AMQPMessageTransportProtocol

    # Configure logging level and handler to see things
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())

    # Create the platform launcher
    launcher = PlatformLauncher("ptf1")

    # Register MTP. Since we want to connect this platform to another one, we need an MTP.
    # Here we are going to use the AMQPMessageTransferProtocol, which relies on AMQP 0.9.1 protocol.
    launcher.add_mtp(AMQPMessageTransportProtocol("amqp://guest:guest@localhost/"))

    # Now we can add our agent. The other agent AID is hardcode but we could use
    # the DF agent in a real case scenario to retrieve it.
    launcher.add_agent(
        AgentDescription(
            "my-agent",
            MyAgent,
            kwargs={"other": AID("other@ptf2", ["amqp://ptf2/acc"])},
        )
    )

    # The program will run until you hit Ctrl+C
    launcher.run()
