from abc import ABC
from io import TextIOWrapper
from types import ModuleType
from typing import Any, TextIO

from wg_federation.data_transformation.saver.configuration_saver_interface import ConfigurationSaverInterface
from wg_federation.utils.utils import Utils


class FileConfigurationSaver(ConfigurationSaverInterface, ABC):
    """
    Save any configuration from to kind of files
    """

    _pathlib_lib: ModuleType = None

    def __init__(self, pathlib_lib: ModuleType):
        """
        Constructor
        :param pathlib_lib:
        """
        self._pathlib_lib = pathlib_lib

    def save_to(self, data: dict, destination: Any) -> None:
        if not isinstance(destination, TextIOWrapper):
            with Utils.open(file=destination, mode='w+', encoding='utf-8') as file:
                self._save_data(data, file)
                return

        self._save_data(data, destination)

    def supports(self, data: dict, destination: Any) -> bool:
        return isinstance(destination, (str, TextIOWrapper))

    def is_initialized(self, data: dict, destination: Any) -> bool:
        if not isinstance(destination, TextIOWrapper) and not self._pathlib_lib.Path(destination).exists():
            return False

        return True

    def initialize(self, data: dict, destination: Any) -> None:
        self._pathlib_lib.Path(destination).parents[0].mkdir(parents=True, exist_ok=True)

    # pylint: disable=unused-argument
    def _save_data(self, data: dict, file: TextIO) -> None:
        """
        Process an open file and returns configuration
        :param file: open file handler
        :return: configuration
        """
        file.truncate(0)
