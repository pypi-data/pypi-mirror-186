import os
from typing import NoReturn

from wg_federation.crypto.message_signer import MessageSigner
from wg_federation.data_transformation.configuration_location_finder import ConfigurationLocationFinder
from wg_federation.data_transformation.loader.can_load_configuration_interface import CanLoadConfigurationInterface
from wg_federation.exception.developer.data_transformation.invalid_data_error import InvalidDataError


class VerifySignatureConfigurationLoaderProxy(CanLoadConfigurationInterface):
    """
    CanLoadConfigurationInterface Proxy.
    Verifies the signature of the loaded configurations.
    """

    _configuration_location_finder: ConfigurationLocationFinder = None
    _configuration_loader: CanLoadConfigurationInterface = None
    _message_signer: MessageSigner = None
    _digest_configuration_loader: CanLoadConfigurationInterface = None

    def __init__(
            self,
            configuration_location_finder: ConfigurationLocationFinder,
            configuration_loader: CanLoadConfigurationInterface,
            message_signer: MessageSigner,
            digest_configuration_loader: CanLoadConfigurationInterface,
    ):
        """
        Constructor
        :param configuration_loader:
        :param message_signer:
        :param configuration_location_finder:
        """
        self._configuration_location_finder = configuration_location_finder
        self._configuration_loader = configuration_loader
        self._message_signer = message_signer
        self._digest_configuration_loader = digest_configuration_loader

    def load_if_exists(self, source: str, configuration_loader: type = None) -> dict:
        return self._verify_data(
            self._configuration_loader.load_if_exists(source, configuration_loader)
        )

    def load(self, source: str, configuration_loader: type = None) -> dict:
        return self._verify_data(
            self._configuration_loader.load(source, configuration_loader)
        )

    def load_all_if_exists(self, sources: tuple[str, ...]) -> dict:
        return self._verify_data(
            self._configuration_loader.load_all_if_exists(sources)
        )

    def load_all(self, sources: tuple[str, ...]) -> dict:
        return self._verify_data(
            self._configuration_loader.load_all(sources)
        )

    def _verify_data(self, data: dict) -> dict:
        self._message_signer.verify_sign(
            str(self._get_real_data(data)),
            self._get_data_nonce(data),
            self._get_data_digest(data),
        )

        return self._get_real_data(data)

    def _get_data_nonce(self, data: dict) -> str:
        if not data.get('nonce'):
            self.__raise_invalid_data_error(
                'A “nonce” was expected next to the data, but it was not found.'
            )

        return data.get('nonce')

    def _get_real_data(self, data: dict) -> dict:
        if not data.get('data'):
            self.__raise_invalid_data_error(
                '“data” key not found in the inputted dict.'
            )
        if not isinstance(data.get('data'), dict):
            self.__raise_invalid_data_error(
                f'Data is expected to be in a dict, but “{type(data.get("data"))}” was found instead.'
            )

        return data.get('data')

    # Because pylint can't parse properly:
    # pylint: disable=inconsistent-return-statements
    def _get_data_digest(self, data: dict) -> str:
        if self._configuration_location_finder.state_digest_belongs_to_state():
            if not data.get('digest'):
                self.__raise_invalid_data_error(
                    'A “digest” was expected next to the data, but it was not found.'
                )

            return data.get('digest')

        try:
            return str(
                list(
                    self._digest_configuration_loader.load(
                        self._configuration_location_finder.state_digest()
                    ).values()
                )[0]
            )
        except RuntimeError as error:
            self.__raise_invalid_data_error(
                f'Fail to load digest from “{self._configuration_location_finder.state_digest()}” '
                f'to verify data signature.'
                f'Original error: {error}'
            )

    def __raise_invalid_data_error(self, message: str) -> NoReturn:
        """
        :raise InvalidDataError
        """
        raise InvalidDataError(
            f'Fail to verify data signature.{os.linesep}{message}'
        )
