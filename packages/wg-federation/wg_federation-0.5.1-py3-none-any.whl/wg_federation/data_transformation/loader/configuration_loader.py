import functools
import logging
from typing import Any

from deepmerge import always_merger

from wg_federation.data_transformation.loader.can_load_configuration_interface import CanLoadConfigurationInterface
from wg_federation.data_transformation.loader.configuration_loader_interface import ConfigurationLoaderInterface
from wg_federation.exception.developer.data_transformation.source_unsupported_error import SourceUnsupportedError
from wg_federation.utils.utils import Utils


class ConfigurationLoader(CanLoadConfigurationInterface):
    """
    Read any configuration from any sources
    """
    _configuration_loaders: tuple[ConfigurationLoaderInterface, ...] = None
    _logger: logging.Logger = None

    def __init__(
            self,
            configuration_loaders: tuple[ConfigurationLoaderInterface, ...],
            logger: logging.Logger,
    ):
        """
        Constructor
        :param configuration_loaders:
        :param logger:
        """
        self._configuration_loaders = tuple(configuration_loaders)
        self._logger = logger

    def load_if_exists(self, source: Any, configuration_loader: type = None) -> dict:
        try:
            return self.load(source, configuration_loader)
        except SourceUnsupportedError:
            return {}

    def load(self, source: Any, configuration_loader: type = None) -> dict:
        if configuration_loader:
            return self.__do_load_from(self._fetch(configuration_loader), source)

        for _configuration_loader in self._configuration_loaders:
            if _configuration_loader.supports(source):
                return self.__do_load_from(_configuration_loader, source)

        raise SourceUnsupportedError(
            f'Could not load any configuration from “{source} ({configuration_loader})”. '
            f'It seems no ConfigurationLoader supports this type of source.'
        )

    def load_all_if_exists(self, sources: tuple[Any, ...]) -> dict:
        return functools.reduce(self.__merge_configuration_if_exists, sources, {})

    def load_all(self, sources: tuple[Any, ...]) -> dict:
        return functools.reduce(self.__merge_configuration, sources, {})

    def _fetch(self, configuration_loader: type = None) -> ConfigurationLoaderInterface:
        for _configuration_loader in self._configuration_loaders:
            if isinstance(_configuration_loader, configuration_loader):
                return _configuration_loader

        raise TypeError(
            f'Unable to fetch ConfigurationLoader of type “{configuration_loader}”. '
            f'Either this type does not implement ConfigurationLoaderInterface or it was not registered.'
        )

    def __do_load_from(self, configuration_loader: ConfigurationLoaderInterface, source: Any) -> dict:
        self._logger.debug(
            f'{Utils.classname(configuration_loader)} '
            f'configuration loader supports {source}.'
        )
        return dict(configuration_loader.load_from(source))

    def __merge_configuration(self, previous_configuration: dict, next_source: Any) -> dict:
        return dict(always_merger.merge(previous_configuration, self.load(next_source)))

    def __merge_configuration_if_exists(self, previous_configuration: dict, next_source: Any) -> dict:
        return dict(always_merger.merge(previous_configuration, self.load_if_exists(next_source)))
