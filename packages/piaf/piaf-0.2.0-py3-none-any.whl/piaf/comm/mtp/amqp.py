# coding: utf-8
"""This module enables communication between platforms using the AMQP 0.9.1 protocol."""
from __future__ import annotations

import asyncio
import logging
import pickle

try:
    import aiormq
    import aiormq.abc
    from aiormq import PublishError
    from yarl import URL
except ImportError as e:
    print("Install extra amqp-mtp to use amqp message transfer protocol.")
    raise e

from piaf.comm import Message
from piaf.comm.mts import MessageContext, MessageTransportProtocol


class AMQPMessageTransportProtocol(MessageTransportProtocol):
    """
    A MTP implementation enabling communications using the AMQP 0.9.1 protocol.

    This MTP is built on asyncio and runs on the same thread as the platform. It first
    establishes a connection with an AMQP server and then:

        - use (and create if necessary) an exchange called "acc" in direct mode
        - bind an unnamed queue on it, using the platform name as routing key

    Messages are published on the "acc" exchange, using the destination platform name as routing key.
    """

    def __init__(self, amqp_server_url: str) -> None:
        """
        Initialize a new instance of :class:`AMQPMessageTransferProtocol`.

        :param amqp_server_url: URL to the AMQP server this connector will connect to.
        """
        super().__init__()
        self._server_url = amqp_server_url
        self._listening_condition = asyncio.Condition()
        self._listening_flag = False
        self.logger = logging.getLogger(type(self).__name__)

    @property
    def scheme(self) -> str:
        """
        Get the scheme of the protocol.

        :return: the scheme
        """
        return "amqp"

    @property
    def address(self) -> str:
        """
        Get the ACC address using the current protocol.

        :return: URL of the platform's ACC using the current protocol
        """
        return f"{self.scheme}://{self.acc.ptf_name}/acc"

    @property
    def type(self) -> str:
        """
        Get the type of this protocol (what to put in `protocol` fields).

        :return: the protocol type
        """
        return "piaf.mts.mtp.amqp.aio"

    async def send(self, message: Message, address: str) -> bool:
        """
        Send the provided message to the provided address (expected to be an amqp one).

        :param message: the message to send
        :param address: the amqp address of the other platform's ACC
        :return: `True` if the message is sent, `False` if the provided address is not an AMQP
            one or the MTP is unable to deliver the message to the remote platform.
        """
        parsed_url = URL(address)
        if parsed_url.scheme != self.scheme:
            return False

        rt_key = parsed_url.host
        if rt_key is None:
            return False

        # Make sure we are ready to receive responses
        if not self._listening_flag:
            async with self._listening_condition:
                await self._listening_condition.wait()

        try:
            await self.channel.basic_publish(
                body=pickle.dumps(message, protocol=4),
                exchange="acc",
                routing_key=rt_key,
                mandatory=True,
            )
        except PublishError as e:
            self.logger.warn("[AMQP] Unable to route message.", exc_info=e)
            return False

        self.logger.debug("[AMQP] Sent %s", message)
        return True

    async def start(self) -> None:
        """
        Start this MTP.

        It wil establish the connection to the AMQP server and create a long running task to
        listen to incoming messages.
        """
        await self._connect()
        self.listener = asyncio.create_task(self._listen())

    async def stop(self) -> None:
        """
        Stop this MTP.

        Cancel the listening task and close the connection with the AMQP server.
        """
        self.listener.cancel()
        await self.channel.close()
        await self.connection.close()

    async def _connect(self) -> None:
        """Establish the connection with the AMQP server and create a channel."""
        # Create channel
        self.connection = await aiormq.connect(URL(self._server_url))
        self.channel = await self.connection.channel()

    async def _listen(self) -> None:
        """A long running task that listens on incoming messages and transfer them to the ACC."""
        # Declare exchange & random queue
        await self.channel.exchange_declare(exchange="acc", exchange_type="direct")
        declare_ok = await self.channel.queue_declare(
            durable=False, exclusive=True, auto_delete=True
        )

        # Bind queue to this platform and start listening
        await self.channel.queue_bind(
            declare_ok.queue, "acc", routing_key=self.acc.ptf_name
        )

        # Set listening flag to true
        async with self._listening_condition:
            self._listening_flag = True
            self._listening_condition.notify_all()
        await self.channel.basic_consume(declare_ok.queue, self._on_message)

    async def _on_message(self, msg: aiormq.abc.DeliveredMessage) -> None:
        """
        Callback called when an incoming message is received.

        :param msg: the received message
        """
        self.logger.debug("[AMQP] Received %s", pickle.loads(msg.body))
        self.acc.forward(pickle.loads(msg.body), MessageContext("", self))
