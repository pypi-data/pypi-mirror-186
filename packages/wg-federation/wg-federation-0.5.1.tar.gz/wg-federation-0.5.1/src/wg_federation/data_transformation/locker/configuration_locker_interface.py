from abc import ABC, abstractmethod
from typing import ContextManager


class ConfigurationLockerInterface(ABC):
    """
    Interface describing a class that can lock any kind of configuration.
    """

    @abstractmethod
    def obtain_exclusive_lock(self, location: str) -> ContextManager:
        """
        Obtain the exclusive lock for a location.
        To be used with a python "with".
        ```
        with my_locker.obtain_lock_exclusive(location):
            do_some_actions while location is locked.
        ```
        :param location: Location to be locked.
        :return:
        """

    @abstractmethod
    def obtain_shared_lock(self, location: str) -> ContextManager:
        """
        Obtain the shared lock for a location.
        To be used with a python "with".
        ```
        with my_locker.obtain_lock_shared(location):
            do_some_actions while location is locked.
        ```
        :param location: Location to be locked.
        :return:
        """

    @abstractmethod
    def is_default_for(self, location: str) -> bool:
        """
        Whether this locker is the default choice for the location given
        :param location: Location to be locked
        :return: True if this lock is the default for the given location, false otherwise
        """
