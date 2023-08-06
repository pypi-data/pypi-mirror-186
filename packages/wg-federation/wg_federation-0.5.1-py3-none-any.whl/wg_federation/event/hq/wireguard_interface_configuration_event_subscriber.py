import configparser
import stat
from collections.abc import Mapping
from enum import Enum
from types import ModuleType

from wg_federation.data.state.hq_state import HQState
from wg_federation.data.state.interface_kind import InterfaceKind
from wg_federation.data.state.wireguard_interface import WireguardInterface
from wg_federation.data_transformation.configuration_location_finder import ConfigurationLocationFinder
from wg_federation.data_transformation.locker.configuration_locker import ConfigurationLocker
from wg_federation.event.hq.hq_event import HQEvent
from wg_federation.observer.event_subscriber import EventSubscriber
from wg_federation.utils.utils import Utils


class WireguardInterfaceConfigurationEventSubscribe(EventSubscriber[HQState]):
    """ Creates/Updates WireGuard interfaces """

    _os_lib: ModuleType = None
    _configuration_location_finder: ConfigurationLocationFinder = None
    _configuration_locker: ConfigurationLocker = None

    def __init__(
            self,
            os_lib: ModuleType,
            configuration_location_finder: ConfigurationLocationFinder,
            configuration_locker: ConfigurationLocker,
    ):
        """ Constructor """
        self._os_lib = os_lib
        self._configuration_location_finder = configuration_location_finder
        self._configuration_locker = configuration_locker

    def get_subscribed_events(self) -> list[Enum]:
        return [HQEvent.STATE_CREATED, HQEvent.STATE_UPDATED]

    def run(self, data: HQState) -> HQState:
        for interface in data.interfaces + data.phone_lines + data.forums:
            with self._configuration_locker.lock_exclusively(self.__get_wireguard_configuration_path(interface)):
                self.__prepare_ini_file(interface)

        return data

    def __prepare_ini_file(self, interface: WireguardInterface) -> None:
        self.__empty_wireguard_configuration(interface)

        config = configparser.ConfigParser(interpolation=None)

        for section, options in interface.into_wireguard_ini().items():
            if isinstance(options, Mapping):
                config.add_section(section)

                for option_name, option_value in options.items():
                    config[section][option_name] = str(option_value)

                self.__write_wireguard_configuration(interface, config)

    def __empty_wireguard_configuration(self, interface: WireguardInterface) -> None:
        Utils.open(self.__get_wireguard_configuration_path(interface), 'w', 'UTF-8')

    def __write_wireguard_configuration(self, interface: WireguardInterface, config: configparser.ConfigParser) -> None:
        with Utils.open(self.__get_wireguard_configuration_path(interface), 'a++', 'UTF-8') as wg_config:
            config.write(wg_config)

        self._os_lib.chmod(self.__get_wireguard_configuration_path(interface), stat.S_IREAD | stat.S_IWRITE)

    def __get_wireguard_configuration_path(self, interface: WireguardInterface) -> str:
        if InterfaceKind.INTERFACE == interface.kind:
            return self.__real_path(self._configuration_location_finder.interfaces_directory(), interface.name)

        if InterfaceKind.PHONE_LINE == interface.kind:
            return self.__real_path(self._configuration_location_finder.phone_lines_directory(), interface.name)

        return self.__real_path(self._configuration_location_finder.forums_directory(), interface.name)

    def __real_path(self, directory: str, interface_name: str) -> str:
        return self._os_lib.path.join(directory, f'{interface_name}.conf')
