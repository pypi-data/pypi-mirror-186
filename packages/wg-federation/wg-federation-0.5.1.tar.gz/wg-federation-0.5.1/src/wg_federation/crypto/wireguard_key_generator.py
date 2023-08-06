import base64
from types import ModuleType


class WireguardKeyGenerator:
    """
    Generates WireGuard public/private keys and PSK.
    """

    _nacl_public_lib: ModuleType = None
    _cryptodome_random_lib: ModuleType = None

    def __init__(self, nacl_public_lib: ModuleType, cryptodome_random_lib: ModuleType):
        """
        Constructor
        :param nacl_public_lib:
        :param cryptodome_random_lib:
        """
        self._nacl_public_lib = nacl_public_lib
        self._cryptodome_random_lib = cryptodome_random_lib

    def generate_key_pairs(self) -> tuple[str, str]:
        """
        Generate X25519 ECDH private and public key
        :return: Tuple with base64 encoded private key and public key: (private, public)
        """

        key_pair = self._nacl_public_lib.PrivateKey(
            bytes(self._nacl_public_lib.PrivateKey.generate())
        )
        return (
            self.__convert_to_base64(bytes(key_pair)),
            self.__convert_to_base64(key_pair.public_key)
        )

    def generate_psk(self) -> str:
        """
        Generate a pre-shared key (PSK) for WireGuard.
        :return: base64 encoded pre-shared key
        """
        return self.__convert_to_base64(self._cryptodome_random_lib.get_random_bytes(32))

    def __convert_to_base64(self, key: bytes) -> str:
        return base64.b64encode(bytes(key)).decode('ascii')
