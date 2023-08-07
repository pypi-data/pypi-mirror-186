# coding: utf-8
"""Define all exceptions that are used in the piaf framework."""
from __future__ import annotations
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    import piaf.agent  # noqa
    import piaf.ptf as plt  # noqa

__all__ = [
    "InvalidStateException",
    "StateTransitionException",
    "UnsupportedOperationException",
    "MessageNotSentException",
    "MandatoryFieldValueException",
    "DuplicatedNameException",
    "DuplicatedSchemeException",
    "IllegalArgumentException",
]


class InvalidStateException(Exception):
    """
    Exception raised when an operation cannot be performed because of an invalid state.

    The exception message contains the state and the operation that was attempted.
    """

    def __init__(
        self,
        state: piaf.agent.AgentState | plt.PlatformState,
        operation: str = "",
    ):
        """
        Create a new :class:`InvalidStateException`.

        :param state: object's state when the exception occurred.
        :param operation: the operation that was attempted when the exception occurred.
        """
        super().__init__(f"Cannot perform operation {operation} when state is {state}.")


class StateTransitionException(Exception):
    """
    Exception raised when the object can't transition from a state to another.

    The exception's message contains the original state and the state that was targeted.
    """

    def __init__(
        self,
        from_: piaf.agent.AgentState | plt.PlatformState,
        to: piaf.agent.AgentState | plt.PlatformState,
    ):
        """
        Create a new :class:`StateTransitionException`.

        :param from_: the object's state
        :param to_: the state that can't be reached
        """
        super().__init__(f"Cannot transition from state {from_} to state {to}.")


class UnsupportedOperationException(Exception):
    """
    Exception raised when the requested operation is not supported.

    The message can provide extra information about the reasons.
    """

    def __init__(self, msg: str = ""):
        """
        Create a new :class:`UnsupportedOperationException`.

        :param msg: why this operation is not supported (optional)
        """
        super().__init__(msg)


class MessageNotSentException(Exception):
    """Raised when something went wrong and a message sending failed."""

    def __init__(self) -> None:
        """Create a new :class:`MessageNotSentException`."""
        super().__init__(
            "Your message couldn't be sent, see MTS logs for more information."
        )


class MandatoryFieldValueException(Exception):
    """Raised when a mandatory field as no value."""

    def __init__(self, field_name) -> None:
        """Create a new :class:`MandatoryFieldValueException`."""
        super().__init__(f"Mandatory field '{field_name}' has no value.'")


class DuplicatedNameException(Exception):
    """Raised when some action doesn't support name duplication."""

    def __init__(self, name: str) -> None:
        """
        Create a new :class:`DuplicatedNameException`.

        :param name: duplicated name
        """
        super().__init__(f"Duplicated name: {name}")


class DuplicatedSchemeException(Exception):
    """Raised when you try to register a MTP into an ACC for a scheme that as already a registered MTP."""

    def __init__(self, scheme: str) -> None:
        """
        Create a new :class:`DuplicatedSchemeException`.

        :param scheme: duplicated scheme
        """
        super().__init__(f"Duplicated scheme: {scheme}")


class IllegalArgumentException(Exception):
    """Raised when an argument doesn't respect a precondition."""

    def __init__(self, message: str) -> None:
        """
        Create a new :class:`IllegalArgumentException`.

        :param message: message to display. Mostlikely the violated precondition.
        """
        super().__init__(message)
