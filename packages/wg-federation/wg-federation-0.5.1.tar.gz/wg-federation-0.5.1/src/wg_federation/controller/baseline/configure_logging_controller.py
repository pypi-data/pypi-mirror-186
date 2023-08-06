import logging
from enum import Enum

from wg_federation.controller.controller_events import ControllerEvents
from wg_federation.data.input.user_input import UserInput
from wg_federation.observer.event_subscriber import EventSubscriber


class ConfigureLoggingController(EventSubscriber[UserInput]):
    """
    Configure the application logging
    For example, logging level depending on user inputs

    Note: this code can be run quite late during the flow of the program.
    To enable debug sooner, see the dependency injection Container class.
    """
    _logger_handler: logging.Handler = None
    _logger: logging.Logger = None

    def __init__(self, logger_handler: logging.Handler, logger: logging.Logger):
        """
        Constructor
        :param logger_handler:
        :param logger:
        """
        self._logger_handler = logger_handler
        self._logger = logger

    def get_subscribed_events(self) -> list[Enum]:
        return [ControllerEvents.CONTROLLER_BASELINE]

    def run(self, data: UserInput) -> UserInput:
        if data.quiet:
            logging.disable()
            return data

        # This is a mask (as in POSIX permission mask): the Handler object sets the real logging level.
        self._logger.setLevel(logging.DEBUG)
        self._logger_handler.setLevel(logging.getLevelName(data.log_level))

        if data.verbose:
            self._logger_handler.setLevel(logging.INFO)

        if data.debug:
            self._logger_handler.setLevel(logging.DEBUG)

        return data
