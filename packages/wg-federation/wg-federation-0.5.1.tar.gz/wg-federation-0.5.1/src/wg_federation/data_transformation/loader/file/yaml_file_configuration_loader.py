from typing import Any, TextIO

import yaml

from wg_federation.data_transformation.loader.file.file_configuration_loader import FileConfigurationLoader
from wg_federation.utils.utils import Utils


class YamlFileConfigurationLoader(FileConfigurationLoader):
    """
    Read any configuration from YAML files
    """

    def supports(self, source: Any) -> bool:
        return super().supports(source) and \
            Utils.has_extension(source, r'(yaml|yml)')

    def _load_file(self, file: TextIO) -> dict:
        super()._load_file(file)
        return Utils.always_dict(yaml.safe_load(file))
