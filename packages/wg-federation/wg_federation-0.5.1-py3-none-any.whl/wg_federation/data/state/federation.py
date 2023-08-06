from typing import Any

from pydantic import BaseModel, constr, conint, validator

from wg_federation.exception.developer.data.data_validation_error import DataValidationError


# mypy: ignore-errors
# https://github.com/pydantic/pydantic/issues/156


class Federation(BaseModel, frozen=True):
    """
    Data class representing a federation configuration file
    Important: https://pydantic-docs.helpmanual.io/usage/models/#field-ordering
    """

    _FEDERATION_NAME = r'^[A-Za-z0-9_\-]{1,64}$'

    name: constr(regex=_FEDERATION_NAME)
    forum_max_port: conint(ge=1010, le=65535) = 44299
    forum_min_port: conint(ge=1000, le=65525) = 44200
    phone_line_max_port: conint(ge=1010, le=65535) = 44199
    phone_line_min_port: conint(ge=1000, le=65525) = 44100

    # pylint: disable=no-self-argument
    @validator('phone_line_min_port')
    def check_phone_line_port(cls, value: int, values: dict) -> int:
        """
        Validate phone_line_min_port and phone_line_max_port
        :param value: phone_line_min_port value
        :param values: other validated attributes of the current object as dict
        :return:
        """
        if values.get('phone_line_max_port') is not None:
            cls.__check_port_range('phone line', values.get('phone_line_max_port'), value)

        return value

    # pylint: disable=no-self-argument

    @validator('forum_min_port')
    def check_forum_min_port(cls, value: int, values: dict) -> int:
        """
        Validate forum_min_port and forum_max_port
        :param value: forum_min_port value
        :param values: other validated attributes of the current object as dict
        :return:
        """
        if values.get('forum_max_port') is not None:
            cls.__check_port_range('forum', values.get('forum_max_port'), value)

        return value

    def port_within_phone_line_range(self, port: int) -> bool:
        """
        Check whether a given port is within the phone line ports range.
        :param port: Port to check
        :return: True if port is within range, false otherwise
        """
        return self.phone_line_max_port >= port >= self.phone_line_min_port

    def port_within_forum_range(self, port: int) -> bool:
        """
        Check whether a given port is within the forum ports range.
        :param port: Port to check
        :return: True if port is within range, false otherwise
        """
        return self.forum_max_port >= port >= self.forum_min_port

    @classmethod
    def from_dict(cls, configuration: dict[str, Any]) -> 'Federation':
        """
        Create a new Federation from a dict of key/values.
        :param configuration:
        :return: Federation
        """
        return cls(**configuration)

    @classmethod
    def __check_port_range(cls, field: str, max_port: int, min_port: int) -> None:
        if max_port - min_port < 10:
            raise DataValidationError(
                f'The federation {field} port ranges must be at minimum 10, to insure potential {field} rotation.'
                f' Port range given: “{min_port}” to “{max_port}”.'
            )
        if max_port - min_port > 100:
            raise DataValidationError(
                f'The federation {field} port ranges must be at maximum 100 to avoid reserving too much ports. '
                f' Port range given: “{min_port}” to “{max_port}”.'
            )
