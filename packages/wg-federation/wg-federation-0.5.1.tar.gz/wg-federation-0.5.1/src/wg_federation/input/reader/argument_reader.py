import os
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter, RawTextHelpFormatter
from collections.abc import Sequence

from wg_federation.data.input.command_line.command_line_argument import CommandLineArgument
from wg_federation.data.input.command_line.command_line_option import CommandLineOption
from wg_federation.data.input.raw_options import RawOptions
from wg_federation.input.reader.environment_variable_reader import EnvironmentVariableReader


class Formatter(RawTextHelpFormatter, ArgumentDefaultsHelpFormatter):
    """ Argparse formatter combining linesep and defaults """


class ArgumentReader:
    """
    Read & manipulate command line arguments
    """

    _argument_parser: ArgumentParser
    _program_version: str

    def __init__(
            self,
            argument_parser: ArgumentParser,
            program_version: str,
    ):
        """
        Constructor
        :param argument_parser:
        :param program_version:
        """
        self._argument_parser = argument_parser
        self._program_version = program_version

    def parse_all(self) -> Namespace:
        """
        Parse all command line options and arguments
        :return: Command line arguments values
        """

        self._argument_parser.description = f"""
{self._argument_parser.prog} can be configured in three ways. By order of precedence, first is overridden by last:
  1. Configuration file
  2. Environment variables
  3. Command line options
  {(os.linesep + str(self._argument_parser.epilog) + os.linesep) if self._argument_parser.epilog is not None else ''}
environment variables:
  {(os.linesep + "  ").join(
            f"{EnvironmentVariableReader.get_real_env_var_name(option.name):30} {option.description}"
            for option in RawOptions.options
        )}
"""

        self._argument_parser.formatter_class = Formatter
        self._setup_general_options(self._argument_parser)

        self._setup_sub_parser(self._argument_parser, RawOptions.arguments)

        return self._argument_parser.parse_args()

    def _setup_sub_parser(
            self, _parent_argument_parser: ArgumentParser, _arguments: Sequence[CommandLineArgument], depth: int = 0
    ) -> None:
        subparser_action = _parent_argument_parser.add_subparsers(required=False, dest='arg' + str(depth))

        for argument in _arguments:
            parser = subparser_action.add_parser(
                argument.command,
                help=argument.description,
                formatter_class=ArgumentDefaultsHelpFormatter
            )
            self._setup_general_options(parser)
            if (isinstance(argument.options, Sequence)) and len(argument.options) != 0:
                for option in argument.options:
                    self.__add_argument(parser, option)
            if isinstance(argument.subcommands, Sequence) and len(argument.subcommands) != 0:
                self._setup_sub_parser(parser, argument.subcommands, depth + 1)

    def _setup_general_options(self, _parser: ArgumentParser) -> None:
        """
        Setup command line general options
        :param _parser:
        :return:
        """
        for option in RawOptions.options:
            self.__add_argument(_parser, option)

        _parser.add_argument(
            '-V',
            '--version',
            action='version',
            version=self._program_version,
            help='Shows the version number and exit.'
        )

    def __add_argument(self, parser: ArgumentParser, command_line_option: CommandLineOption) -> None:
        parser.add_argument(
            command_line_option.argument_short,
            command_line_option.argument_alias,
            dest=command_line_option.name,
            action=command_line_option.argparse_action.value,
            default=command_line_option.default,
            help=f'{command_line_option.description}',
        )
