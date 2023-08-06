import logging
from typing import Any

from wg_federation.data_transformation.saver.can_save_configuration_interface import CanSaveConfigurationInterface
from wg_federation.data_transformation.saver.configuration_saver_interface import ConfigurationSaverInterface
from wg_federation.exception.developer.data_transformation.destination_unsupported_error import \
    DestinationUnsupportedError
from wg_federation.utils.utils import Utils


class ConfigurationSaver(CanSaveConfigurationInterface):
    """
    Save any configuration to any destination
    """
    _configuration_savers: tuple[ConfigurationSaverInterface, ...] = None
    _logger: logging.Logger = None

    def __init__(
            self,
            configuration_savers: tuple[ConfigurationSaverInterface, ...],
            logger: logging.Logger,
    ):
        """
        Constructor
        :param configuration_savers:
        :param logger:
        """
        self._configuration_savers = tuple(configuration_savers)
        self._logger = logger

    def save_try(self, data: dict, destination: Any, configuration_saver: type = None) -> None:
        try:
            self.save(data, destination, configuration_saver)
        except DestinationUnsupportedError:
            return

    def save(self, data: dict, destination: Any, configuration_saver: type = None) -> None:
        if configuration_saver:
            self.__do_save_to(data, destination, self._fetch(configuration_saver))
            return

        for _configuration_saver in self._configuration_savers:
            if _configuration_saver.supports(data, destination):
                self.__do_save_to(data, destination, _configuration_saver)
                return

        raise DestinationUnsupportedError(
            f'Could not save configuration to “{str(destination)} ({configuration_saver})”. '
            f'It seems no ConfigurationSaver supports this type of data or destination.'
        )

    def _fetch(self, configuration_saver: type = None) -> ConfigurationSaverInterface:
        for _configuration_saver in self._configuration_savers:
            if isinstance(_configuration_saver, configuration_saver):
                return _configuration_saver

        raise TypeError(
            f'Unable to fetch ConfigurationSaver of type “{configuration_saver}”. '
            f'Either this type does not implement ConfigurationSaverInterface or it was not registered.'
        )

    def __do_save_to(self, data: dict, destination: Any, configuration_saver: ConfigurationSaverInterface) -> None:
        if not configuration_saver.is_initialized(data, destination):
            self._logger.debug(
                f'{Utils.classname(configuration_saver)} '
                f'configuration saver initializing {str(destination)}.'
            )
            configuration_saver.initialize(data, destination)

        self._logger.debug(
            f'{Utils.classname(configuration_saver)} '
            f'configuration saver used for {str(destination)}.'
        )
        configuration_saver.save_to(data, destination)
