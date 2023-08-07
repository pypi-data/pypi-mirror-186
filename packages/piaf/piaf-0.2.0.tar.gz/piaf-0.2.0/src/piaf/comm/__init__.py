# coding: utf-8
"""
This module contains the building blocks of Agent Communication.

The first block is the agent identity, called :class:`AID`. It is unique to each agent.
Then comes :class:`ACLMessage` and templates.
"""
from __future__ import annotations
from dataclasses import dataclass
import datetime
import enum
import abc
import functools
import operator
import copy

from typing import (
    Dict,
    List,
    Optional,
    Sequence,
    MutableMapping,
    Union,
    Any,
    Type,
)

import piaf.exceptions

__all__ = [
    "AID",
    "Performative",
    "ACLMessage",
    "MessageTemplate",
    "MT_ALL",
    "MT_AND",
    "MT_OR",
    "MT_NOT",
    "MT_PERFORMATIVE",
    "MT_SENDER",
    "MT_CONVERSATION_ID",
    "MT_ENCODING",
    "MT_IN_REPLY_TO",
    "MT_LANGUAGE",
    "MT_ONTOLOGY",
    "MT_PROTOCOL",
    "MT_REPLY_TO",
    "MT_REPLY_WITH",
    "Envelope",
    "ReceivedObject",
    "Message",
]


class AID:
    """
    Represents the identification of an agent.

    This class has three fields:

    * ``name``, which is mandatory and has the following form: agent_name@hap_name
    * ``addresses``, which is a list of URLs to reach the agent. This field is optional
      and URL order is relevant as it defines priorities between URLs.
    * ``resolvers``, which is a list of AIDs of name resolvers agents. This field is
      optional and order is relevant as it defines priorities between AIDs.

    According to the the fipa standard, two AIDs are considered equivalent if their
    ``name`` parameters are the same. Full specification is available here:
    http://www.fipa.org/specs/fipa00023/.
    """

    def __init__(
        self, name: str, addresses: Sequence[str] = (), resolvers: Sequence[AID] = ()
    ):
        """
        Create a new AID object.

        The create object will be initialized with the provided values. The
        ``name`` parameter must following this format : agent@hap_name.

        :param name: the agent's name
        :param addresses: an ordered sequence of URLs.
        :param resolvers: an ordered sequence of AIDs.
        :raise ValueError: if the name parameter is not well formed
        """
        if name is None or "@" not in name:
            raise ValueError("fullname must be agent_name@hap_name")

        self._name: str = name
        self.addresses: Sequence[str] = list(addresses)
        self.resolvers: Sequence[AID] = list(resolvers)

    @property
    def short_name(self) -> str:
        """Short agent's name (ie the part before '@' in the name)."""
        return self._name.split("@")[0]

    @property
    def hap_name(self) -> str:
        """Host agent plateform name (ie the part after '@' in the name)."""
        return self._name.split("@")[1]

    @property
    def name(self) -> str:
        """Agent's name."""
        return self._name

    def __eq__(self, value: Any) -> bool:
        """Two AIDs are equal if and only if their name are the same."""
        return (
            value is not None
            and type(value) == type(self)
            and self._name == value._name
        )

    def __hash__(self):
        return hash(self.name)

    def __deepcopy__(self, memo):
        return AID(self.name, tuple(self.addresses), tuple(self.resolvers))

    def __repr__(self) -> str:
        return f"AID({self.name}, {self.addresses}, {self.resolvers})"


class Performative(enum.Enum):
    """
    Performatives available as defined in http://www.fipa.org/specs/fipa00037/.

    These performatives are intended to be used with :class:`ACLMessage`. Here is
    a small summary of what each performative means:

    **ACCEPT_PROPOSAL**
        The action of accepting a previously submitted proposal to perform an action.
    **AGREE**
        The action of agreeing to perform some action, possibly in the future.
    **CANCEL**
        The action of one agent informing another agent that the first agent no longer
        has the intention that the second agent perform some action.
    **CFP**
        The action of calling for proposals to perform a given action.
    **CONFIRM**
        The sender informs the receiver that a given proposition is true, where the
        receiver is known to be uncertain about the proposition.
    **DISCONFIRM**
        The sender informs the receiver that a given proposition is false, where the
        receiver is known to believe, or believe it likely that, the proposition is
        true.
    **FAILURE**
        The action of telling another agent that an action was attempted but the
        attempt failed.
    **INFORM**
        The sender informs the receiver that a given proposition is true.
    **INFORM_IF**
        A macro action for the agent of the action to inform the recipient whether or
        not a proposition is true.
    **INFORM_REF**
        A macro action for sender to inform the receiver the object which corresponds
        to a descriptor, for example, a name.
    **NOT_UNDERSTOOD**
        The sender of the act (for example, i) informs the receiver (for example, j)
        that it perceived that j performed some action, but that i did not understand
        what j just did. A particular common case is that i tells j that i did not
        understand the message that j has just sent to i.
    **PROPAGATE**
        The sender intends that the receiver treat the embedded message as sent
        directly to the receiver, and wants the receiver to identify the agents denoted
        by the given descriptor and send the received propagate message to them.
    **PROPOSE**
        The action of submitting a proposal to perform a certain action, given certain
        preconditions.
    **PROXY**
        The sender wants the receiver to select target agents denoted by a given
        description and to send an embedded message to them.
    **QUERY_IF**
        The action of asking another agent whether or not a given proposition is true.
    **QUERY_REF**
        The action of asking another agent for the object referred to by a referential
        expression.
    **REFUSE**
        The action of refusing to perform a given action, and explaining the reason for
        the refusal.
    **REJECT_PROPOSAL**
        The action of rejecting a proposal to perform some action during a negotiation.
    **REQUEST**
        The sender requests the receiver to perform some action. One important class of
        uses of the request act is to request the receiver to perform another
        communicative act.
    **REQUEST_WHEN**
        The sender wants the receiver to perform some action when some given
        proposition becomes true.
    **REQUEST_WHENEVER**
        The sender wants the receiver to perform some action as soon as some
        proposition becomes true and thereafter each time the proposition becomes true
        again.
    **SUBSCRIBE**
        The act of requesting a persistent intention to notify the sender of the value
        of a reference, and to notify again whenever the object identified by the
        reference changes.
    """

    def _generate_next_value_(name, start, count, last_values):  # noqa
        return name.lower().replace("_", "-")

    ACCEPT_PROPOSAL = enum.auto()
    AGREE = enum.auto()
    CANCEL = enum.auto()
    CFP = enum.auto()
    CONFIRM = enum.auto()
    DISCONFIRM = enum.auto()
    FAILURE = enum.auto()
    INFORM = enum.auto()
    INFORM_IF = enum.auto()
    INFORM_REF = enum.auto()
    NOT_UNDERSTOOD = enum.auto()
    PROPAGATE = enum.auto()
    PROPOSE = enum.auto()
    PROXY = enum.auto()
    QUERY_IF = enum.auto()
    QUERY_REF = enum.auto()
    REFUSE = enum.auto()
    REJECT_PROPOSAL = enum.auto()
    REQUEST = enum.auto()
    REQUEST_WHEN = enum.auto()
    REQUEST_WHENEVER = enum.auto()
    SUBSCRIBE = enum.auto()


class ACLMessage:
    """
    Representation of an ACL Message as described in
    http://www.fipa.org/specs/fipa00061/.

    FIPA-defined fields are exposed as attributes. Custom fields (aka non FIPA-defined)
    are supported. You can access them using :func:`getattr` function. Those fields are
    prefixed with 'X-'.

    For example, if your message as a custom field named 'custom', you can access to it
    like this::

        value = getattr(msg, "X-custom")

    If you want to build a new :class:`ACLMessage`, use the provided builder
    :class:`ACLMessage.Builder`. Only the builder will make checks to ensure your
    message respects the fipa specification.
    """

    class Builder:
        """
        Ease :class:`ACLMessage` creation.

        It also perform some checks when the message is built. When building a message,
        you must:

        * Instantiate a new builder
        * use :meth:`performative` to set the message performative
        * use whatever method to fill the message
        * invoke the :meth:`build` method

        Calling twice the same method will override the previously set value.
        """

        def __init__(self):
            """Create a new :class:`ACLMessage.Builder`."""
            self._params: MutableMapping[str, Any] = {}

        def performative(self, value: Union[str, Performative]) -> ACLMessage.Builder:
            """Set the message performative."""
            self._params["performative"] = value
            return self

        def sender(self, value: AID) -> ACLMessage.Builder:
            """Set the message sender."""
            self._params["sender"] = value
            return self

        def receiver(self, value: Union[AID, Sequence[AID]]) -> ACLMessage.Builder:
            """Set the message receiver."""
            self._params["receiver"] = value
            return self

        def reply_to(self, value: AID) -> ACLMessage.Builder:
            """Set the reply_to field."""
            self._params["reply_to"] = value
            return self

        def content(self, value: Any) -> ACLMessage.Builder:
            """Set the message content."""
            self._params["content"] = value
            return self

        def language(self, value: str) -> ACLMessage.Builder:
            """Set the message language."""
            self._params["language"] = value
            return self

        def encoding(self, value: str) -> ACLMessage.Builder:
            """Set the message encoding."""
            self._params["encoding"] = value
            return self

        def ontology(self, value: str) -> ACLMessage.Builder:
            """Set the message ontology."""
            self._params["ontology"] = value
            return self

        def protocol(self, value: str) -> ACLMessage.Builder:
            """
            Set the message protocol.

            When set, you should also set the conversation-id and the reply-by fields.
            Otherwise the :meth:`ACLMessage.Builder.build` method will fail.
            """
            self._params["protocol"] = value
            return self

        def conversation_id(self, value: str) -> ACLMessage.Builder:
            """Set the message conversation id."""
            self._params["conversation_id"] = value
            return self

        def reply_with(self, value: str) -> ACLMessage.Builder:
            """Set the reply_with field."""
            self._params["reply_with"] = value
            return self

        def in_reply_to(self, value: str) -> ACLMessage.Builder:
            """Set the in_reply_to field."""
            self._params["in_reply_to"] = value
            return self

        def reply_by(self, value: datetime.datetime) -> ACLMessage.Builder:
            """Set the reply_by field."""
            self._params["reply_by"] = value
            return self

        def custom(self, key: str, value: Any) -> ACLMessage.Builder:
            """
            Add a custom field to the message.

            According to FIPA specification, the key should start with "X-".
            At message build, this will be done if your custom field doesn't already
            starts with it.

            :param key: the key to identify the custom field
            :param value: the value stored in the field
            """
            self._params[key] = value
            return self

        def build(self) -> ACLMessage:
            """
            Build the message.

            Also perform some sanity checks.

            :raise piaf.exceptions.MandatoryFieldValueException: if the performative field is not set
            :raise piaf.exceptions.MandatoryFieldValueException: when ``protocol`` is
                set, ``conversation_id`` and ``reply_by`` should also be set.
            """
            # Perform some checks
            self._check_performative()
            self._check_protocol()
            return ACLMessage(**self._params)

        def _check_performative(self):
            if "performative" not in self._params:
                raise piaf.exceptions.MandatoryFieldValueException("performative")

        def _check_protocol(self):
            if "protocol" in self._params:
                if "conversation_id" not in self._params:
                    raise piaf.exceptions.MandatoryFieldValueException(
                        "conversation_id"
                    )
                if "reply_by" not in self._params:
                    raise piaf.exceptions.MandatoryFieldValueException("reply_by")

    def __init__(
        self,
        performative: Union[str, Performative],
        sender: AID = None,
        receiver: Union[AID, Sequence[AID]] = None,
        reply_to: AID = None,
        content: Any = None,
        language: str = None,
        encoding: str = None,
        ontology: str = None,
        protocol: str = None,
        conversation_id: str = None,
        reply_with: str = None,
        in_reply_to: str = None,
        reply_by: datetime.datetime = None,
        **kwargs: Any,
    ):
        """
        Create a new :class:`ACLMessage`.

        Unless you know what you are doing, use the :class:`ACLMessage.Builder` class
        instead.
        Non fipa fields will be prefixed with 'X-' if not already set.
        """
        self.performative = performative
        self.sender = sender
        self.receiver = receiver
        self.reply_to = reply_to
        self.content = content
        self.language = language
        self.encoding = encoding
        self.ontology = ontology
        self.protocol = protocol
        self.conversation_id = conversation_id
        self.reply_with = reply_with
        self.in_reply_to = in_reply_to
        self.reply_by = reply_by

        # Non FIPA fields : prefix with 'X-' if not already set
        for k, v in kwargs.items():
            if not k.startswith("X-"):
                k = f"X-{k}"
            setattr(self, k, v)

    def __eq__(self, o: object) -> bool:
        """Two :class:`ACLMessage` objects are equals if all fields are equals."""
        if type(o) == type(self):
            for key, val in self.__dict__.items():
                try:
                    if getattr(o, key) != val:
                        return False
                except AttributeError:
                    return False
            return True
        return False

    def __repr__(self) -> str:
        """Textual representation of the ACLMessage for debugging purpose."""
        attrs_and_val = dict(self.__dict__.items())
        text = "ACLMessage("
        text += ",".join(map(lambda k: f"{k}={repr(attrs_and_val[k])}", attrs_and_val))
        return text + ")"


class MessageTemplate(abc.ABC):
    """Common interface for filtering messages."""

    @abc.abstractmethod
    def apply(self, message: ACLMessage) -> bool:
        """
        Apply the template to the provided message.

        :param message: the message to check
        """
        raise NotImplementedError()


class MT_OR(MessageTemplate):
    """Complex template that do a logic "OR" using the provided templates."""

    def __init__(self, a: MessageTemplate, b: MessageTemplate, *args):
        """
        Create a new OR message template with the provided message templates.

        You must provide at least two of them.

        :param a: the first message template
        :param b: the second message template
        :param args: any number of additional message templates
        """
        self._filters = [a, b] + list(args)

    def apply(self, message):
        return functools.reduce(operator.or_, (f.apply(message) for f in self._filters))


class MT_AND(MessageTemplate):
    """Complex template that do a logic "AND" using the provided templates."""

    def __init__(self, a: MessageTemplate, b: MessageTemplate, *args):
        self._filters = [a, b] + list(args)

    def apply(self, message):
        """
        Create a new AND message template with the provided message templates.

        You must provide at least two of them.

        :param a: the first message template
        :param b: the second message template
        :param args: any number of additional message templates
        """
        return functools.reduce(
            operator.and_, (f.apply(message) for f in self._filters)
        )


class MT_NOT(MessageTemplate):
    def __init__(self, template: MessageTemplate) -> None:
        self._template = template

    def apply(self, message: ACLMessage) -> bool:
        return not self._template.apply(message)


def _MT_factory(field_name: str) -> Type[MessageTemplate]:
    """
    Class factory used to create message templates matching simple message fields.

    :param field_name: the message field's name
    """

    def __init__(self, value: str):
        """
        Initializer for the class.

        :param value: the field's value
        """
        self._value = value

    def apply(self, message: ACLMessage) -> bool:
        return getattr(message, field_name) == self._value

    clazz = type(
        f"MT_{field_name.upper()}",
        (MessageTemplate,),
        {"__init__": __init__, "apply": apply},
    )
    return clazz


#: Check the performative field
MT_PERFORMATIVE = _MT_factory("performative")

#: Check the sender field
MT_SENDER = _MT_factory("sender")

#: Check the conversation_id field
MT_CONVERSATION_ID = _MT_factory("conversation_id")

#: Check the encoding field
MT_ENCODING = _MT_factory("encoding")

#: Check the in_reply_to field
MT_IN_REPLY_TO = _MT_factory("in_reply_to")

#: Check the language field
MT_LANGUAGE = _MT_factory("language")

#: Check the ontology field
MT_ONTOLOGY = _MT_factory("ontology")

#: Check the protocol field
MT_PROTOCOL = _MT_factory("protocol")

#: Check the reply_with field
MT_REPLY_WITH = _MT_factory("reply_with")

#: Check the reply_to field
MT_REPLY_TO = _MT_factory("reply_to")


class MT_ALL(MessageTemplate):
    """Special template that matches all messages."""

    def apply(self, message):
        return True


class ReceivedObject:
    """
    Object used in class:`Envelope` object.

    Contains information about the message path, including the ACC who transmitted the message to the receiver.
    See http://www.fipa.org/specs/fipa00067/SC00067F.html
    """

    class Builder:
        """Builder to ease :class:`ReceivedObject` creation."""

        FIPA_PREFIX = "X-"

        def __init__(self) -> None:
            """Create a new empty builder."""
            self._by: Optional[str] = None
            self._date: Optional[datetime.datetime] = None
            self._from: Optional[str] = None
            self._id: Optional[str] = None
            self._via: Optional[str] = None
            self._custom_fields: Dict[str, Any] = {}

        def by(self, by: str) -> ReceivedObject.Builder:
            """
            Set the by field value of the :class:`ReceivedObject` being built.

            Calling this method multiple times will replace previous value.
            """
            self._by = by
            return self

        def date(self, date: datetime.datetime) -> ReceivedObject.Builder:
            """
            Set the date field value of the :class:`ReceivedObject` being built.

            Calling this method multiple times will replace previous value.
            """
            self._date = date
            return self

        def from_(self, from_: str) -> ReceivedObject.Builder:
            """
            Set the from field value of the :class:`ReceivedObject` being built.

            Calling this method multiple times will replace previous value.
            """
            self._from = from_
            return self

        def id(self, id: str) -> ReceivedObject.Builder:
            """
            Set the id field value of the :class:`ReceivedObject` being built.

            Calling this method multiple times will replace previous value.
            """
            self._id = id
            return self

        def via(self, via: str) -> ReceivedObject.Builder:
            """
            Set the via field value of the :class:`ReceivedObject` being built.

            Calling this method multiple times will replace previous value.
            """
            self._via = via
            return self

        def custom(self, fieldname, value) -> ReceivedObject.Builder:
            """
            Add a custom field to the :class:`ReceivedObject` being built.

            The field name must start with FIPA prefix ('X-')
            :raise IllegalArgumentException: If fieldname doesn't start with FIPA prefix
            """
            if not fieldname.startswith(ReceivedObject.Builder.FIPA_PREFIX):
                raise piaf.exceptions.IllegalArgumentException(
                    f"Custom field {fieldname} doesn't start with {ReceivedObject.Builder.FIPA_PREFIX}"
                )
            self._custom_fields[fieldname] = value
            return self

        def build(self) -> ReceivedObject:
            """
            Build the received object.

            :raise MandatoryFieldValueException: if either 'by' or 'date' is not set.
            """
            if self._by is None:
                raise piaf.exceptions.MandatoryFieldValueException("by")
            if self._date is None:
                raise piaf.exceptions.MandatoryFieldValueException("date")
            return ReceivedObject(
                self._by,
                self._date,
                self._from,
                self._id,
                self._via,
                self._custom_fields,
            )

    def __init__(
        self,
        by: str,
        date: datetime.datetime,
        from_: str = None,
        id: str = None,
        via: str = None,
        custom: Dict[str, Any] = None,
    ) -> None:
        """
        Build a new :class:`ReceivedObject`.

        Parameters ``by`` and ``date`` are mandatory. Others can be omitted.

        :param by: URL representing the transport address of the receiving ACC
        :param date: The date when a message was received
        :param from_: The URL representing the transport address of the sending ACC, defaults to None
        :param id: The unique identifier of a message. It is required that uniqueness be garanteed within the scope of
            the sending ACC only, defaults to None
        :param via: The type of the MTP the message was delivered over, defaults to None
        :param custom: Custom fields with their value. Field names must start with FIPA prefix.
        """
        self.by = by
        self.date = date
        self.from_ = from_
        self.id = id
        self.via = via
        if custom is not None:
            self.__dict__.update(custom)

    def __deepcopy__(self, memo):
        custom = {
            name: copy.deepcopy(value, memo)
            for name, value in self.__dict__.items()
            if name.startswith(ReceivedObject.Builder.FIPA_PREFIX)
        }
        return ReceivedObject(
            copy.deepcopy(self.by, memo),
            copy.deepcopy(self.date, memo),
            copy.deepcopy(self.from_, memo),
            copy.deepcopy(self.id, memo),
            copy.deepcopy(self.via, memo),
            custom,
        )


class Envelope:
    """
    Representation of an :class:`ACLMessage` envelope.

    This class supports multiple definition for fields and thus can store the Envelope history.
    Accessing a field directly will always give the last version of it, but you can access to any version
    separately.

    See http://www.fipa.org/specs/fipa00067/SC00067F.html
    """

    class Builder:
        """
        Builder to ease :class:`Envelope` creation.

        There are three types of methods:

         - methods with name matching an Envelope field
         - the :meth:`Builder.with_group_of_fields` method
         - and the :meth:`Builder.build` method

        Each envelope is in fact an history of different fields. To reflect this, the builder
        works that way:

         - the first group of methods defines the history base, ie the value of fields at the creation of the envelope
         - the :meth:`Builder.with_group_of_fields` method adds modifications to fields. Each time the method is called,
           a new "revision" is created.

        In the end, you need to call method :meth:`Builder.build` to build the :class:`Envelope` object.
        """

        TO = "to"
        FROM = "from_"
        ACL_REPRESENTATION = "acl_representation"
        DATE = "date"
        COMMENTS = "comments"
        PLAYLOAD_LENGTH = "playload_length"
        PLAYLOAD_ENCODING = "playload_encoding"
        RECEIVED = "received"
        INTENDED_RECEIVER = "intended_receiver"
        TRANSPORT_BEHAVIOUR = "transport_behaviour"

        # Standard fields
        _FIELDNAMES = [
            TO,
            FROM,
            ACL_REPRESENTATION,
            DATE,
            COMMENTS,
            PLAYLOAD_LENGTH,
            PLAYLOAD_ENCODING,
            RECEIVED,
            INTENDED_RECEIVER,
            TRANSPORT_BEHAVIOUR,
        ]

        # Fipa prefix for custom fields
        _CUSTOM_FIELD_PREFIX = "X-"

        # Mandatory fields in base (revision 0)
        _MANDATORY_FIELDS = ["to", "from_", "acl_representation", "date"]

        def __init__(self) -> None:
            """Create a new :class:`Envelope.Builder` object."""
            self._base: Dict[str, Any] = {}
            self._groups: List[Dict[str, Any]] = [self._base]

        def to(self, to: Sequence[AID]) -> Envelope.Builder:
            """
            Set the ``to`` field of the envelope.

            Each time you call this method, it will replace the old value by the provided one.
            """
            self._base[Envelope.Builder.TO] = to
            return self

        def from_(self, from_: AID) -> Envelope.Builder:
            """
            Set the ``from`` field of the envelope.

            Each time you call this method, it will replace the old value by the provided one.
            """
            self._base[Envelope.Builder.FROM] = from_
            return self

        def acl_representation(self, acl_representation: str) -> Envelope.Builder:
            """
            Set the ``acl-representation`` field of the envelope.

            Each time you call this method, it will replace the old value by the provided one.
            """
            self._base[Envelope.Builder.ACL_REPRESENTATION] = acl_representation
            return self

        def date(self, date: datetime.datetime) -> Envelope.Builder:
            """
            Set the ``date`` field of the envelope.

            Each time you call this method, it will replace the old value by the provided one.
            """
            self._base[Envelope.Builder.DATE] = date
            return self

        def comments(self, comments: str) -> Envelope.Builder:
            """
            Set the ``comments`` field of the envelope.

            Each time you call this method, it will replace the old value by the provided one.
            """
            self._base[Envelope.Builder.COMMENTS] = comments
            return self

        def playload_length(self, playload_length: str) -> Envelope.Builder:
            """
            Set the ``playload-length`` field of the envelope.

            Each time you call this method, it will replace the old value by the provided one.
            """
            self._base[Envelope.Builder.PLAYLOAD_LENGTH] = playload_length
            return self

        def playload_encoding(self, playload_encoding: str) -> Envelope.Builder:
            """
            Set the ``playload-encoding`` field of the envelope.

            Each time you call this method, it will replace the old value by the provided one.
            """
            self._base[Envelope.Builder.PLAYLOAD_ENCODING] = playload_encoding
            return self

        def received(self, received: ReceivedObject) -> Envelope.Builder:
            """
            Set the ``received`` field of the envelope.

            Each time you call this method, it will replace the old value by the provided one.
            """
            self._base[Envelope.Builder.RECEIVED] = received
            return self

        def intended_receiver(
            self, intended_receiver: Sequence[AID]
        ) -> Envelope.Builder:
            """
            Set the ``intended-receiver`` field of the envelope.

            Each time you call this method, it will replace the old value by the provided one.
            """
            self._base[Envelope.Builder.INTENDED_RECEIVER] = intended_receiver
            return self

        def transport_behaviour(self, transport_behaviour) -> Envelope.Builder:
            """
            Set the ``transport-behaviour`` field of the envelope.

            Each time you call this method, it will replace the old value by the provided one.
            """
            self._base[Envelope.Builder.TRANSPORT_BEHAVIOUR] = transport_behaviour
            return self

        def custom(self, fieldname: str, value: Any) -> Envelope.Builder:
            """
            Add a custom field to the envelope.

            If the field was already set, the provided value will replace the old one. Note that according to
            specification, custom fields should start with "X-".
            """
            if not fieldname.startswith(Envelope.Builder._CUSTOM_FIELD_PREFIX):
                raise piaf.exceptions.IllegalArgumentException(
                    f"Custom field {fieldname} doesn't start with {Envelope.Builder._CUSTOM_FIELD_PREFIX}"
                )

            self._base[fieldname] = value
            return self

        def with_group_of_fields(self, group: Dict[str, Any]) -> Envelope.Builder:
            """
            Create a new revision.

            Each time this method is called, a new envelope revision is created. The revision will contain modified
            values + untouched ones.
            For example, if envelope is
            ``Envelope((AID("recv@localhost"),), AID("sender@localhost"), "custom.repr", 01/01/01T01:01)``
            and group is ``{"to": AID("recv2@localhost")}``, then revision 1 (0 is the base) will be
            ``Envelope((AID("recv2@localhost"),), AID("sender@localhost"), "custom.repr", 01/01/01T01:01)``

            Authorized fields are: to, from\\_, acl_representation, date, comments, playload_length, playload_encoding,
            received, intended_receiver, transport_behaviour and custom fields starting by "X-".
            """
            for field in group:
                if field not in Envelope.Builder._FIELDNAMES and not field.startswith(
                    Envelope.Builder._CUSTOM_FIELD_PREFIX
                ):
                    raise piaf.exceptions.IllegalArgumentException(
                        f"Custom field {field} doesn't start with {Envelope.Builder._CUSTOM_FIELD_PREFIX}"
                    )

            self._groups.append(group)
            return self

        def build(self) -> Envelope:
            """Build the envelope."""
            return Envelope(self._groups)

    def __init__(self, groups_of_fields: List[Dict[str, Any]]) -> None:
        """
        Create a new :class:`Envelope` object from the provided groups of fields.

        The first group is the base envelope, ie revision 0. It **MUST** contains the following fields :

        - to: Sequence[AID]
        - from\\_: AID
        - acl_representation: str
        - date: datetime.datetime

        Each additional group defines a new revision.
        Authorized fields are: to, from\\_, acl_representation, date, comments, playload_length, playload_encoding,
        received, intended_receiver, transport_behaviour and custom fields starting by "X-".

        :param group_of_fields: a list of groups
        :raise IndexError: the list must contain at least one group (base)
        :raise MandatoryFieldValueException: if one of the mandatory fields has no value (base group)
        """
        # Check base
        base = groups_of_fields[0]
        for m_field in Envelope.Builder._MANDATORY_FIELDS:
            if m_field not in base:
                raise piaf.exceptions.MandatoryFieldValueException(m_field)

        # Check additional revisions
        self._groups = [base]
        for group in groups_of_fields[1:]:
            self.add_revision(group)

    @property
    def to(self) -> Sequence[AID]:
        """Shortcut access to field to in last revision."""
        return self.get_field_value(Envelope.Builder.TO)

    @property
    def from_(self) -> AID:
        """Shortcut access to field from in last revision."""
        return self.get_field_value(Envelope.Builder.FROM)

    @property
    def acl_representation(self) -> str:
        """Shortcut access to field acl-representation in last revision."""
        return self.get_field_value(Envelope.Builder.ACL_REPRESENTATION)

    @property
    def date(self) -> datetime.datetime:
        """Shortcut access to field date in last revision."""
        return self.get_field_value(Envelope.Builder.DATE)

    @property
    def comments(self) -> str:
        """Shortcut access to field comments in last revision."""
        return self.get_field_value(Envelope.Builder.COMMENTS)

    @property
    def playload_length(self) -> str:
        """Shortcut access to field playload-length in last revision."""
        return self.get_field_value(Envelope.Builder.PLAYLOAD_LENGTH)

    @property
    def playload_encoding(self) -> str:
        """Shortcut access to field playload-encoding in last revision."""
        return self.get_field_value(Envelope.Builder.PLAYLOAD_ENCODING)

    @property
    def received(self) -> ReceivedObject:
        """Shortcut access to field received in last revision."""
        return self.get_field_value(Envelope.Builder.RECEIVED)

    @property
    def intended_receiver(self) -> Sequence[AID]:
        """Shortcut access to field intended-receiver in last revision."""
        return self.get_field_value(Envelope.Builder.INTENDED_RECEIVER)

    @property
    def transport_behaviour(self) -> Any:
        """Shortcut access to field transport-behaviour in last revision."""
        return self.get_field_value(Envelope.Builder.TRANSPORT_BEHAVIOUR)

    @property
    def last_revision_number(self) -> int:
        """Get last revision number."""
        return len(self._groups) - 1

    def get_field_value(self, field: str, revision: int = None) -> Any:
        """
        Get a field's value.

        If revision is None, last revision is assumed. Otherwise, must be an integer greater or equals to 0 (0 meaning
        base envelope).
        If the field doesn't exists, returned value is None (meaning no value associated).
        """
        value = None
        for i, group in enumerate(self._groups):
            if (revision is None or i <= revision) and field in group:
                value = group[field]
        return value

    def get_revision(self, revision: int = None) -> Dict[str, Any]:
        """
        Get a snapshot of fields in the desirated revision.

        If revision is None, last revision is assumed.
        Result is a mapping key -> value.
        """
        result: Dict[str, Any] = {}
        for i, group in enumerate(self._groups):
            if revision is None or i <= revision:
                for field in group:
                    result[field] = group[field]
        return result

    def add_revision(self, group_of_fields: Dict[str, Any]) -> None:
        """
        Create a new revision for this envelope.

        Each time this method is called, a new envelope revision is created. The revision will contain modified
        values + untouched ones.
        For example, if envelope is
        ``Envelope((AID("recv@localhost"),), AID("sender@localhost"), "custom.repr", 01/01/01T01:01)``
        and group is ``{"to": AID("recv2@localhost")}``, then revision 1 (0 is the base) will be
        ``Envelope((AID("recv2@localhost"),), AID("sender@localhost"), "custom.repr", 01/01/01T01:01)``

        Authorized fields are: to, from\\_, acl_representation, date, comments, playload_length, playload_encoding,
        received, intended_receiver, transport_behaviour and custom fields starting by "X-".
        """
        for field in group_of_fields:
            if field not in Envelope.Builder._FIELDNAMES and not field.startswith(
                Envelope.Builder._CUSTOM_FIELD_PREFIX
            ):
                raise piaf.exceptions.IllegalArgumentException(
                    f"Custom field {field} doesn't start with {Envelope.Builder._CUSTOM_FIELD_PREFIX}"
                )

        self._groups.append(group_of_fields)

    def __deepcopy__(self, memo):
        return Envelope(copy.deepcopy(self._groups, memo))


@dataclass(eq=True, frozen=True)
class Message:
    """Data class carrying both the :class:`Envelope` and the :class:`ACLMessage`."""

    envelope: Envelope
    acl_message: ACLMessage

    def __deepcopy__(self, memo):
        envelope = copy.deepcopy(self.envelope, memo)
        acl_message = copy.deepcopy(self.acl_message)

        return Message(envelope, acl_message)
