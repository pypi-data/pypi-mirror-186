from types import ModuleType
from typing import Any, TextIO

from wg_federation.data_transformation.saver.file.file_configuration_saver import FileConfigurationSaver
from wg_federation.utils.utils import Utils


class TextFileConfigurationSaver(FileConfigurationSaver):
    """
    Save any configuration to a signature file
    """
    _os_lib: ModuleType = None

    def __init__(self, pathlib_lib: ModuleType, os_lib: ModuleType):
        self._os_lib = os_lib
        super().__init__(pathlib_lib)

    def supports(self, data: dict, destination: Any) -> bool:
        return super().supports(data, destination) and \
            Utils.has_extension(destination, r'(digest|sha([0-9]{3})?|md5|sig|txt)')

    def _save_data(self, data: dict, file: TextIO) -> None:
        super()._save_data(data, file)

        file.write(self._os_lib.linesep.join(
            list(map(str, data.values()))
        ))
