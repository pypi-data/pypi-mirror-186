from typing import Callable, Optional

from ipaddr import IPNetwork
from pydantic import BaseModel, validator, Field
from typing_extensions import Annotated

from wg_federation.data.state.federation import Federation
from wg_federation.data.state.interface_kind import InterfaceKind
from wg_federation.data.state.wireguard_interface import WireguardInterface
from wg_federation.exception.developer.data.data_validation_error import DataValidationError


# mypy: ignore-errors
# https://github.com/pydantic/pydaOntic/issues/156


class HQState(BaseModel, frozen=True):
    """
    Data class representing a full HQ state
    Important: https://pydantic-docs.helpmanual.io/usage/models/#field-ordering
    """

    federation: Annotated[Federation, Field(
        ...,
        alias='federation',
        title='Federation',
        description='Federation data',
        true_type=Federation
    )]

    forums: Annotated[tuple[WireguardInterface, ...], Field(
        ...,
        alias='forums',
        title='Forums',
        description='WireGuard interfaces for untrusted communication between HQ and candidates',
        true_type=tuple[WireguardInterface, ...],
    )]

    phone_lines: Annotated[tuple[WireguardInterface, ...], Field(
        ...,
        alias='phone_lines',
        title='Phone Lines',
        description='WireGuard interfaces for trusted communication between HQ and members',
        true_type=tuple[WireguardInterface, ...],
    )]

    interfaces: Annotated[tuple[WireguardInterface, ...], Field(
        ...,
        alias='interfaces',
        title='Interfaces',
        description='WireGuard interfaces: Federation VPNs',
        true_type=tuple[WireguardInterface, ...],
    )]

    # pylint: disable=no-self-argument

    @validator('interfaces')
    def wireguard_interface_are_valid(
            cls, value: tuple[WireguardInterface, ...], values: dict
    ) -> tuple[str, WireguardInterface]:
        """
        Validate interfaces.
        Also checks forums and phone_lines.
        :param value: interfaces value
        :param values: other validated attributes of the current object as dict
        :return:
        """
        return cls._check_wireguard_connection(value, values)

    @classmethod
    def _check_wireguard_connection(
            cls, value: tuple[WireguardInterface, ...], values: dict
    ) -> tuple[str, WireguardInterface]:

        interface_names = []
        interface_addresses = []
        interface_listen_ports = []

        for wireguard_interface in (value + values.get('forums') + values.get('phone_lines')):
            if wireguard_interface.name in interface_names:
                raise ValueError(
                    f'The wireguard interface “{wireguard_interface.name}” has the same name of another interface.'
                )

            for address in wireguard_interface.address:
                for other_address in interface_addresses:
                    if IPNetwork(str(address)).overlaps(other_address):
                        raise ValueError(
                            f'The wireguard interface address “{wireguard_interface.name}”'
                            f' has an address “{address}” that overlaps with another address: “{other_address}”.'
                        )

                interface_addresses.append(IPNetwork(str(address)))

            if wireguard_interface.listen_port in interface_listen_ports:
                raise ValueError(
                    f'The wireguard interface “{wireguard_interface.name}” has the same listen_port'
                    f' “{wireguard_interface.listen_port}” as another interface.'
                )

            interface_names.append(wireguard_interface.name)
            interface_listen_ports.append(wireguard_interface.listen_port)

        cls._check_listen_port(
            value,
            'interface',
            lambda x: values.get('federation').port_within_forum_range(x) or values.get(
                'federation').port_within_phone_line_range(x)
        )

        cls._check_listen_port(
            values.get('forums'),
            'forum',
            lambda x: not values.get('federation').port_within_forum_range(x)
        )

        cls._check_listen_port(
            values.get('phone_lines'),
            'phone line',
            lambda x: not values.get('federation').port_within_phone_line_range(x)
        )

        return value

    @classmethod
    def _check_listen_port(
            cls,
            interfaces: tuple[WireguardInterface, ...],
            interface_type: str,
            callback: Callable
    ) -> None:
        for wireguard_interface in interfaces:
            if callback(wireguard_interface.listen_port):
                raise DataValidationError(
                    f'The wireguard {interface_type} “{wireguard_interface.name}”’s listen_port '
                    f'“{wireguard_interface.listen_port}” is invalid.'
                    f'Make sure the port is in the allowed range and not the same as another interface.'
                )

    def find_interface_by_name(self, kind: InterfaceKind, name: str) -> Optional[WireguardInterface]:
        """
        Search and return an interface by its name
        :param kind: Kind of interface to find
        :param name: Name of the interface to find
        :return:
        """
        for interface in self.find_interfaces_by_kind(kind):
            if interface.name == name:
                return interface

        return None

    def find_interfaces_by_kind(self, kind: InterfaceKind) -> tuple:
        """
        Return interfaces by their kind.
        :param kind:
        :return: tuple[WireguardInterface] or empty tuple if the kind is not found
        """
        if hasattr(self, kind):
            return getattr(self, kind)

        return ()
