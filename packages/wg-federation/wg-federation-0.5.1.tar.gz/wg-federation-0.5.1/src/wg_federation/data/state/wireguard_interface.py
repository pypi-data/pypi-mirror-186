import re
from typing import Any

from pydantic import BaseModel, IPvAnyAddress, conint, constr, IPvAnyInterface, SecretStr, validator

from wg_federation.data.input.command_line.secret_retreival_method import SecretRetrievalMethod
from wg_federation.data.state.interface_kind import InterfaceKind
from wg_federation.data.state.interface_status import InterfaceStatus
from wg_federation.exception.developer.data.data_validation_error import DataValidationError


# mypy: ignore-errors
# https://github.com/pydantic/pydantic/issues/156


class WireguardInterface(BaseModel, frozen=True):
    """
    Data class representing a WireGuard interface
    """

    _REGEXP_WIREGUARD_KEY = r'^[0-9A-Za-z+/]{43}[=]$'
    _REGEXP_WIREGUARD_INTERFACE_NAME = r'^[a-zA-Z0-9_=+-]{1,15}$'

    address: tuple[IPvAnyInterface, ...] = ('10.10.100.1/24',)
    listen_port: conint(le=65535) = 35200
    public_key: constr(regex=_REGEXP_WIREGUARD_KEY)
    private_key: SecretStr = None
    mtu: conint(ge=68, le=65535) = None
    dns: tuple[IPvAnyAddress, ...] = ()
    post_up: tuple[str, ...] = ()

    name: constr(regex=_REGEXP_WIREGUARD_INTERFACE_NAME) = 'wg-federation0'
    status: InterfaceStatus = InterfaceStatus.NEW
    kind: InterfaceKind = None
    private_key_retrieval_method: SecretRetrievalMethod = None
    shared_psk: SecretStr = None

    # pylint: disable=no-self-argument
    @validator('private_key')
    def check_private_key(cls, value: SecretStr, values: dict) -> SecretStr:
        """
        Validate private_key
        :param value: private_key value
        :param values: rest of the current object’s attributes
        :return:
        """
        return cls._check_wireguard_key(value, values, 'private_key')

    # pylint: disable=no-self-argument
    @validator('shared_psk')
    def check_shared_psk(cls, value: SecretStr, values: dict) -> SecretStr:
        """
        Validate psk.
        Also validate psk, public_key and private_key relation together.
        :param value: psk value
        :param values: rest of the current object’s attributes
        :return:
        """
        cls._check_wireguard_key(value, values, 'psk')

        cls._check_public_private_and_psk(
            values.get('public_key'),
            values.get('private_key').get_secret_value(),
            value.get_secret_value(),
            values.get('name')
        )

        return value

    @classmethod
    def from_dict(cls, configuration: dict[str, Any]) -> 'WireguardInterface':
        """
        Create a new WireguardInterface from a dict of key/values.
        :param configuration:
        :return: WireguardInterface
        """
        return cls(**configuration)

    @classmethod
    def from_list(cls, configurations: list[dict[str, Any]]) -> tuple['WireguardInterface', ...]:
        """
        Instantiate a tuple of WireguardInterface using a list of dict of keys/values
        :param configurations:
        :return: tuple of WireguardInterface
        """
        return tuple(map(cls.from_dict, configurations))

    def into_wireguard_ini(self) -> dict:
        """
        Transform the current object into a dict specifically made for WireGuard configuration files
        :return:
        """

        # While this is manual and inconvenient, unfruitful research was done:
        # - Use pydentic aliases for keys: buggy, mess with IDE static analysis
        # - Using configparse: wireguard needs duplicated section, not handled by configparser
        # - Using toml: wireguard configuration is not toml compliant
        return {
            'Interface': self.copy(
                include={},
                update={
                    'Address': ', '.join(str(address) for address in self.address),
                    'ListenPort': self.listen_port,
                    # pylint: disable=line-too-long
                    'PrivateKey': self.private_key.get_secret_value() if self.private_key and self.private_key_retrieval_method == SecretRetrievalMethod.TEST_INSECURE_CLEARTEXT else None,
                    'MTU': self.mtu,
                    'DNS': ', '.join(str(dns) for dns in self.dns) if len(self.dns) > 0 else None,
                    'PostUp': '; '.join(command for command in self.post_up) if len(self.post_up) > 0 else None,
                }).dict(exclude_none=True, )
        }

    @classmethod
    def _check_wireguard_key(cls, value: SecretStr, values: dict, kind: str) -> SecretStr:
        if not re.match(cls._REGEXP_WIREGUARD_KEY, value.get_secret_value()):
            raise DataValidationError(f'The interface named “{values.get("name")}” was provided an invalid {kind}.')

        return value

    @classmethod
    def _check_public_private_and_psk(cls, public_key: str, private_key: str, psk: str, interface_name: str) -> None:
        if len({public_key}.union({private_key}).union({psk})) != 3:
            raise DataValidationError(
                f'The interface named “{interface_name}”'
                f'private key, public key and psk must be different from each others.'
            )
