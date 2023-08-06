from abc import ABC, abstractmethod
from typing import Any


class CanSaveConfigurationInterface(ABC):
    """
    Interface describing a class that can save configuration to any kind of destination.
    """

    @abstractmethod
    def save_try(self, data: dict, destination: Any, configuration_saver: type = None) -> None:
        """
        Save a given data to a given destination (path or any handler).
        Do not guarantee that data is written.
        Ignore destination errors.
        :param data: Data to be saved
        :param destination: destination for the data to save. Can be a path or an open handler to the destination.
        :param configuration_saver: Force a specific ConfigurationSaver to use
        :return:
        """

    @abstractmethod
    def save(self, data: dict, destination: Any, configuration_saver: type = None) -> None:
        """
        Save a given data to a given destination (path or any handler).
        :param data: Data to be saved
        :param destination: destination for the data to save. Can be a path or an open handler to the destination.
        :param configuration_saver: Force a specific ConfigurationSaver to use
        :raise DestinationUnsupportedError when the destination is not available or not valid
        :return:
        """
