from abc import ABC, abstractmethod
from typing import Any


class CanLoadConfigurationInterface(ABC):
    """
    Interface describing a class that can load any kind of configuration, from a single source or multiple sources.
    """

    @abstractmethod
    def load_if_exists(self, source: Any, configuration_loader: type = None) -> dict:
        """
        Load a configuration source of source_kind, ignoring whether the source can be processed
        :raise InvalidDataError When source was loaded but contains invalid data
        :param source: Source of the configuration
        :param configuration_loader: ConfigurationLoader to be forcefully used
        :return: Configuration as a dict or empty dict if source is unsupported
        """

    @abstractmethod
    def load(self, source: Any, configuration_loader: type = None) -> dict:
        """
        Load a configuration source of source_kind.
        :raise SourceUnsupportedError When source is not supported because no ConfigurationLoader can handle it.
        :raise InvalidDataError When source was loaded but contains invalid data
        :param source: Source of the configuration
        :param configuration_loader: ConfigurationLoader to be forcefully used
        :return: Configuration as a dict
        """

    @abstractmethod
    def load_all_if_exists(self, sources: tuple[Any, ...]) -> dict:
        """
        Load multiple sources and unify them into a single configuration with a deep merge.
        Ignore sources that are not supported
        :raise InvalidDataError When source was loaded but contains invalid data
        :param sources: Sources of the configurations
        :return: Unified configuration as a dict
        """

    @abstractmethod
    def load_all(self, sources: tuple[Any, ...]) -> dict:
        """
        Load multiple sources and unify them into a single configuration with a deep merge.
        :raise SourceUnsupportedError When a source is not supported because no ConfigurationLoader can handle it.
        :raise InvalidDataError When source was loaded but contains invalid data
        :param sources: Sources of the configurations
        :return: Unified configuration as a dict
        """
