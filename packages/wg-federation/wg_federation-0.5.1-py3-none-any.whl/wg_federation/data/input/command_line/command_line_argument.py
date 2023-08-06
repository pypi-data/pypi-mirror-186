from typing import Optional, MutableSequence

from pydantic import BaseModel

from wg_federation.data.input.command_line.command_line_option import CommandLineOption


class CommandLineArgument(BaseModel):
    """ Data class representing a command line argument """

    command: str = None
    description: str = None
    subcommands: Optional[MutableSequence['CommandLineArgument']] = None
    options: Optional[MutableSequence[CommandLineOption]] = None
