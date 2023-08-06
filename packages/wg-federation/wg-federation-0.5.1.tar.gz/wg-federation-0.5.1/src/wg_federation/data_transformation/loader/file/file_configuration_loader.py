from abc import ABC
from io import TextIOWrapper
from types import ModuleType
from typing import Any, TextIO

from wg_federation.data_transformation.loader.configuration_loader_interface import ConfigurationLoaderInterface
from wg_federation.utils.utils import Utils


class FileConfigurationLoader(ConfigurationLoaderInterface, ABC):
    """
    Read any configuration from any kind of files
    """

    _os_path_lib: ModuleType = None

    def __init__(self, os_path_lib: ModuleType):
        """
        Constructor
        :param os_path_lib:
        """
        self._os_path_lib = os_path_lib

    def load_from(self, source: Any) -> dict:
        if not isinstance(source, TextIOWrapper):
            with Utils.open(file=source, mode='r+', encoding='utf-8') as file:
                return self._load_file(file)

        return self._load_file(source)

    def supports(self, source: Any) -> bool:
        return (isinstance(source, str) and self._os_path_lib.exists(source)) \
            or isinstance(source, TextIOWrapper)

    def _load_file(self, file: TextIO) -> dict:
        """
        Process an open file and returns configuration
        :param file: open file handler
        :return: configuration
        """
        file.seek(0)
        return {}
