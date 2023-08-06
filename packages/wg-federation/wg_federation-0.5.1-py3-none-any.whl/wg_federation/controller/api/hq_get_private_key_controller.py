from enum import Enum

from wg_federation.controller.controller_events import ControllerEvents
from wg_federation.data.input.user_input import UserInput
from wg_federation.observer.event_subscriber import EventSubscriber
from wg_federation.state.manager.state_data_manager import StateDataManager


class HQGetPrivateKeyController(EventSubscriber[UserInput]):
    """
    Get the PrivateKey of given WireGuard interfaces.
    """

    _state_data_manager: StateDataManager = None

    def __init__(
            self,
            state_data_manager: StateDataManager,
    ):
        """
        Constructor
        :param state_data_manager:
        """
        self._state_data_manager = state_data_manager

    def get_subscribed_events(self) -> list[Enum]:
        return [ControllerEvents.CONTROLLER_MAIN]

    def should_run(self, data: UserInput) -> bool:
        return data.arg0 == 'hq' and data.arg1 == 'get-private-key'

    def run(self, data: UserInput) -> UserInput:
        hq_state = self._state_data_manager.reload()

        interface = hq_state.find_interface_by_name(data.interface_kind, data.interface_name)

        if not interface:
            return data

        print(interface.private_key.get_secret_value())

        return data
