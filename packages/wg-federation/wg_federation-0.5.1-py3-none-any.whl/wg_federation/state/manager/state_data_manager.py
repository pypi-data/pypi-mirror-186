from logging import Logger
from typing import Any

from wg_federation.crypto.wireguard_key_generator import WireguardKeyGenerator
from wg_federation.data.input.command_line.secret_retreival_method import SecretRetrievalMethod
from wg_federation.data.input.user_input import UserInput
from wg_federation.data.state.federation import Federation
from wg_federation.data.state.hq_state import HQState
from wg_federation.data.state.interface_kind import InterfaceKind
from wg_federation.data.state.wireguard_interface import WireguardInterface
from wg_federation.data_transformation.configuration_location_finder import ConfigurationLocationFinder
from wg_federation.data_transformation.loader.can_load_configuration_interface import CanLoadConfigurationInterface
from wg_federation.data_transformation.locker.configuration_locker import ConfigurationLocker
from wg_federation.data_transformation.saver.can_save_configuration_interface import CanSaveConfigurationInterface
from wg_federation.event.hq.hq_event import HQEvent
from wg_federation.exception.user.data.state_signature_cannot_be_verified import StateNotBootstrapped
from wg_federation.observer.event_dispatcher import EventDispatcher
from wg_federation.utils.utils import Utils


class StateDataManager:
    """
    Handles wg-federation HQState lifecycles: create, updates and reload form source of truth.
    """
    _configuration_location_finder: ConfigurationLocationFinder = None
    _configuration_loader: CanLoadConfigurationInterface = None
    _configuration_saver: CanSaveConfigurationInterface = None
    _configuration_locker: ConfigurationLocker = None
    _wireguard_key_generator: WireguardKeyGenerator = None
    _event_dispatcher: EventDispatcher = None
    _logger: Logger = None

    # pylint: disable=too-many-arguments
    def __init__(
            self,
            configuration_location_finder: ConfigurationLocationFinder,
            configuration_loader: CanLoadConfigurationInterface,
            configuration_saver: CanSaveConfigurationInterface,
            configuration_locker: ConfigurationLocker,
            wireguard_key_generator: WireguardKeyGenerator,
            event_dispatcher: EventDispatcher,
            logger: Logger
    ):
        """
        Constructor
        :param configuration_location_finder:
        :param configuration_loader:
        :param configuration_saver:
        :param configuration_locker:
        :param wireguard_key_generator:
        :param event_dispatcher:
        :param logger:
        """
        self._configuration_location_finder = configuration_location_finder
        self._configuration_loader = configuration_loader
        self._configuration_saver = configuration_saver
        self._configuration_locker = configuration_locker
        self._wireguard_key_generator = wireguard_key_generator
        self._event_dispatcher = event_dispatcher
        self._logger = logger

    def reload(self) -> HQState:
        """
        Loads a HQState from the source of truth.
        :return:
        """
        try:
            with self._configuration_locker.lock_shared(self._configuration_location_finder.state()) as conf_file:
                raw_configuration = self._reload_from_source(conf_file)

            return self._event_dispatcher.dispatch([HQEvent.STATE_LOADED], HQState(
                federation=Federation.from_dict(raw_configuration.get('federation')),
                interfaces=WireguardInterface.from_list(raw_configuration.get('interfaces')),
                forums=WireguardInterface.from_list(raw_configuration.get('forums')),
                phone_lines=WireguardInterface.from_list(raw_configuration.get('phone_lines')),
            ))
        except FileNotFoundError as err:
            raise StateNotBootstrapped('Unable to load the state: it was not bootstrapped. Run `hq boostrap`.') from err

    def create_hq_state(self, user_input: UserInput) -> HQState:
        """
        Create a new HQState and save it.
        This method disregard whether a state already exists. To use with precaution.
        :param: user_input
        :return:
        """
        state = self._generate_new_hq_state(user_input)

        with self._configuration_locker.lock_exclusively(self._configuration_location_finder.state()) as conf_file:
            self._configuration_saver.save(state.dict(), conf_file)

        self._event_dispatcher.dispatch([HQEvent.STATE_CREATED], state)

        return state

    def _reload_from_source(self, source: Any = None) -> dict:
        self._logger.debug(
            f'{Utils.classname(self)}: reloading configuration from {self._configuration_location_finder.state()}'
        )

        return self._configuration_loader.load_if_exists(source)

    def _generate_new_hq_state(self, user_input: UserInput) -> HQState:
        self.__check_passphrase_retrieval_method(user_input)

        forum_key_pairs = self._wireguard_key_generator.generate_key_pairs()
        phone_line_key_pairs = self._wireguard_key_generator.generate_key_pairs()
        interface_key_pairs = self._wireguard_key_generator.generate_key_pairs()
        federation = Federation(name='wg-federation0')

        return HQState(
            federation=federation,
            forums=(
                WireguardInterface(
                    name='wgf-forum0',
                    address=('172.32.0.1/22',),
                    private_key=forum_key_pairs[0],
                    public_key=forum_key_pairs[1],
                    shared_psk=self._wireguard_key_generator.generate_psk(),
                    listen_port=federation.forum_min_port,
                    private_key_retrieval_method=user_input.private_key_retrieval_method,
                    kind=InterfaceKind.FORUM,
                    post_up=self.__add_secret_retrieval_to_post_up(
                        (),
                        'forums',
                        'wgf-forum0',
                        user_input.private_key_retrieval_method,
                        user_input.root_passphrase_command
                    )
                ),
            ),
            phone_lines=(
                WireguardInterface(
                    name='wgf-phoneline0',
                    address=('172.32.4.1/22',),
                    private_key=phone_line_key_pairs[0],
                    public_key=phone_line_key_pairs[1],
                    shared_psk=self._wireguard_key_generator.generate_psk(),
                    listen_port=federation.phone_line_min_port,
                    private_key_retrieval_method=user_input.private_key_retrieval_method,
                    kind=InterfaceKind.PHONE_LINE,
                    post_up=self.__add_secret_retrieval_to_post_up(
                        (),
                        'phone_lines',
                        'wgf-phoneline0',
                        user_input.private_key_retrieval_method,
                        user_input.root_passphrase_command
                    )
                ),
            ),
            interfaces=(
                WireguardInterface(
                    name='wg-federation0',
                    address=('172.30.8.1/22',),
                    private_key=interface_key_pairs[0],
                    public_key=interface_key_pairs[1],
                    shared_psk=self._wireguard_key_generator.generate_psk(),
                    private_key_retrieval_method=user_input.private_key_retrieval_method,
                    kind=InterfaceKind.INTERFACE,
                    post_up=self.__add_secret_retrieval_to_post_up(
                        (),
                        'interfaces',
                        'wg-federation0',
                        user_input.private_key_retrieval_method,
                        user_input.root_passphrase_command
                    ),
                ),
            ),
        )

    def __check_passphrase_retrieval_method(self, user_input: UserInput) -> None:
        if self.__should_use_insecure_private_key(user_input.private_key_retrieval_method):
            self._logger.warning(
                f'The root passphrase retrieval method has been set to '
                f'“{SecretRetrievalMethod.TEST_INSECURE_CLEARTEXT.value}”. '
                f'This is insecure: any user able to read configuration files would be able to get the private keys. '
                f'This method is left for testing purpose but SHOULD NOT be used in production.'
            )

    def __add_secret_retrieval_to_post_up(
            self,
            post_up: tuple[str, ...],
            interface_type: str,
            interface_name: str,
            private_key_retrieval_method: SecretRetrievalMethod,
            root_passphrase_command: str,
    ) -> tuple[str, ...]:
        if not self.__should_use_insecure_private_key(private_key_retrieval_method):
            post_up += (f'wg set %i private-key <(wg-federation hq get-private-key '
                        f'--interface-type {interface_type} '
                        f'--interface-name {interface_name}'
                        f'{self.__get_root_passphrase(private_key_retrieval_method, root_passphrase_command)}'
                        f')',)

        return post_up

    def __get_root_passphrase(
            self, private_key_retrieval_method: SecretRetrievalMethod, root_passphrase_command: str
    ) -> str:
        if private_key_retrieval_method is SecretRetrievalMethod.WG_FEDERATION_COMMAND:
            return f' --root-passphrase-command "{root_passphrase_command}"'

        return ''

    def __should_use_insecure_private_key(self, private_key_retrieval_method: SecretRetrievalMethod) -> bool:
        return private_key_retrieval_method is SecretRetrievalMethod.TEST_INSECURE_CLEARTEXT
