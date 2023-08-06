from enum import Enum


class InterfaceStatus(str, Enum):
    """
    Enum of possible network InterfaceStatus
    """
    ACTIVE = 'ACTIVE'  # System-installed, in-use and valid
    NEW = 'NEW'  # Not system-installed, not used and valid
    INACTIVE = 'INACTIVE'  # Not system-installed, not used, not valid
    DRAINING = 'DRAINING'  # System-installed, in-use and not valid
