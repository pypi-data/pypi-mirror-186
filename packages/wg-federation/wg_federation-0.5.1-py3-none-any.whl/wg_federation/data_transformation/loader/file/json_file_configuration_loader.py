import json
from typing import Any, TextIO

from wg_federation.data_transformation.loader.file.file_configuration_loader import FileConfigurationLoader
from wg_federation.utils.utils import Utils


class JsonFileConfigurationLoader(FileConfigurationLoader):
    """
    Read any configuration from JSON files
    """

    def supports(self, source: Any) -> bool:
        return super().supports(source) and \
            Utils.has_extension(source, 'json')

    def _load_file(self, file: TextIO) -> dict:
        super()._load_file(file)
        return Utils.always_dict(json.load(file))
