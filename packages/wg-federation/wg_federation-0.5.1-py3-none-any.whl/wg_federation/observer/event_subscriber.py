from abc import ABC
from enum import Enum
from typing import TypeVar, Generic

from wg_federation.observer.is_data_class import IsDataClass

_IsDataClassT = TypeVar('_IsDataClassT', bound=IsDataClass)


class EventSubscriber(ABC, Generic[_IsDataClassT]):
    """
    Abstract class for any kind of EventSubscriber any kind of events, previously registered.
    """

    def get_subscribed_events(self) -> list[Enum]:
        """
        Returns the list of events that this subscriber listens to.
        :return: list of Enums of type Sequence[str, type, Optional[bool]]
        """
        raise NotImplementedError

    # OK, since it might be used by subclasses.
    # pylint: disable=unused-argument
    def should_run(self, data: _IsDataClassT) -> bool:
        """
        Whether the subscriber should run.
        Use this method to set conditions to determine whether the subscriber `run` method needs to be called or not.
        :param data:
        :return:
        """
        return True

    def run(self, data: _IsDataClassT) -> _IsDataClassT:
        """
        Runs the subscriber.
        Whether this method is called depends on the local `should_run`.
        It also depends on various logic in the EventDispatcher, for example, the validity of the data object.
        :param data: Any kind of data expected by your specific implementation of a subscriber.
        :raise SubscriberGracefulError when this subscriber failed to execute correctly,
          but you want the program execution to continue gracefully.
        :return: Same data type passed as argument, unchanged or mutated.
        """
        raise NotImplementedError

    @classmethod
    def must_stop_propagation(cls) -> bool:
        """
        Whether to stop propagation to other subscribers at the end of this specific subscriber.
        Useful when a specific subscriber requires preventing any other subscriber to run.
        :return:
        """
        return False

    def get_order(self) -> int:
        """
        Order of execution for this specific subscriber, compared to other subscribers.
        Lower values will always be executed before high values.
        Two subscribers with the same order value will have precedences determined by order of registration using FIFO.
        :return:
        """
        return 500
