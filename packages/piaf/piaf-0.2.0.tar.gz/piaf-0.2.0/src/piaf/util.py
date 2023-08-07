# coding: utf-8
"""Utility module."""
# TODO: complete description
from __future__ import annotations
import asyncio
from abc import ABCMeta, abstractmethod
from piaf.behavior import Behavior
from piaf.comm import ACLMessage, MT_OR, MT_PERFORMATIVE, Performative
from typing import Any, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    import piaf.agent


def not_understood_message_from_request(request: ACLMessage, reason: str) -> ACLMessage:
    """
    Build a `NOT_UNDERSTOOD` message from the provided request.

    It will extract the sender and the conversation id of the request. The returned message has performative
    `NOT_UNDERSTOOD` and its content is a list containing two elements:
      - the original request
      - the reason why the request is understood

    :param request: the request message to reply to.
    :param reason: a text message explaining why we reply with `NOT_UNDERSTOOD`
    :return: the built message
    """
    return (
        ACLMessage.Builder()
        .performative(Performative.NOT_UNDERSTOOD)
        .receiver(request.sender)
        .conversation_id(request.conversation_id)
        .content([request, reason])
        .build()
    )


def refuse_message_from_request(request: ACLMessage, reason: str) -> ACLMessage:
    """
    Build a `REFUSE` message from the provided request.

    It will extract the sender and the conversation id of the request. The returned message has performative
    `REFUSE` and its content is a list containing two elements:
      - the original request
      - the reason why the request is refused

    :param request: the request message to reply to.
    :param reason: a text message explaining why we reply with `REFUSE`
    :return: the built message
    """
    return (
        ACLMessage.Builder()
        .performative(Performative.REFUSE)
        .receiver(request.sender)
        .conversation_id(request.conversation_id)
        .content([request.content, reason])
        .build()
    )


def agree_message_from_request(request: ACLMessage) -> ACLMessage:
    """
    Build an `AGREE` message from the provided request.

    It will extract the sender and the conversation id of the request. The returned message has performative
    `AGREE` and its content is set to the content of the request.

    :param request: the request message to reply to.
    :return: the built message
    """
    return (
        ACLMessage.Builder()
        .performative(Performative.AGREE)
        .receiver(request.sender)
        .conversation_id(request.conversation_id)
        .content(request.content)
        .build()
    )


def failure_message_from_request(request: ACLMessage, reason: str) -> ACLMessage:
    """
    Build a `FAILURE` message from the provided request.

    It will extract the sender and the conversation id of the request. The returned message has performative
    `FAILURE` and its content is a list with two items: the first one is set to the content of the request and
    the second one to the provided failure reason.

    :param request: the request message to reply to.
    :param reason: the reason why the operation failed
    :return: the built message
    """
    return (
        ACLMessage.Builder()
        .performative(Performative.FAILURE)
        .receiver(request.sender)
        .conversation_id(request.conversation_id)
        .content([request.content, reason])
        .build()
    )


def inform_message_from_request(request: ACLMessage, content: Any) -> ACLMessage:
    """
    Build an `INFORM` message from the provided request.

    It will extract the sender and the conversation id of the request. The returned message has performative
    `INFORM` and its content is set to the provided one.

    :param request: the request message to reply to.
    :param content: the content of the `INFORM` message
    :return: the built message
    """
    return (
        ACLMessage.Builder()
        .performative(Performative.INFORM)
        .receiver(request.sender)
        .conversation_id(request.conversation_id)
        .content(content)
        .build()
    )


class FIPARequestProtocolBehavior(Behavior, metaclass=ABCMeta):
    """Behavior designed to handle the FIPA request protocol."""

    def __init__(self, agent: piaf.agent.Agent, *args, **kwargs):
        """
        Initialize the :var:`tasks` attribute which stores all running tasks.

        :param agent: the agent that owns the behavior
        """
        super().__init__(agent, *args, **kwargs)
        self.tasks: Dict[str, asyncio.Future] = {}

    def done(self) -> bool:
        """Infinite behavior."""
        return False

    @property
    def msg_template(self) -> piaf.comm.MessageTemplate:
        """
        Template message used to retrieve messages related to the request protocol.

        By default, any message using the :cvar:`Performative.REQUEST` or the :cvar:`Performative.CANCEL` performative
        will match.

        :return: the message template to use
        """
        return MT_OR(
            MT_PERFORMATIVE(Performative.REQUEST), MT_PERFORMATIVE(Performative.CANCEL)
        )

    def check_message(self, msg: ACLMessage) -> bool:
        """
        Check if the given request message is valid.

        Users can override this method to provide their own checks or even send replies. By default it always returns
        `True`.

        :param msg: message to check
        :return: Must return `True` if the message is valid, `False` otherwise.
        """
        return True

    @abstractmethod
    async def on_valid_request(self, msg: ACLMessage) -> None:
        """
        Coroutine called when the request message is valid and can be handled.

        The user should redefine this method. The coroutine will be cancelled if the agent receives a cancel message
        with the same conversation id than the request.

        :param msg: the request ot handle
        :return: coroutine to asynchronously handle it
        """
        raise NotImplementedError()

    async def action(self) -> None:
        """
        Behavior blocks until a valid message (ie validate template :var:`msg_template`) is found.

        Once a message matches, we probe the act and the content to decide what to do.
        """
        # Get next handled message
        msg = await self.agent.receive(self.msg_template)
        acl_msg = msg.acl_message

        # Request -> new conversation
        if acl_msg.performative == Performative.REQUEST:

            # If message content is invalid, stop processing
            if not self.check_message(acl_msg):
                return

            # Otherwise execute the user method
            self.tasks[acl_msg.conversation_id] = asyncio.create_task(
                self.on_valid_request(acl_msg)
            )

        # Cancel -> check if existing conversation
        elif acl_msg.performative == Performative.CANCEL:
            try:
                self.tasks[acl_msg.conversation_id].cancel()
                del self.tasks[acl_msg.conversation_id]
                self.agent.send(inform_message_from_request(acl_msg, acl_msg))
            except KeyError:
                self.agent.send(
                    not_understood_message_from_request(
                        acl_msg, f"Unexpected Act: {acl_msg.performative}"
                    )
                )
