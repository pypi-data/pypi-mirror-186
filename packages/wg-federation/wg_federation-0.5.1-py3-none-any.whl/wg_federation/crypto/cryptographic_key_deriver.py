import functools
from functools import _CacheInfo

from Cryptodome import Random
from Cryptodome.Hash import SHA512
from Cryptodome.Protocol import KDF
from pydantic import SecretStr

from wg_federation.data.input.user_input import UserInput
from wg_federation.data_transformation.configuration_location_finder import ConfigurationLocationFinder
from wg_federation.data_transformation.loader.configuration_loader import ConfigurationLoader
from wg_federation.data_transformation.saver.configuration_saver import ConfigurationSaver
from wg_federation.exception.developer.crypto.root_passphrase_not_set import RootPassphraseNotSet


class CryptographicKeyDeriver:
    """
    Able to derive cryptographic keys.
    """

    _user_input: UserInput = None
    _configuration_location_finder: ConfigurationLocationFinder = None
    _configuration_loader: ConfigurationLoader = None
    _configuration_saver: ConfigurationSaver = None
    _cryptodome_random_lib: Random = None

    # pylint: disable=too-many-arguments
    def __init__(
            self,
            user_input: UserInput,
            configuration_location_finder: ConfigurationLocationFinder,
            configuration_loader: ConfigurationLoader,
            configuration_saver: ConfigurationSaver,
            cryptodome_random_lib: Random,
    ):
        """
        Constructor
        :param user_input:
        :param configuration_location_finder:
        :param configuration_loader:
        :param configuration_saver:
        :param cryptodome_random_lib:
        """
        self._user_input = user_input
        self._configuration_location_finder = configuration_location_finder
        self._configuration_loader = configuration_loader
        self._configuration_saver = configuration_saver
        self._cryptodome_random_lib = cryptodome_random_lib

    @functools.lru_cache(maxsize=8, typed=False)
    def derive_32b_key_from_root_passphrase(self) -> bytes:
        """
        Derive a 32byte cryptographic key from the current root passphrase.
        As deriving a key can impact performance, the result of this function is cached.
        :return: 32b key
        """
        return KDF.PBKDF2(
            password=self._get_root_passphrase(),
            salt=self._get_salt().encode('UTF-8'),
            dkLen=32,
            count=1111,
            hmac_hash_module=SHA512
        )

    def clear_cache(self) -> None:
        """
        Clear the cache for all this class’s functions
        :return: None
        """
        self.derive_32b_key_from_root_passphrase.cache_clear()

    def get_cache_status(self) -> _CacheInfo:
        """
        Return cache information
        :return: CacheInfo
        """
        return self.derive_32b_key_from_root_passphrase.cache_info()

    def create_salt(self) -> None:
        """
        Create salt.
        Careful, calling this function after any bootstrapping will invalidate the state.
        :return:
        """
        self._configuration_saver.save(
            {'raw': self._cryptodome_random_lib.get_random_bytes(32)},
            self._configuration_location_finder.salt()
        )

    def _get_salt(self) -> str:
        return list(
            self._configuration_loader.load(self._configuration_location_finder.salt()).values()
        )[0]

    def _get_root_passphrase(self) -> str:
        if not isinstance(self._user_input.root_passphrase, SecretStr) or \
                not self._user_input.root_passphrase.get_secret_value():
            raise RootPassphraseNotSet(
                'Cannot derive cryptographic key. The root passphrase was not set.'
            )

        return self._user_input.root_passphrase.get_secret_value()
