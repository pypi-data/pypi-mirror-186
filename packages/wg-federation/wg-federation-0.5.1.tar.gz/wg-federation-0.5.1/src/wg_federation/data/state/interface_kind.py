from enum import Enum


class InterfaceKind(str, Enum):
    """
    Enum of possible WireGuard interfaces kind
    """
    INTERFACE = 'interfaces'  # Federation interface
    PHONE_LINE = 'phone_lines'  # For HQ/Member meta communications
    FORUM = 'forums'  # For HQ/Candidate meta communications
