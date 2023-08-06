from typing import Any

from wg_federation.crypto.message_signer import MessageSigner
from wg_federation.data_transformation.configuration_location_finder import ConfigurationLocationFinder
from wg_federation.data_transformation.saver.can_save_configuration_interface import CanSaveConfigurationInterface


class SignConfigurationSaverProxy(CanSaveConfigurationInterface):
    """
    CanSaveConfigurationInterface Proxy.
    Able to sign configuration ready to be saved.
    """

    _configuration_location_finder: ConfigurationLocationFinder = None
    _configuration_saver: CanSaveConfigurationInterface = None
    _message_signer: MessageSigner = None
    _digest_configuration_saver: CanSaveConfigurationInterface = None

    def __init__(
            self,
            configuration_location_finder: ConfigurationLocationFinder,
            configuration_saver: CanSaveConfigurationInterface,
            message_signer: MessageSigner,
            digest_configuration_saver: CanSaveConfigurationInterface,
    ):
        """
        Constructor
        :param configuration_location_finder:
        :param configuration_saver:
        :param message_signer:
        :param digest_configuration_saver:
        """
        self._configuration_location_finder = configuration_location_finder
        self._message_signer = message_signer
        self._configuration_saver = configuration_saver
        self._digest_configuration_saver = digest_configuration_saver

    def save_try(self, data: dict, destination: Any, configuration_saver: type = None) -> None:
        self._configuration_saver.save_try(self._sign(data), destination, configuration_saver)

    def save(self, data: dict, destination: Any, configuration_saver: type = None) -> None:
        self._configuration_saver.save(self._sign(data), destination, configuration_saver)

    def _sign(self, data: dict) -> dict:
        mac, nonce = self._message_signer.sign(str(data))

        data = {'data': data, 'nonce': nonce}

        if self._configuration_location_finder.state_digest_belongs_to_state():
            data['digest'] = mac
        else:
            self._digest_configuration_saver.save({'digest': mac}, self._configuration_location_finder.state_digest())

        return data
