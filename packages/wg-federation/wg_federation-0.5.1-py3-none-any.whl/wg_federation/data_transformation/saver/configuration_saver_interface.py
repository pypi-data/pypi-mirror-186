from abc import ABC, abstractmethod
from typing import Any


class ConfigurationSaverInterface(ABC):
    """
    Configuration Saver interface. Represents any configuration saver.
    """

    @abstractmethod
    def save_to(self, data: dict, destination: Any) -> None:
        """
        Save configuration to the destination.
        :param data: data to save
        :param destination: destination for the data to save. Can be a string or an open handler to the destination.
        :return: configuration
        """

    @abstractmethod
    def supports(self, data: dict, destination: Any) -> bool:
        """
        Whether the configuration saver supports the given destination
        :param data: data to save
        :param destination: destination for the data to save. Can be a string or an open handler to the destination.
        :return: True if the configuration saver supports the destination, false otherwise.
        """

    @abstractmethod
    def is_initialized(self, data: dict, destination: Any) -> bool:
        """
        Whether data and destination are properly initialized
        :param data: data to save
        :param destination: destination for the data to save. Can be a string or an open handler to the destination.
        :return: True if the configuration location is initialized, False otherwise
        """

    @abstractmethod
    def initialize(self, data: dict, destination: Any) -> None:
        """
        Initialize the destination the first time it is accessed
        :param data: data to save
        :param destination: destination for the data to save. Can be a string or an open handler to the destination.
        :return:
        """
