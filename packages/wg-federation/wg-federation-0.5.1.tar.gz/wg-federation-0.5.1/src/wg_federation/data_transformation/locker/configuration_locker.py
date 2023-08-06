import logging
import os
from typing import Callable, ContextManager

from wg_federation.data_transformation.locker.can_lock_configuration_interface import CanLockConfigurationInterface
from wg_federation.data_transformation.locker.configuration_locker_interface import ConfigurationLockerInterface
from wg_federation.exception.developer.data_transformation.lock_unsupported_error import LockUnsupportedError
from wg_federation.utils.utils import Utils


class ConfigurationLocker(CanLockConfigurationInterface):
    """
    Lock any configuration from any sources
    """
    _configuration_lockers: tuple[ConfigurationLockerInterface, ...] = None
    _logger: logging.Logger = None

    def __init__(
            self,
            configuration_lockers: tuple[ConfigurationLockerInterface, ...],
            logger: logging.Logger,
    ):
        """
        Constructor
        :param configuration_lockers:
        :param logger:
        """
        self._configuration_lockers = tuple(configuration_lockers)
        self._logger = logger

    def lock_exclusively(self, location: str, configuration_locker: type = None) -> ContextManager:
        def lock(locker: ConfigurationLockerInterface, _location: str):
            return locker.obtain_exclusive_lock(_location)

        return self._do_lock(lock, location, configuration_locker)

    def lock_shared(self, location: str, configuration_locker: type = None) -> ContextManager:
        def lock(locker: ConfigurationLockerInterface, _location: str):
            return locker.obtain_shared_lock(_location)

        return self._do_lock(lock, location, configuration_locker)

    def _do_lock(self, lock: Callable, location: str, lock_classname: type = None) -> ContextManager:
        for _configuration_locker in self._configuration_lockers:
            if not lock_classname and _configuration_locker.is_default_for(location):
                self.__log_try_to_obtain_lock(location, Utils.classname(_configuration_locker))
                return lock(_configuration_locker, location)

            if lock_classname and isinstance(_configuration_locker, lock_classname):
                self.__log_try_to_obtain_lock(location, Utils.classname(_configuration_locker))
                return lock(_configuration_locker, location)

        if lock_classname:
            raise LockUnsupportedError(
                self.__get_lock_unsupported_message_error(
                    location,
                    f'Given classname “{str(lock_classname)}” does not implement a ConfigurationLockInterface '
                    f'or was not registered.'
                )
            )

        raise LockUnsupportedError(
            self.__get_lock_unsupported_message_error(
                location,
                f'No default ConfigurationLockInterface class for “{location}”.'
            )
        )

    def __log_try_to_obtain_lock(self, location: str, classname: str) -> None:
        self._logger.debug(
            f'Tried to obtain the lock for {location} using {classname}.'
        )

    def __get_lock_unsupported_message_error(self, location: str, follow_message: str) -> str:
        return f'Failed to lock “{location}”. {os.linesep}{follow_message}'
