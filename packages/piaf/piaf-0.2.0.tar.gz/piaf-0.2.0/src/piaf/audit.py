# coding: utf-8
"""This module contains all the tools to work with events."""
from __future__ import annotations

import abc
import asyncio
import logging
from dataclasses import dataclass
from time import time
from typing import Any, Dict, Iterable, Set, Tuple


@dataclass(frozen=True, eq=True)
class Event:
    """
    The minimal structure of an event.

    It contains three fields:

    - `source`: from which component the event is emitted
    - `type`: what kind of event it is. Useful to know the content of the `data` field
    - `data`: the piece of data the event contains

    This class shouldn't be extended. Use the combination of the `type` and `data` field to extend the diversity of events.
    """

    source: str
    type: str
    data: Any


@dataclass(frozen=True, eq=True)
class EventRecord:
    """
    A tiny wrapper around an :class:`Event` that brings additional information.

    Each record contains three fields:

    - `event`: the :class:`Event` instance this record wraps
    - `timestamp`: when the event was emitted (second resolution)
    - `topics`: a tuple of topics where the event was broadcasted

    :class:`EventRecord` is what you manipulate in a custom :class:`Subscriber`.
    """

    event: Event
    timestamp: int
    topics: Tuple[Topic, ...]


class Topic:
    """
    A :class:`Topic` is the way to filter events.

    Rather than being a simple string, topics are hierarchical objects very much like loggers. Each topic, except the root one (`Topic(name="", parent=None)), have a parent :class:`Topic`.

    Combined with the :class:`Subscriber`, topics allow complex events broadcast scenarios.

    Topics are cached, meaning that if you create two topics, they will have at least the root topic in common (hierarchy is a tree).
    """

    DEFAULT_SEP = "."
    __CACHE: Set[Topic] = set()

    @classmethod
    def __from_cache(cls, name: str, parent: Topic | None) -> Topic | None:
        """
        Lookup the cache and try to get an existing :class:`Topic`.

        :param name: the topic's name
        :param parent: the parent of the topic
        :return: the :class:`Topic` instance or `None` if there is no such topic in the cache.
        """
        for topic in cls.__CACHE:
            if topic._name == name and topic._parent == parent:
                return topic
        return None

    @classmethod
    def from_str(cls, topic: str) -> Topic:
        """
        The right way to create topics.

        This method will create the full hierarchy of topics from the given string. Parent topics are separated by `.` (dots). For example, "parent.topic" will create three topics: `Topic(name="topic", parent=Topic(name="parent", parent=Topic(name="", parent=None)))`

        :param topic: the full name of the topic
        :return: the full topic's hierarchy
        """
        parts = topic.split(cls.DEFAULT_SEP)
        if parts[0] != "":
            parts.insert(0, "")  # Root topic

        prev = None
        for part in parts:
            prev = Topic(part, prev)
        return prev  # type: ignore

    @classmethod
    def resolve_from_parent_topic(cls, parent: Topic, topic: str) -> Topic:
        """
        Resolve the given str against the provided parent topic.

        This method will create the full hierarchy of topics from the given string, starting from parent. Parent topics are separated by `.` (dots). For example, "parent.topic" will create three topics: `Topic(name="topic", parent=Topic(name="parent", parent=Topic(name="", parent=None)))`

        :param parent: the parent topic
        :param topic: the full name of the child topic
        :return: the full topic's hierarchy
        """
        parts = topic.split(cls.DEFAULT_SEP)
        if parts[0] == "":
            return parent

        prev = parent
        for part in parts:
            prev = Topic(part, prev)
        return prev

    def __new__(cls, name: str, parent: Topic | None):
        """
        Override the default behavior of `__new__` by looking up the cache.

        If a matching topic already exist (same name and parent), then the cached object is returned. Otherwise the default behavior is called and a new instance is created.

        :param name: the topic's name
        :param parent: the topic's parent
        :return: a :class:`Topic` instance
        """
        topic = cls.__from_cache(name, parent)
        if topic is not None:
            return topic
        return super().__new__(cls)

    def __init__(self, name: str, parent: Topic | None) -> None:
        """
        Initialize the :class:`Topic` instance returned by :meth:`Topic.__new__`.

        If the provided instance is in the cache, initialization is skipped. :class:`Topic` creation should be done using the classmethod :meth:`Topic.from_str` rather than using the constructor.

        :param name: the topic's name
        :param parent: the topic's parent
        """
        try:
            # If the object is in the cache, skip initialization
            self in self.__CACHE
            return
        except AttributeError:
            # The object is not yet initialized and thus doesn't have the _name and the _parent attributes
            pass

        self._name = name
        self._parent = parent
        self.__CACHE.add(self)

    @property
    def name(self) -> str:
        """
        Get this topic's name.

        :return: the name
        """
        return self._name

    @property
    def parent(self) -> Topic | None:
        """
        Get this topic's parent.

        :return: the parent or `None` if this topic is the root topic
        """
        return self._parent

    def __str__(self) -> str:
        return f"{str(self.parent) if self.parent is not None else ''}{self.DEFAULT_SEP if self.parent is not None else ''}{self.name}"

    def __repr__(self) -> str:
        return f"Topic[parent={str(self.parent)}, name={self.name}]"

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Topic) and o.name == self.name and o.parent == self.parent

    def __hash__(self) -> int:
        return hash((self.name, self.parent))

    def __truediv__(self, o: str) -> Topic:
        if not isinstance(o, str):
            raise TypeError(
                f"Can't create a new topic using a non-str of type {type(o).__name__}"
            )
        return Topic.resolve_from_parent_topic(self, o)


PLATFORM_TOPIC = Topic.from_str("platform")
ACC_TOPIC = Topic.from_str("platform.acc")
AGENTS_PARENT_TOPIC = Topic.from_str("platform.agents")


class Subscriber(metaclass=abc.ABCMeta):
    """
    Abstract definition of a subscriber.

    Subscribers have only one method called :meth:`Subscriber.on_event`, which gets called when an event is published on a topic the subscriber is listening to.

    The subscription part is realized in the :class:`EventManager`.
    """

    @abc.abstractmethod
    async def on_event(self, event_record: EventRecord) -> None:
        """
        Called when an event is published on a topic this subscriber is listening to.

        :param event_record: the :class:`EventRecord` that wraps the published event.
        """
        raise NotImplementedError()

    async def close(self):
        """
        Close this subscriber by performing cleanup.

        Default implementation does nothing.
        """
        pass


class EventManager:
    """
    The heart of the AuditAPI.

    The :class:`EventManager` holds the binding between topics and subscribers and also the publish/notify algorithm.
    """

    def __init__(self) -> None:
        """Initialize a new :class:`EventManager` instance with no topics nor subscribers."""
        self._subscribers: Dict[Topic, Set[Subscriber]] = {}
        self._tasks: Set[asyncio.Task] = set()
        self.logger = logging.getLogger(type(self).__name__)

    async def publish(self, event: Event, topics: Topic | Iterable[Topic]) -> None:
        """
        Publish the given event on the given topics.

        The notification algorithm is the following:

        1. Topics are expanded to get the full hierarchy of topics
        2. For each topic in the expanded set, get the registered subscribers
        3. For each (unique) subscriber, call the :meth:`Subscriber.on_event` method

        :param event: the event that is being published
        :param topics: either a :class:`Topic` or a list of topics where the event is published
        """
        if isinstance(topics, Topic):
            topics = [topics]

        # Expand topics to get the full hierarchy
        expanded_topics: Set[Topic] = set()
        for topic in topics:
            expanded_topics.add(topic)
            parent = topic.parent
            while parent is not None:
                expanded_topics.add(parent)
                parent = parent.parent

        # Retrieve subscribers
        subscribers: Set[Subscriber] = set()
        for topic in expanded_topics:
            subscribers |= self._subscribers.get(topic, set())

        # Notify subscribers
        record = EventRecord(event, int(time()), tuple(topics))
        for subscriber in subscribers:
            await subscriber.on_event(record)

    def publish_sync(self, event: Event, topics: Topic | Iterable[Topic]) -> None:
        """
        Synchronous version of :meth:`EventManager.publish`.

        :param event: the event that is being published
        :param topics: either a :class:`Topic` or a list of topics where the event is published
        """
        task = asyncio.create_task(self.publish(event, topics))
        self._tasks.add(task)

        async def _cleanup():
            await task
            self._tasks.discard(task)

        asyncio.create_task(_cleanup())

    def subscribe_to(
        self, subscriber: Subscriber, topics: Topic | Iterable[Topic]
    ) -> None:
        """
        Bind the given subscriber to the provided list of topics.

        After this call, the subscriber will get notified when an event is published on one of the given topics.

        :param subscriber: the subscriber to bind
        :param topics: either a :class:`Topic` or a list of topics that will be bound to the subscriber
        """
        if isinstance(topics, Topic):
            topics = [topics]

        for topic in topics:
            subscribers = self._subscribers.setdefault(topic, set())
            subscribers.add(subscriber)

    async def close(self) -> None:
        """
        Close the :class:`EventManager` and give a chance to subscribers to cleanup.
        """
        # Wait until synchronous publishes are done
        if self._tasks:
            await asyncio.wait(self._tasks, return_when=asyncio.ALL_COMPLETED)

        # Close all subscribers
        all_subscribers = set()
        for subscribers in self._subscribers.values():
            all_subscribers.update(subscribers)
        map(Subscriber.close, all_subscribers)
