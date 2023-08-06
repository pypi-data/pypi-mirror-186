from typing import Any

from pydantic import SecretStr

from wg_federation.crypto.message_encrypter import MessageEncrypter
from wg_federation.data_transformation.saver.can_save_configuration_interface import CanSaveConfigurationInterface
from wg_federation.utils.utils import Utils


class EncryptConfigurationSaverProxy(CanSaveConfigurationInterface):
    """
    CanSaveConfigurationInterface Proxy.
    Able to encrypt plaintext configuration ready to be saved.
    """
    _configuration_saver: CanSaveConfigurationInterface = None
    _message_encrypter: MessageEncrypter = None

    def __init__(self, configuration_saver: CanSaveConfigurationInterface, message_encrypter: MessageEncrypter):
        """
        Constructor
        :param configuration_saver:
        :param message_encrypter:
        """
        self._configuration_saver = configuration_saver
        self._message_encrypter = message_encrypter

    def save_try(self, data: dict, destination: Any, configuration_saver: type = None) -> None:
        self._configuration_saver.save_try(
            dict(Utils.recursive_map(self._find_and_encrypt_secrets, data)),
            destination,
            configuration_saver
        )

    def save(self, data: dict, destination: Any, configuration_saver: type = None) -> None:
        self._configuration_saver.save(
            dict(Utils.recursive_map(self._find_and_encrypt_secrets, data)),
            destination,
            configuration_saver
        )

    def _find_and_encrypt_secrets(self, value: Any) -> Any:
        """
        Decrypt value if it is found to be a secret
        :param data:
        :return:
        """
        if isinstance(value, SecretStr):
            return self._encrypt_secret(value)

        return value

    def _encrypt_secret(self, message: SecretStr) -> dict:
        return self._message_encrypter.encrypt(message.get_secret_value().encode('UTF-8')).hex_dict()
