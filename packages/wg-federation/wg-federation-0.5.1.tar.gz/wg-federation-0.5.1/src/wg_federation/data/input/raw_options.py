from collections.abc import Sequence
from typing import MutableSequence

from wg_federation.data.input.command_line.command_line_argument import CommandLineArgument
from wg_federation.data.input.command_line.command_line_option import CommandLineOption
from wg_federation.data.input.user_input import UserInput
from wg_federation.utils.utils import Utils


class RawOptions:
    """
    Contains metadata for all options, command line arguments, environment variables and options configuration stanzas.
    """

    options: list[str, CommandLineOption] = list(  # type: ignore
        (CommandLineOption.from_dict(option_name, option) for option_name, option in  # type: ignore
         Utils.extract_attributes(UserInput, ('category', 'general')).items())
    )

    arguments: list[CommandLineArgument] = [
        CommandLineArgument(
            command='hq',
            description='HQ commands',
            subcommands=[
                CommandLineArgument(
                    command='run',
                    description='Runs the HeadQuarter daemon.',
                ),
                CommandLineArgument(
                    command='bootstrap',
                    description='Bootstrap the HeadQuarter.',
                    options=list(
                        CommandLineOption.from_dict(option_name, option) for option_name, option in  # type: ignore
                        Utils.extract_attributes(UserInput, ('category', 'bootstrap')).items()
                    )
                ),
                CommandLineArgument(
                    command='get-private-key',
                    description='Fetch the private key of a given interface.',
                    options=list(
                        CommandLineOption.from_dict(option_name, option) for option_name, option in  # type: ignore
                        Utils.extract_attributes(UserInput, ('category', 'get-private-key')).items()
                    )
                ),
                CommandLineArgument(
                    command='add-interface',
                    description='Add a wireguard interface to the Federation.',
                ),
                CommandLineArgument(
                    command='remove-interface',
                    description='Remove a wireguard interface to the Federation.',
                ),
            ],
        )
    ]

    @classmethod
    def get_all_argument_options_names(
            cls, arguments: Sequence[CommandLineArgument], options: MutableSequence[str] = None
    ) -> Sequence[str]:
        """
        Gets all option names for a given list of CommandLineArgument.
        :param arguments:
        :param options: Used internally for recursive function, ignore this.
        :return:
        """
        if options is None:
            options = []

        for argument in arguments:
            if isinstance(argument.options, MutableSequence):
                for option in argument.options:
                    options.append(option.name)
            if argument.subcommands:
                cls.get_all_argument_options_names(argument.subcommands, options)

        return options

    @classmethod
    def get_all_options_names(cls) -> list[str]:
        """
        Returns all possible options names
        :return:
        """
        return list(map(lambda x: x.name, cls.options))

    @classmethod
    def get_argument_depth(cls, _arguments: Sequence[CommandLineArgument] = None, _depth_level: int = None) -> int:
        """
        Returns the maximum number of arguments that may be set
        :param _arguments:
        :param _depth_level: Starting depth level. Used internally for recursive function: user must ignore this.
        :return:
        """
        if not _depth_level:
            _depth_level = 1

        if _arguments is None:
            _arguments = cls.arguments

        if not _arguments:
            return 0

        for arguments in _arguments:
            if isinstance(arguments.subcommands, Sequence) and len(arguments.subcommands) != 0:
                return cls.get_argument_depth(arguments.subcommands, _depth_level + 1)

        return _depth_level

    @classmethod
    def get_all_argument_keys(cls) -> list[str]:
        """
        Returns all possible argument keys
        :return:
        """

        return list(map(lambda x: 'arg' + str(x), range(cls.get_argument_depth())))
