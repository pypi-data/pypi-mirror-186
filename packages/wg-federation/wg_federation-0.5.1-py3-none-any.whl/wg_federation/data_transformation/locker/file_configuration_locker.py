from __future__ import annotations

from contextlib import contextmanager, _GeneratorContextManager
from types import ModuleType

import portalocker

from wg_federation.data_transformation.locker.configuration_locker_interface import ConfigurationLockerInterface


class FileConfigurationLocker(ConfigurationLockerInterface):
    """
    Locks a file
    """

    _file_locker: ModuleType = None
    _path_lib: ModuleType = None

    def __init__(self, file_locker: ModuleType, path_lib: ModuleType) -> None:
        self._file_locker = file_locker
        self._path_lib = path_lib

    def obtain_exclusive_lock(self, location: str) -> _GeneratorContextManager:
        return self._do_lock(
            location,
            'a+',
            self._file_locker.LockFlags.NON_BLOCKING | self._file_locker.LockFlags.EXCLUSIVE
        )

    def obtain_shared_lock(self, location: str) -> _GeneratorContextManager:
        return self._do_lock(
            location,
            'r+',
            self._file_locker.LockFlags.NON_BLOCKING | self._file_locker.LockFlags.SHARED
        )

    def is_default_for(self, location: str) -> bool:
        return self._path_lib.Path(location).parent.is_dir()

    @contextmanager
    def _do_lock(self, location: str, mode: str, flags: portalocker.LockFlags):
        with self._file_locker.Lock(
                location,
                mode,
                timeout=5,
                flags=flags
        ) as file:
            yield file
