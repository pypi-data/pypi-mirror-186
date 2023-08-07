# coding: utf-8
from __future__ import annotations

import asyncio
import platform
import sys
from dataclasses import dataclass, field
from typing import Any, Collection, Dict, List, Mapping, Type

import semver

from piaf.comm.mts import MessageTransportProtocol
from piaf.exceptions import InvalidStateException
from piaf.ptf import AgentPlatform, Extension, PlatformState


@dataclass(eq=True, frozen=True)
class ServiceDescription:
    """Description of a service to be launched by a :class:`PlatformLauncher` instance."""

    #: The :class:`AID` short name
    name: str

    #: The class
    clazz: Type

    #: A collection of arguments to be passed to the constructors
    args: Collection[Any] = field(default_factory=list)

    #: Same as  `args` but for keyword arguments
    kwargs: Mapping[str, Any] = field(default_factory=dict)


AgentDescription = ServiceDescription
AgentDescription.__doc__ = """Description of an agent to be launched by a :class:`PlatformLauncher` instance."""


class PlatformLauncher:
    """
    A simpler API to create, set up, launch and teardown a platform.

    Once the :class:`PlatformLauncher` instance is created, you can add agents, services and MTPs. Once ready, just
    call the :meth:`run` method. It will launch the platform and wait for you to hit Ctrl + C.
    """

    def __init__(self, ptf_name: str) -> None:
        """
        Create a new :class:`PlatformLauncher` instance.

        Initially, there is no agents, services or MTPs registered and the platform is created but not launched.

        :param ptf_name: name of the platform
        """
        self.ptf = AgentPlatform(ptf_name)
        self._agents: List[AgentDescription] = []
        self._services: List[ServiceDescription] = []
        self._mtps: List[MessageTransportProtocol] = []
        self._extensions: Dict[str, Extension] = {}

    def add_agent(self, agent_description: AgentDescription) -> None:
        """
        Add the given agent to the platform.

        :param agent_description: description of the agent to add
        :raise InvalidStateException: the platform is already launched
        """
        if self.ptf.state != PlatformState.INITIALIZED:
            raise InvalidStateException(self.ptf.state, "add_agent")
        self._agents.append(agent_description)

    def add_service(self, service_description: ServiceDescription) -> None:
        """
        Add the given service to the platform.

        :param service_description: description of the service to add
        :raise InvalidStateException: the platform is already launched
        """
        if self.ptf.state != PlatformState.INITIALIZED:
            raise InvalidStateException(self.ptf.state, "add_service")
        self._services.append(service_description)

    def add_mtp(self, mtp: MessageTransportProtocol) -> None:
        """
        Add the given MTP to the platform.

        :param mtp: the instantiated MTP
        :raise InvalidStateException: the platform is already launched
        """
        if self.ptf.state != PlatformState.INITIALIZED:
            raise InvalidStateException(self.ptf.state, "add_mtp")
        self._mtps.append(mtp)

    def add_extension(self, name: str, ext: Extension) -> None:
        """
        Add the given extension to the platform.

        :param name: name given for indexing
        :param extension: the extension to add
        :raise InvalidStateException: the platform is already launched
        """
        if self.ptf.state != PlatformState.INITIALIZED:
            raise InvalidStateException(self.ptf.state, "add_extension")
        self._extensions[name] = ext

    def run(self) -> None:
        """
        Configure and run the wrapped :class:`AgentPlatform`.

        This method takes care of getting the event loop and tearing down things. Control is given back with CTRL+C.
        """
        # Before Python 3.10.6, there is a bug in the ProactorEventLoop.
        # See https://github.com/nedbat/dinghy/issues/9 and https://github.com/python/cpython/issues/83413
        if semver.match(platform.python_version(), ">=3.8.0") and semver.match(
            platform.python_version(), "<3.10.6"
        ):

            def unraisablehook(unraisable, _old_hook=sys.unraisablehook):
                if (
                    unraisable.exc_value.args[0] == "Event loop is closed"
                    and unraisable.object.__name__ == "__del__"
                ):
                    return
                return _old_hook(unraisable)

            sys.unraisablehook = unraisablehook

        # Configure the loop and launch the platform
        loop = asyncio.get_event_loop()
        try:
            loop.create_task(self._main())
            loop.run_until_complete(self._wait_platform_death())
        except KeyboardInterrupt:
            pass
        finally:
            loop.run_until_complete(self._cleanup())
            tasks = asyncio.all_tasks(loop)
            if tasks:
                loop.run_until_complete(
                    asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
                )
            loop.run_until_complete(loop.shutdown_asyncgens())
            loop.close()

    async def _cleanup(self) -> None:
        # Stop the platform if not done already
        if self.ptf.state != PlatformState.STOPPED:
            await self.ptf.stop()

        # Close the event manager since the platform doesn't manage its lifecycle
        await self.ptf.evt_manager.close()

    async def _main(self) -> None:
        """Coroutine that starts the platform and setup mtps, services and agents."""
        # Extensions are loaded first, before the platform is started since agents could rely on exposed primitives.
        for name, ext in self._extensions.items():
            self.ptf.load_extension(name, ext)

        # Before adding anything, we need to start the platform. This ensure that the
        # AMS agent is created
        await self.ptf.start()

        # Then register all provided MTP instances
        asyncio.gather(*(self.ptf.acc.register_mtp(mtp) for mtp in self._mtps))

        # Then services
        asyncio.gather(*(self._launch_agent(service, True) for service in self._services))

        # Then agents
        asyncio.gather(*(self._launch_agent(agent, False) for agent in self._agents))

    async def _wait_platform_death(self) -> None:
        """Wait until the platform is stopped."""
        async with self.ptf.state_sync:
            await self.ptf.state_sync.wait_for(
                lambda: self.ptf.state == PlatformState.STOPPED
            )
    
    async def _launch_agent(self, description: AgentDescription | ServiceDescription, is_service: bool) -> None:
        aid = await self.ptf.agent_manager.create(
            description.clazz, description.name, is_service, *description.args, **description.kwargs
        )
        await self.ptf.agent_manager.invoke(aid)
