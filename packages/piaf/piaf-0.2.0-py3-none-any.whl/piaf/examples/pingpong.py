# coding: utf-8
from piaf.agent import Agent
from piaf.comm import AID
from piaf.comm import ACLMessage, Performative
from piaf.behavior import Behavior, FSMBehavior


class SendMsgBehavior(Behavior):
    """A simple behavior that sends messages."""

    def __init__(self, agent, msg, *args, **kwargs):
        """
        Create a new :class:`SendMsgBehavior`.

        :param agent: the agent running this behavior
        :param msg: the message to send
        """
        super().__init__(agent, *args, **kwargs)
        self.msg = msg

    async def action(self):
        """Send the message and increase the agent send counter."""
        self.agent.send(self.msg)
        self.agent.send_count += 1

    def result(self):
        """Get the counter's value."""
        return self.agent.send_count


class RcvMsgBehavior(Behavior):
    """A simple behavior that receives messages."""

    async def action(self):
        """Receive a message, display it and increase the agent receive counter."""
        msg = await self.agent.receive()
        self.agent.rcv_count += 1
        self.agent.logger.info(
            "[%s] Received %s", self.agent.aid.short_name, msg.acl_message.content
        )

    def result(self):
        """Return the agent receive counter."""
        return self.agent.rcv_count


class TerminateAgentBehavior(Behavior):
    """A simple behavior that terminates the agent."""

    async def action(self):
        """Terminate the agent."""
        await self.agent.quit()


class PingAgent(Agent):
    """
    The Ping agent is an agent that sends "PING" messages.

    This agent uses a FSM::

        SEND ----> RECEIVE --- (rcv > 10) --> END
          ^                 |
          ---( rcv <= 10) ---

    """

    def __init__(self, aid, platform):
        super().__init__(aid, platform)
        self.send_count = 0
        self.rcv_count = 0

        pong = AID("Pong@localhost", ("memory://localhost/Pong",))
        msg = (
            ACLMessage.Builder()
            .receiver(pong)
            .content("PING")
            .performative(Performative.INFORM)
            .build()
        )

        bhv = FSMBehavior(self)
        bhv.add_state("SEND", SendMsgBehavior, args=(msg,), final=False)
        bhv.add_state("RCV", RcvMsgBehavior)
        bhv.add_state("END", TerminateAgentBehavior, final=True)

        # Careful: order matter
        bhv.add_transition("RCV", "END", lambda r: r >= 10)
        bhv.add_transition("SEND", "RCV", lambda r: True)
        bhv.add_transition("RCV", "SEND", lambda r: True)

        bhv.set_initial_state("SEND")
        self.add_behavior(bhv)


class PongAgent(Agent):
    """
    Same as Ping agent, but slightly different::

        RECEIVE ----> SEND --- (send > 10) --> END
          ^                 |
          ---( send <= 10) ---

    """

    def __init__(self, aid, platform):
        super().__init__(aid, platform)
        self.send_count = 0
        self.rcv_count = 0

        pong = AID("Ping@localhost", ("memory://localhost/Ping",))
        msg = (
            ACLMessage.Builder()
            .receiver(pong)
            .content("PONG")
            .performative(Performative.INFORM)
            .build()
        )

        bhv = FSMBehavior(self)
        bhv.add_state("SEND", SendMsgBehavior, args=(msg,), final=False)
        bhv.add_state("RCV", RcvMsgBehavior)
        bhv.add_state("END", TerminateAgentBehavior, final=True)

        # Careful: order matter
        bhv.add_transition("SEND", "END", lambda r: r >= 10)
        bhv.add_transition("SEND", "RCV", lambda r: True)
        bhv.add_transition("RCV", "SEND", lambda r: True)

        bhv.set_initial_state("RCV")
        self.add_behavior(bhv)


if __name__ == "__main__":
    import logging
    from piaf.launcher import AgentDescription, PlatformLauncher

    # Configure logging level and handler to see things
    logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())

    # Create platform launcher
    launcher = PlatformLauncher("localhost")

    # Now we can add our agents
    launcher.add_agent(AgentDescription("Ping", PingAgent))
    launcher.add_agent(AgentDescription("Pong", PongAgent))

    # The program will run until you hit Ctrl+C
    launcher.run()
