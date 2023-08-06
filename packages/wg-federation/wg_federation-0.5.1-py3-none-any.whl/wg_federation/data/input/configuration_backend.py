from enum import Enum


class ConfigurationBackend(str, Enum):
    """
    Enum of possible ConfigurationBackend
    """
    FILE = 'FILE'
    DEFAULT = 'DEFAULT'
