from enum import Enum
from typing import Optional

from wg_federation.data.state.federation import Federation
from wg_federation.data.state.hq_state import HQState
from wg_federation.data.state.wireguard_interface import WireguardInterface


class HQEvent(tuple[str, type, Optional[bool]], Enum):
    """
    HQ events
    """

    BOOTSTRAPPED = ('bootstrapped', HQState)

    FEDERATION_LOADED = ('federation_loaded', Federation)
    FEDERATION_CREATED = ('federation_created', Federation)
    FEDERATION_BEFORE_UPDATE = ('federation_before_update', Federation, True)
    FEDERATION_UPDATED = ('federation_updated', Federation)
    FEDERATION_BEFORE_DELETE = ('federation_before_delete', Federation)
    FEDERATION_DELETED = ('federation_before_delete', Federation)

    INTERFACE_CREATED = ('interface_created', WireguardInterface)
    INTERFACE_BEFORE_UPDATE = ('interface_updated', WireguardInterface, True)
    INTERFACE_UPDATED = ('interface_updated', WireguardInterface)
    INTERFACE_BEFORE_DELETE = ('interface_before_delete', WireguardInterface)
    INTERFACE_DELETED = ('interface_deleted', WireguardInterface)

    FORUM_INTERFACE_CREATED = ('forum_created', WireguardInterface)
    FORUM_INTERFACE_BEFORE_UPDATE = ('forum_before_update', WireguardInterface, True)
    FORUM_INTERFACE_UPDATE = ('forum_updated', WireguardInterface)
    FORUM_INTERFACE_BEFORE_DELETE = ('forum_before_delete', WireguardInterface)
    FORUM_INTERFACE_DELETED = ('forum_deleted', WireguardInterface)

    PHONE_LINE_INTERFACE_CREATED = ('phone_line_created', WireguardInterface)
    PHONE_LINE_INTERFACE_BEFORE_UPDATE = ('phone_line_before_update', WireguardInterface, True)
    PHONE_LINE_INTERFACE_UPDATED = ('phone_line_updated', WireguardInterface)
    PHONE_LINE_INTERFACE_BEFORE_DELETE = ('phone_line_before_delete', WireguardInterface)
    PHONE_LINE_INTERFACE_DELETED = ('phone_line_deleted', WireguardInterface)

    STATE_LOADED = ('state_loaded', HQState)
    STATE_CREATED = ('state_created', HQState)
    STATE_BEFORE_UPDATE = ('state_before_update', HQState, True)
    STATE_UPDATED = ('state_updated', HQState)
