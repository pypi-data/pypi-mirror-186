"""
Part of the "two-platforms" test.

This module contains everything to setup and run the second platform. Once invoked, it will
create a platform named "ptf2" and one agent, called "other".

The agent waits until a message is received, print it using its logger and die.

.. note: In order to run this example, you will have to setup an AMQP server. Using Docker and RabbitMQ,
    you can easily launch the example: `docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management-alpine`

Once the server is ready, just run `python ptf2.py` in one terminal and `python ptf1.py` in another. If the example
works, you should see in the ptf2 terminal the message sent by the ptf1 agent.
"""
from piaf.agent import Agent
from piaf.behavior import Behavior, FSMBehavior, SuicideBehavior
from piaf.comm import AID
from piaf.ptf import AgentPlatformFacade


class RcvMsgBehavior(Behavior):
    """A simple behavior that receives messages and print them using the agent's logger."""

    async def action(self):
        """Receive a message and display it."""
        msg = await self.agent.receive()
        self.agent.logger.info(
            "[%s] Received %s", self.agent.aid.short_name, msg.acl_message.content
        )


class OtherAgent(Agent):
    """A simple agent that waits a message, print it and then die."""

    def __init__(self, aid: AID, platform: AgentPlatformFacade):
        """
        Initialize a new instance of the agent.

        :param aid: the agent's AID
        :param platform: where the agent will run.
        """
        super().__init__(aid, platform)

        fsm = FSMBehavior(self)
        self.add_behavior(fsm)

        fsm.add_state("RCV", RcvMsgBehavior)
        fsm.add_state("DEATH", SuicideBehavior, final=True)
        fsm.set_initial_state("RCV")

        fsm.add_transition("RCV", "DEATH", lambda e: True)


if __name__ == "__main__":
    import logging
    from piaf.launcher import AgentDescription, PlatformLauncher
    from piaf.comm.mtp.amqp import AMQPMessageTransportProtocol

    # Configure logging level and handler to see things
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())

    # Create platform launcher
    launcher = PlatformLauncher("ptf2")

    # Since we want to connect this platform to another one, we need an MTP.
    # Here we are going to use the AMQPMessageTransferProtocol, which relies on AMQP 0.9.1 protocol.
    launcher.add_mtp(AMQPMessageTransportProtocol("amqp://guest:guest@localhost/"))

    # Now we can add our agent
    launcher.add_agent(AgentDescription("other", OtherAgent))

    # The program will run until you hit Ctrl+C
    launcher.run()
