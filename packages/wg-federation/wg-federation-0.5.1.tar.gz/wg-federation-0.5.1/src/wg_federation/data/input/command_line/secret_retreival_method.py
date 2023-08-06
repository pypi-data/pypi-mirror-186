from enum import Enum


class SecretRetrievalMethod(str, Enum):
    """
    Enum of all possible secret retrieval methods.
    This helps configure tier application - like wg-quick - to instruct how it should get secrets.

    Note that methods may not be always available, depending on the secret to be retrieved.

    WG_FEDERATION_ENV_VAR_OR_FILE: Proxy through this program. Expect environment variable or file to contain root pass.
    WG_FEDERATION_COMMAND: Proxy through this program. Retrieve root passphrase through a provided command line.
    TEST_INSECURE_CLEARTEXT: Directly pass secrets, cleartext. Unsecure, only use for testing.

    Not implemented yet (here for future reference, helping determine what method could be implemented):
    WG_FEDERATION_DBUS: Proxy through a daemon started by this program. Use dbus and polkit for authentication.
    SYSTEMD_CREDS: Ask systemd-creds to retrieve secrets
    HASHICORP_VAULT: Ask Hashicorp vault to retrieve secrets
    …
    """

    WG_FEDERATION_ENV_VAR_OR_FILE = 'WG_FEDERATION_ENV_VAR_OR_FILE'
    WG_FEDERATION_COMMAND = 'WG_FEDERATION_COMMAND'

    TEST_INSECURE_CLEARTEXT = 'TEST_INSECURE_CLEARTEXT'
