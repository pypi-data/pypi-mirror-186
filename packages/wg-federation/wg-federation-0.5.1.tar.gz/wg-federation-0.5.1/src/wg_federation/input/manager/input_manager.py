import logging
import os
import subprocess
from argparse import Namespace
from typing import Union

from pydantic import SecretStr

from wg_federation.data.input.raw_options import RawOptions
from wg_federation.data.input.user_input import UserInput
from wg_federation.input.reader.argument_reader import ArgumentReader
from wg_federation.input.reader.configuration_file_reader import ConfigurationFileReader
from wg_federation.input.reader.environment_variable_reader import EnvironmentVariableReader
from wg_federation.utils.utils import Utils


class InputManager:
    """
    Parse, validate and store all user inputs:
      1. command line arguments and options
      2. environment variables
      3. user configuration files
    """
    _argument_reader: ArgumentReader = None
    _environment_variable_reader: EnvironmentVariableReader = None
    _configuration_file_reader: ConfigurationFileReader = None
    _logger: logging.Logger = None

    def __init__(
            self,
            argument_reader: ArgumentReader,
            environment_variable_reader: EnvironmentVariableReader,
            configuration_file_reader: ConfigurationFileReader,
            logger: logging.Logger,
    ):
        """
        Constructor
        :param argument_reader:
        :param environment_variable_reader:
        :param configuration_file_reader:
        :param logger:
        """
        self._argument_reader = argument_reader
        self._environment_variable_reader = environment_variable_reader
        self._configuration_file_reader = configuration_file_reader
        self._logger = logger

    def parse_all(self) -> UserInput:
        """
        Parse all user inputs, from all possible sources: cmd arguments, env vars, configuration files
        :return: data object containing validated inputs
        """

        arguments = self._argument_reader.parse_all()
        self._logger.debug(f'{Utils.classname(self)}: Command line argument processed:{os.linesep}\t{arguments}')
        environment_variables = self._environment_variable_reader.fetch_all()
        self._logger.debug(
            f'{Utils.classname(self)}: Environment variables processed:{os.linesep}\t{environment_variables}'
        )
        configuration = self._configuration_file_reader.load_all()
        self._logger.debug(f'{Utils.classname(self)}: Loaded configuration processed:{os.linesep}\t{configuration}')

        user_input = UserInput(
            **dict((option_name, self._get_first_defined_user_input_value(
                option_name, arguments, environment_variables, configuration
            )) for option_name in self.__get_all_user_input_names())
        )

        user_input = self._process_root_passphrase_command(user_input)

        self._warn_if_secrets_are_in_configuration(user_input, configuration)

        self._logger.debug(f'{Utils.classname(self)}: Final processed user inputs:{os.linesep}\t{user_input}')

        return user_input

    def _process_root_passphrase_command(self, user_input: UserInput) -> UserInput:
        if user_input.root_passphrase_command:
            if user_input.root_passphrase:
                self._logger.warning(
                    'A root-passphrase-command was set but the root passphrase was retrieved through other means. '
                    'Ignoring the root passphrase command.'
                )
                return user_input

            command_result = subprocess.run(
                user_input.root_passphrase_command.split(' '),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                check=True
            )
            if command_result.returncode != 0:
                raise ChildProcessError(
                    f'The command to get the root passphrase '
                    f'({user_input.root_passphrase_command}) returned a non-zero status.'
                )

            user_input.root_passphrase = SecretStr(
                command_result.stdout.strip(os.linesep.encode('UTF-8')).decode('UTF-8')
            )

        return user_input

    def _warn_if_secrets_are_in_configuration(self, user_input: UserInput, configuration: dict):
        for attribute, value in user_input:
            if isinstance(value, SecretStr) and configuration.get(attribute):
                self._logger.warning(
                    f'The secret “{attribute}” was loaded from a configuration file. '
                    f'This secret might be readable by whomever access the disk or the configuration file. '
                    f'Consider using an environment variable, command line argument (`-h` for other options).'
                )

    @classmethod
    def _get_first_defined_user_input_value(
            cls, option_name: str, arguments: Namespace, environment_variables: dict[str, str], configuration: dict
    ) -> Union[type, object]:
        """
        Get the first user-defined option value for a specific option, among arguments, env vars or configuration files
        :param option_name: Option name to get
        :param arguments: User-defined options and arguments
        :param environment_variables: Environment variables defined in the context
        :param configuration: Configuration defined files in the system
        :return: option value or None when the option is not found or undefined
        """
        # type: ignore
        return getattr(arguments, option_name, None) or \
            environment_variables.get(option_name) or \
            configuration.get(option_name) or \
            Utils.extract_attributes(UserInput).get(option_name).get('default')  # type: ignore

    @classmethod
    def __get_all_user_input_names(cls):
        return (
            RawOptions.get_all_options_names() +
            RawOptions.get_all_argument_options_names(RawOptions.arguments) +
            RawOptions.get_all_argument_keys()
        )
