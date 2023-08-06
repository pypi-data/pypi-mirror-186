import json
from typing import Any, TextIO

from wg_federation.data_transformation.saver.file.file_configuration_saver import FileConfigurationSaver
from wg_federation.utils.utils import Utils


class JsonFileConfigurationSaver(FileConfigurationSaver):
    """
    Save any configuration to JSON files
    """

    def supports(self, data: dict, destination: Any) -> bool:
        return super().supports(data, destination) and \
            Utils.has_extension(destination, 'json')

    def _save_data(self, data: dict, file: TextIO) -> None:
        super()._save_data(data, file)
        json.dump(data, file)
