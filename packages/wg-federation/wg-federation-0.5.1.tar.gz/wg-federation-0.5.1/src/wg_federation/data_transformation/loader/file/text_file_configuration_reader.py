from typing import Any, TextIO

from wg_federation.data_transformation.loader.file.file_configuration_loader import FileConfigurationLoader
from wg_federation.utils.utils import Utils


class TextFileConfigurationLoader(FileConfigurationLoader):
    """
    Read any configuration from signature files
    """

    def supports(self, source: Any) -> bool:
        return super().supports(source) and \
            Utils.has_extension(source, r'(digest|sha([0-9]{3})?|md5|sig|txt)')

    def _load_file(self, file: TextIO) -> dict:
        super()._load_file(file)
        return {file.name: file.read()}
