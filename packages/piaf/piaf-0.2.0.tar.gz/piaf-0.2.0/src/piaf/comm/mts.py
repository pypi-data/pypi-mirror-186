# coding: utf-8
"""
This module contains every related to the Message Transport System.

The MTS is separated in different components:

* :class:`MessageTransferHandler`, which are components designed to handle
  communication using a specific protocol
* :class:`PlayloadParser`, which are responsible to dump and load
  :class:`piaf.comm.ACLMessage` to/from concrete representations
* the :class:`AgentCommunicationChannel` component, which provides message forwarding capability

class:`MessageTransferHandler` and class:`PlayloadParser` are interfaces that allow
you to create your own components (and thus use your own transport protocol or playload
representation).
"""
from __future__ import annotations

import abc
import asyncio
import copy
import itertools
import logging
import urllib.parse
from asyncio.futures import Future
from datetime import datetime
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    Dict,
    Iterable,
    List,
    NamedTuple,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

import piaf.comm
import piaf.exceptions as ex
from piaf.comm import AID, ACLMessage, Envelope, Message, Performative, ReceivedObject
from piaf.audit import ACC_TOPIC, AGENTS_PARENT_TOPIC, Event, Topic

if TYPE_CHECKING:
    from piaf.ptf import AgentPlatform

from piaf.exceptions import DuplicatedNameException

__all__ = [
    "MessageTransportProtocol",
    "PlayloadParser",
    "AgentCommunicationChannel",
    "MailBox",
    "MessageContext",
]


class MailBox:
    """Agent's mailbox."""

    def __init__(self):
        """Create a new mailbox."""
        self._queue: List[Message] = []
        self._sync = asyncio.Condition()

    async def get(
        self, template: piaf.comm.MessageTemplate = piaf.comm.MT_ALL()
    ) -> piaf.comm.Message:
        """
        Retrieve the first matching message in the mail box.

        This method blocks until such message is inserted with the method :meth:`put`.
        Note that the message is removed from the queue so two successive calls to
        :meth:`get` (or :meth:`get_nowait`) will end up with two different messages.
        Template is applied on the :class:`ACLMessage`.
        """
        async with self._sync:
            msg = None
            while msg is None:
                msg = self._lookup_for_matching_message(template)
                if msg is None:
                    await self._sync.wait()
            return msg

    def _lookup_for_matching_message(
        self, template: piaf.comm.MessageTemplate = piaf.comm.MT_ALL()
    ) -> Union[None, piaf.comm.Message]:
        """
        Lookup the queue for a message matching the provided template.

        If no such message exists, this method will return ``None``. This method
        doesn't take the lock so callers must lock the call themselves.
        Template is applied on the :class:`ACLMessage`.
        """
        for i in range(len(self._queue)):
            if template.apply(self._queue[i].acl_message):
                return self._queue.pop(i)
        return None

    async def get_nowait(
        self, template: piaf.comm.MessageTemplate = piaf.comm.MT_ALL()
    ) -> Union[None, piaf.comm.Message]:
        """
        Retrieve the first matching message in the mail box.

        Unlike :meth:`get`, this method returns ``None`` if no matching message is
        found. Otherwise, the behavior is similar to :meth:`get`.
        """
        async with self._sync:
            return self._lookup_for_matching_message(template)

    async def put(self, item: piaf.comm.Message) -> None:
        """Put the provided message in this mailbox."""
        async with self._sync:
            self._queue.append(item)
            self._sync.notify_all()


class MailBoxDelegate:
    """
    Delegation to internal agent or service mailbox.

    Restrict access to agent/service mailbox. Only exposed method is :meth:`MailBox.put`.
    """

    def __init__(self, delegate: MailBox) -> None:
        """
        Create a new :class:`MailBoxDelegate` object.

        :param delegate: agent's mailbox
        """
        self._delegate: MailBox = delegate

    async def put(self, item: piaf.comm.Message) -> None:
        """Put the provided message in this mailbox."""
        await self._delegate.put(item)


class PlayloadParser(metaclass=abc.ABCMeta):
    """Abstract playload parser. Use concrete classes to load or dump playload."""

    _PARSERS: ClassVar[Dict[str, Type[PlayloadParser]]] = {}
    _COMPONENT_NAME: ClassVar[str] = ""

    def __init_subclass__(cls, cmp_name: str):
        super().__init_subclass__()
        PlayloadParser._PARSERS[cmp_name] = cls
        cls._COMPONENT_NAME = cmp_name

    @classmethod
    def get_parser(cls, cmp_name: str):
        return cls._PARSERS[cmp_name]

    @abc.abstractmethod
    def dump(self, data: Any, encoding: str = "utf-8") -> bytearray:
        """Dump the provided data into a :class:`bytearray`.

        :param data: the playload to dump
        :param encoding: how string are encoded
        :return: the playload dumped into the bytearray
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def load(self, data: bytearray, encoding: str = "utf-8") -> Any:
        """Load a playload from the provided bytearray.

        :param data: the bytearray
        :param encoding: how strings are encoded
        :return: a playload
        """
        raise NotImplementedError()


class AgentCommunicationChannel:
    """
    :class:`AgentCommunicationChannel` is an entity providing the messaging service to the AP agents.

    See http://fipa.org/specs/fipa00067/ for more information.
    """

    _ID = itertools.count(0)
    _id_lock = asyncio.Lock()

    @classmethod
    async def _next_id(cls):
        async with cls._id_lock:
            return next(cls._ID)

    def __init__(self, ptf: AgentPlatform) -> None:
        """Create a new ACC without any registered agent or service."""
        self._knows: Dict[str, MailBox] = {}
        self._tasks: List[Future] = []
        self._ptf: AgentPlatform = ptf
        self._mtps: Dict[str, MessageTransportProtocol] = {}
        self.logger = logging.getLogger(type(self).__name__)

    @property
    def schemes(self) -> Tuple[str, ...]:
        """Get the list of supported schemes."""
        return tuple(self._mtps)

    @property
    def ptf_name(self) -> str:
        """Get the platform name."""
        return self._ptf.name

    def register_agent_or_service(self, name: str, mailbox: MailBox) -> None:
        """
        Register an agent or a service to this ACC.

        If registration is successful, any message received by the ACC targeting the registered agent or service will
        be delivered to that agent or service using the provided mailbox.

        :raise DuplicatedNameException: an agent or a service with the provided name already exists.
        """
        if name in self._knows:
            raise DuplicatedNameException(name)

        self._knows[name] = mailbox

    def forget_agent_or_service(self, name: str) -> None:
        """
        Forget an agent or a service.

        The provided name will be forgotten and messages will no longer be delivered. No-op if the name is unknown.
        """
        if name in self._knows:
            del self._knows[name]

    async def register_mtp(self, mtp: MessageTransportProtocol) -> None:
        """
        Register a new MTP and start it.

        Once registered, the ACC will be able to use the MTP to send messages. ACC doesn't allow duplicated MTPs (ie,
        MTP providing the same scheme). If you try to register a MTP with an already registered scheme, this method
        will raise an exception.

        :raise DuplicatedSchemeException: if you try to register an MTP handling an already-register scheme.
        """
        if mtp.scheme in self._mtps:
            raise ex.DuplicatedSchemeException(mtp.scheme)

        self._mtps[mtp.scheme] = mtp
        mtp.acc = self
        await mtp.start()

        await self._ptf.evt_manager.publish(
            Event("acc", "mtp_registration", mtp.scheme), ACC_TOPIC
        )

    @property
    def addresses(self) -> Tuple[str, ...]:
        """Get all addresses this ACC can be contacted with."""
        return tuple(mtp.address for mtp in self._mtps.values())

    def forward(self, msg: Message, context: MessageContext = None):
        """
        Forward the provided message.

        Rules here.
        """
        task = asyncio.create_task(self._handle_message(msg, context))
        self._tasks.append(task)

    async def stop(self) -> None:
        """
        Stop the ACC.

        This will cancel all running tasks and stop all running MTPs.
        """
        for task in self._tasks:
            task.cancel()

        if self._tasks:
            for result in await asyncio.gather(*self._tasks, return_exceptions=True):
                if (
                    result is not None
                ):  # Exception occurred (result is None if success, see _handle_message)
                    self.logger.exception(
                        "[ACC] Message handling exception.", exc_info=result
                    )

        for mtp in self._mtps.values():
            await mtp.stop()

    async def _handle_message(
        self, msg: Message, context: MessageContext = None
    ) -> None:
        """
        Asynchronous task to take care of a message.

        :param msg: the message to handle
        :param context: optional context linked to the message
        """
        envelope = msg.envelope
        f_update: Dict[str, Any] = {
            Envelope.Builder.RECEIVED: await self._fill_received_field(context),
        }

        # Generate intended-receiver from the to field then re-run method
        if envelope.intended_receiver is None:
            f_update[Envelope.Builder.INTENDED_RECEIVER] = (
                envelope.to if isinstance(envelope.to, Iterable) else (envelope.to,)
            )
            envelope.add_revision(f_update)
            self.forward(msg, context)

        # Read intended-receiver field and dispatch
        else:
            local, others = self._retrieve_local_receivers(envelope.intended_receiver)

            if others:
                for aid in others:
                    f_update[Envelope.Builder.INTENDED_RECEIVER] = (aid,)
                    cpy: Message = copy.deepcopy(msg)
                    cpy.envelope.add_revision(f_update)
                    await self._send_via_mts(aid, cpy)

            if local:
                f_update[Envelope.Builder.INTENDED_RECEIVER] = local
                msg.envelope.add_revision(f_update)
                for aid in local:
                    cpy: Message = copy.deepcopy(msg)
                    cpy.envelope.add_revision(f_update)
                    await self._send_locally(aid, cpy)

    async def _fill_received_field(
        self, context: MessageContext = None
    ) -> ReceivedObject:
        """
        Generate new content for the 'received' field  with this ACC information.

        :param context: message context. Optional.
        """
        by = (
            f"memory://{self._ptf.name}/acc" if context is None else context.via.address
        )
        rcv_obj = ReceivedObject(
            by=by,
            date=datetime.now(),
            id=await AgentCommunicationChannel._next_id(),
        )

        if context is not None:
            rcv_obj.from_ = context.from_
            rcv_obj.via = context.via.type

        return rcv_obj

    async def _send_via_mts(self, aid: AID, msg: Message):
        """
        Send a message through available :class:`MessageTransportProtocol`.

        :param aid: AID of the receiver
        :param msg: Message to send
        """
        success = False
        for address in aid.addresses:
            scheme = self._retrieve_scheme_from_url(address)
            if scheme in self._mtps:
                success = await self._mtps[scheme].send(msg, address)

            if success:
                break

        # If still not successful, try name resolution
        # Not implemented yet
        if not success:
            pass

        # Nothing worked, send failure message
        if not success:
            await self._send_failure_message(msg)

    async def _send_locally(self, aid: AID, msg: Message) -> None:
        """
        Send a message to a local agent.

        :param aid: agent's AID
        :param msg: message to send
        """
        if aid.short_name in self._knows:
            await self._knows[aid.short_name].put(msg)

            # Fire msg reception event
            acl_msg: ACLMessage = copy.deepcopy(msg.acl_message)
            await self._ptf.evt_manager.publish(
                Event(aid.name, "message_reception", acl_msg),
                Topic.resolve_from_parent_topic(
                    AGENTS_PARENT_TOPIC, f"{aid.short_name}.messages"
                ),
            )
        else:
            await self._send_failure_message(msg)

    def _retrieve_scheme_from_url(self, url: str):
        """Retrieve scheme from provided URL."""
        return urllib.parse.urlparse(url).scheme

    def _retrieve_local_receivers(
        self, aids: Sequence[AID]
    ) -> Tuple[Iterable[AID], Iterable[AID]]:
        """
        Retrieve local receivers.

        Returns a tuple containing two sequences: the first one is an iterable of local AIDs, the second one contains
        external AIDs.

        :param aids: Iterable of AIDs containing potentially local AIDs
        """
        local = []
        others = []
        for aid in aids:
            if aid.hap_name == self._ptf.name:
                local.append(aid)
            else:
                others.append(aid)
        return local, others

    async def _send_failure_message(self, msg: Message) -> None:
        """
        Build and send a failure message from the provided message.

        Will extract:

        - conversation_id
        - reply_with
        - sender

        If those information are not provided, abort message sending and log error.
        """

        try:
            reply_msg = (
                ACLMessage.Builder()
                .performative(Performative.FAILURE)
                .receiver(msg.acl_message.sender)
                .conversation_id(msg.acl_message.conversation_id)
                .content([msg.acl_message.content, f"Unreachable agent: {msg.acl_message.receiver}"])
                .build()
            )
            reply_msg.in_reply_to = msg.acl_message.reply_with

            reply_envlp = (
                Envelope.Builder()
                .from_(AID(f"ams@{self._ptf.name}", addresses=self.addresses))
                .to((msg.acl_message.sender,))
                .acl_representation("fipa.acl.rep.string.std")
                .date(datetime.now())
                .build()
            )
            await self._handle_message(Message(reply_envlp, reply_msg))
        except Exception as e:
            self.logger.error(
                "Missing information for sending failure message", exc_info=e
            )


class MessageTransportProtocol(metaclass=abc.ABCMeta):
    """
    Message Transfer Protocol as defined in fipa.

    According to fipa, MTP is used to carry out the physical transfer of messages between two ACCs.
    This is a base interface for all MTPs.
    See http://fipa.org/specs/fipa00067/SC00067F.html
    """

    def __init__(self) -> None:
        """
        Default constructor which declares an attribute named `acc`.

        This attribute should be set by the :class:`AgentCommunicationChannel` at registration time.
        """
        self.acc: None | AgentCommunicationChannel = None

    @abc.abstractmethod
    async def send(self, message: Message, address: str) -> bool:
        """
        Send the provided message to the provided address.

        If the sending operation fails, the coroutine will return ``False``.
        :param message: the message to send.
        :param address: where to send the message
        """
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def scheme(self) -> str:
        """Get the protocol's scheme this MTP is providing."""
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def address(self) -> str:
        """Get the address of the ACC when using this MTP."""
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def type(self) -> str:
        """
        Get this MTP's type.

        For example: fipa.mts.mtp.http.std
        """
        raise NotImplementedError()

    @abc.abstractmethod
    async def start(self) -> None:
        """
        Start the MTP.

        It must not block the caller, so the MTP must be started on its own thread or as
        a new task.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    async def stop(self) -> None:
        """Stop the MTP."""
        raise NotImplementedError()


class MessageContext(NamedTuple):
    """Data class containing the context of a message: url of the sender and MTP used."""

    from_: str
    via: MessageTransportProtocol
