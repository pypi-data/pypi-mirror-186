from enum import Enum
from typing import Optional

from wg_federation.data.input.user_input import UserInput


class ControllerEvents(tuple[str, type, Optional[bool]], Enum):
    """
    Controller events
    """

    CONTROLLER_BASELINE = ('controller_baseline', UserInput)
    CONTROLLER_MAIN = ('controller_main', UserInput)
    CONTROLLER_LATE = ('controller_late', UserInput)
