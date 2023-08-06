import logging
from enum import Enum
from typing import Optional, Iterable, Any, Sequence

from wg_federation.observer.error.subscriber_graceful_error import SubscriberGracefulError
from wg_federation.observer.event_subscriber import EventSubscriber
from wg_federation.observer.is_data_class import IsDataClass
from wg_federation.utils.utils import Utils


class EventDispatcher:
    """
    Dispatches any kind of events through class implementing EventSubscriberInterfaces.
    EventSubscriberInterfaces classes must be previously registered.
    """
    _subscribers: dict[tuple[int, int], EventSubscriber] = None
    _logger: logging.Logger = None

    def __init__(self, logger: logging.Logger, subscribers: list[EventSubscriber] = None):
        """
        Constructor
        :param logger:
        """
        self._logger = logger
        if not subscribers:
            subscribers = []
        if not self._subscribers:
            self._subscribers = {}
        for subscriber in subscribers:
            self.register(subscriber)

    def register(self, subscriber: EventSubscriber, increment: int = 0) -> None:
        """
        Adds another subscriber to the set of subscribers handled by this class.
        :param subscriber:
        :param increment: Do not use this argument directly. Used internally to determine order for subscribers
          with the same order value.
        :return:
        """
        if (subscriber.get_order(), increment) in self._subscribers:
            self.register(subscriber, increment + 1)
            return

        self._subscribers[(subscriber.get_order(), increment)] = subscriber
        return

    def dispatch(self, events: list[Enum], data: IsDataClass) -> IsDataClass:
        """
        Dispatch one or more events. Runs all subscribers that are subscribed to one or more of the events.
        :param events: Any kind of Enum set to a specific value.
        :param data: Any kind of data expected by subscribers listening to it.
        :return: data, modified or unmodified.
        """

        events = self._filter_invalid_events(events)
        self._logger.debug(
            f'Dispatching “{", ".join(self._extract_event_names(Utils.enums_to_list(events)))}” events.'
        )

        for subscriber in self._get_ordered_subscribers():
            subscribed_events: Sequence[tuple[str, type, Optional[bool]]] = self._intersect_events(
                events, subscriber.get_subscribed_events()
            )

            if len(subscribed_events) == 0:
                continue

            if not self._subscribed_events_support_data(subscribed_events, data):
                self._logger.warning(
                    f'Subscribed \u22C2 Dispatched events do not support type “{type(data)}”. '
                    f'Therefore, {Utils.classname(subscriber)} is always ignored. '
                    f'This is probably unwanted. Make sure data and dispatched event have the same type.'
                )
                continue

            if not subscriber.should_run(data):
                self._logger.debug(
                    f'{Utils.classname(subscriber)} was skipped.'
                )
                continue

            try:
                if self._events_allows_data_mutation(subscribed_events):
                    data = subscriber.run(data)
                else:
                    subscriber.run(data)
            except SubscriberGracefulError as error:
                self._logger.warning(
                    f'{Utils.classname(subscriber)} failed. '
                    f'This error was raised: {str(error)}'
                )
                continue

            self._logger.debug(
                f'{Utils.classname(subscriber)} was run in response to: '
                f'“{", ".join(self._extract_event_names(subscribed_events))}”. Allowing mutable data? '
                f'{str(self._events_allows_data_mutation(subscribed_events))}.'
            )

            if subscriber.must_stop_propagation():
                self._logger.debug(f'Stopping event propagation as per “{Utils.classname(subscriber)}” option.')
                break

        return data

    def _subscribed_events_support_data(
            self, events: Sequence[tuple[str, type, Optional[bool]]], data: IsDataClass
    ) -> bool:
        for event in events:
            if not isinstance(data, event[1]):
                return False

        return True

    def _filter_invalid_events(self, events: list[Enum]) -> list[Enum]:
        """ Filters out invalid events """

        def filter_events(event: Enum) -> bool:
            if self._is_event_valid(event.value):
                return True

            self._logger.warning(
                f'An event named “{str(event)}” is invalid, thus, it was filtered out.'
                'Make sure any event is an Enum set to a value containing “tuple[str, type, Optional[bool]]”.'
                'The tuple must have three values, in order: '
                ' 1. "str": the name of the event.'
                ' 2. "type": the accepted data type.'
                ' 3. "Optional[bool]": True if the type is mutable.',
            )
            return False

        return list(filter(filter_events, events))

    def _intersect_events(
            self, events: list[Enum], other_events: list[Enum]
    ) -> Sequence[tuple[str, type, Optional[bool]]]:
        return Utils.enums_to_list(list(
            set(self._filter_invalid_events(events)).intersection(self._filter_invalid_events(other_events))
        ))

    def _is_event_valid(self, enum_value: Any) -> bool:
        return isinstance(enum_value, Sequence) and isinstance(enum_value[0], str) and isinstance(enum_value[1], type)

    def _events_allows_data_mutation(self, events: Sequence[tuple[str, type, Optional[bool]]]) -> bool:
        for event in events:
            if len(event) <= 2 or not event[2]:
                return False

        return True

    def _get_ordered_subscribers(self) -> Iterable[EventSubscriber]:
        return dict(sorted(self._subscribers.items())).values()

    def _extract_event_names(self, events: Sequence[tuple[str, type, Optional[bool]]]) -> list[str]:
        return list(map(lambda x: x[0], events))
