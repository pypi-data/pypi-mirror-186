# coding: utf-8
"""
A simple module that demonstrate how to create a simple agent and a simple behavior.

This module defines:

 * An agent, called CustomAgent
 * One behavior, called HelloWorldBehavior
 * It also show how to launch the platform.
"""
import piaf.agent as agent

from piaf.behavior import Behavior


class HelloWorldBehavior(Behavior):
    """A behavior that uses the agent's logger to display an Hello World message."""

    async def action(self):
        """Body of the Behavior."""
        self.agent.logger.info("Hello world from HelloWorldBehavior !")


class CustomAgent(agent.Agent):
    """A simple agent using the the :class:`HelloWorldBehavior`."""

    def __init__(self, aid, platform):
        """Create a new agent and add the behavior."""
        super().__init__(aid, platform)

        # Create an instance of HelloWorldBehavior and add it to the agent
        b = HelloWorldBehavior(self)
        self.add_behavior(b)


if __name__ == "__main__":
    import logging
    from piaf.launcher import PlatformLauncher, AgentDescription

    # Configure logging level and handler to see things
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())

    # Create the platform launcher
    launcher = PlatformLauncher("localhost")

    # Now we can add our agent
    launcher.add_agent(AgentDescription("hello", CustomAgent))

    # The program will run until you hit Ctrl+C
    launcher.run()
