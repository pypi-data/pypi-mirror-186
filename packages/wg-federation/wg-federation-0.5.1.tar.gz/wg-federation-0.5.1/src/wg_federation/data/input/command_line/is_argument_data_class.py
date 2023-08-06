from abc import ABCMeta

from pydantic import BaseModel


class IsArgumentDataClass(BaseModel, metaclass=ABCMeta):
    """ Interface representing any Argument-specific user inputs """
