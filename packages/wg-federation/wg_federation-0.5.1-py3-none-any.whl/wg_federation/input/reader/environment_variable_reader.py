import logging
import os
from typing import Union

from wg_federation.data.input.raw_options import RawOptions
from wg_federation.utils.utils import Utils


class EnvironmentVariableReader:
    """
    Read & manipulate OS environment variables
    """

    PREFIX = 'WG_FEDERATION_'

    _logger: logging.Logger

    def __init__(self, logger: logging.Logger):
        """
        Constructor
        :param logger:
        """
        self._logger = logger

    def fetch_all(self) -> dict:
        """
        Fetch all possible environment variables
        :return: Dict containing all normalized options names and their values
        """

        retrieved_options: dict = {}
        for env_var_suffix in RawOptions.get_all_options_names():
            retrieved_options[env_var_suffix] = self.read(env_var_suffix.upper())

        return retrieved_options

    def read(self, env_var_suffix: str) -> Union[str, None]:
        """
        Read an environment variable from the current system context.
        :param env_var_suffix: lowercase substance of the name of the environment variable to be read
        :return: the environment variable content
        """
        self._logger.debug(f'{Utils.classname(self)}: '
                           f'Trying to fetch “{self.get_real_env_var_name(env_var_suffix)}” environment variable.')

        if self.get_real_env_var_name(env_var_suffix) in os.environ:
            return os.getenv(self.get_real_env_var_name(env_var_suffix))

        return None

    @classmethod
    def get_real_env_var_name(cls, env_var_suffix: str) -> str:
        """
        Get a real environment variable name based on a suffix
        :param env_var_suffix: Environment variable suffix
        :return: full, real environment variable name
        """

        return cls.PREFIX + env_var_suffix.upper()

    @classmethod
    def get_all_options_env_var_names(cls) -> list[str]:
        """
        Returns all the possible option’s environment variables full names
        :return:
        """

        return list(map(cls.get_real_env_var_name, RawOptions.get_all_options_names()))
