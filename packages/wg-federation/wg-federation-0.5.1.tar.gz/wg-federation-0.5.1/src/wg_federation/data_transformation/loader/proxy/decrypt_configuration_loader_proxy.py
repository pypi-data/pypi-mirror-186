from collections.abc import MutableMapping
from typing import Any

from wg_federation.crypto.data.encrypted_message import EncryptedMessage
from wg_federation.crypto.message_encrypter import MessageEncrypter
from wg_federation.data_transformation.loader.can_load_configuration_interface import CanLoadConfigurationInterface
from wg_federation.utils.utils import Utils


class DecryptConfigurationLoaderProxy(CanLoadConfigurationInterface):
    """
    CanLoadConfigurationInterface Proxy.
    Decrypts an encrypted data from the loaded configurations.
    """
    _configuration_loader: CanLoadConfigurationInterface = None
    _message_encrypter: MessageEncrypter = None

    def __init__(self, configuration_loader: CanLoadConfigurationInterface, message_encrypter: MessageEncrypter):
        """
        Constructor
        :param configuration_loader:
        :param message_encrypter:
        """
        self._configuration_loader = configuration_loader
        self._message_encrypter = message_encrypter

    def load_if_exists(self, source: str, configuration_loader: type = None) -> dict:
        return dict(Utils.recursive_map(
            self._find_and_decrypt_secrets,
            self._configuration_loader.load_if_exists(source, configuration_loader)
        ))

    def load(self, source: str, configuration_loader: type = None) -> dict:
        return dict(Utils.recursive_map(
            self._find_and_decrypt_secrets,
            self._configuration_loader.load(source, configuration_loader)
        ))

    def load_all_if_exists(self, sources: tuple[str, ...]) -> dict:
        return dict(Utils.recursive_map(
            self._find_and_decrypt_secrets,
            self._configuration_loader.load_all_if_exists(sources)
        ))

    def load_all(self, sources: tuple[str, ...]) -> dict:
        return dict(Utils.recursive_map(
            self._find_and_decrypt_secrets,
            self._configuration_loader.load_all(sources)
        ))

    def _find_and_decrypt_secrets(self, value: Any) -> Any:
        """
        Converts value if it found to be a secret to an encrypted dict
        :param value:
        :return: dict with encrypted values if value is a secret, unmodified value otherwise
        """
        if self._contains_encrypted_message(value):
            return self._decrypt_message(value)

        return value

    def _contains_encrypted_message(self, value: Any) -> bool:
        return isinstance(value, MutableMapping) and 'ciphertext' in value.keys() and 'nonce' in value.keys()

    def _decrypt_message(self, message: dict[str, str]) -> str:
        return self._message_encrypter.decrypt(
            EncryptedMessage.from_hex(
                message.get('ciphertext'),
                message.get('digest'),
                message.get('nonce'),
            )
        ).decode('UTF-8')
