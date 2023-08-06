from typing import Any

from pydantic import BaseModel

from wg_federation.data.input.command_line.argparse_action import ArgparseAction


class CommandLineOption(BaseModel):
    """ Data class representing a command line option """

    argparse_action: ArgparseAction = ArgparseAction.STORE
    argument_alias: str = None
    argument_short: str = None
    default: Any = None
    description: str = None
    name: str

    @staticmethod
    def from_dict(name: str, source: dict[str, Any]) -> 'CommandLineOption':
        """
        Creates a new CommandLineOption from a dict source
        :param name:
        :param source:
        :return:
        """
        return CommandLineOption(
            argparse_action=source.get('argparse_action'),
            argument_alias=f'--{name.replace("_", "-")}',
            argument_short=source.get('argument_short'),
            default=source.get('default'),
            description=source.get('description'),
            name=name,
        )
