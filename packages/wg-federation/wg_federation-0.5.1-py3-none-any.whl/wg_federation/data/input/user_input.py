from pydantic import BaseModel, validator, SecretStr, Field
from typing_extensions import Annotated

from wg_federation.data.input.command_line.argparse_action import ArgparseAction
from wg_federation.data.input.command_line.secret_retreival_method import SecretRetrievalMethod
from wg_federation.data.input.configuration_backend import ConfigurationBackend
from wg_federation.data.input.log_level import LogLevel
from wg_federation.data.state.interface_kind import InterfaceKind
from wg_federation.exception.developer.data.data_validation_error import DataValidationError


class UserInput(BaseModel):
    """
    Data class containing all user inputs
    """
    # general

    verbose: Annotated[bool, Field(
        title='Verbose',
        description='Enables “verbose” mode, displaying INFO logs in the standard output.',
        type=bool,
        true_type=bool,
        argparse_action=ArgparseAction.STORE_TRUE,
        argument_short='-v',
        category='general',
    )] = False

    debug: Annotated[bool, Field(
        title='Debug',
        description='Enables “debug” mode, displaying DEBUG logs in the standard output.',
        type=bool,
        true_type=bool,
        argparse_action=ArgparseAction.STORE_TRUE,
        argument_short='--vv',
        category='general',
    )] = False

    quiet: Annotated[bool, Field(
        title='Debug',
        description='Prevents any logs to appear in the standard output, regardless of other logging options',
        type=bool,
        true_type=bool,
        argparse_action=ArgparseAction.STORE_TRUE,
        argument_short='-q',
        category='general',
    )] = False

    log_level: Annotated[LogLevel, Field(
        title='Log Level',
        description='Sets the maximum criticality for logs to appear in the standard output.',
        type=LogLevel,
        allowed=f'“{"”, “".join([e.value for e in LogLevel])}”',
        true_type=LogLevel,
        argparse_action=ArgparseAction.STORE,
        argument_short='-l',
        category='general',
    )] = LogLevel.INFO

    root_passphrase: Annotated[SecretStr, Field(
        title='Root Passphrase',
        description='Sets the root passphrase used encrypt and decrypt all secrets managed by this program. '
                    'To avoid logging the passphrase, don’t this option with a cleartext value. ',
        type=SecretStr,
        true_type=SecretStr,
        argparse_action=ArgparseAction.STORE,
        argument_short='-P',
        category='general',
    )] = None

    root_passphrase_command: Annotated[str, Field(
        title='Root Passphrase Retrieval Command',
        description='Sets the process command that will be called to get the root passphrase. '
                    'This option conflicts with --root-passphrase. '
                    'When both options are set, `--root-passphrase` takes precedence over `--root-passphrase-command`. '
                    'This option can be useful in combination with `--private-key-retrieval-method`, for wg-quick to '
                    'dynamically fetch private keys, thus preventing cleartext secrets in configuration files. '
                    'Use with caution: this option will spawn a subprocess and could be exploited for shell injection.',
        type=str,
        true_type=str,
        argparse_action=ArgparseAction.STORE,
        argument_short='--Pcmd',
        category='general',
    )] = None

    state_backend: Annotated[ConfigurationBackend, Field(
        title='State Backend',
        description='Sets the backend to use to store this program’s state. ',
        type=ConfigurationBackend,
        allowed=f'“{"”, “".join([e.value for e in ConfigurationBackend])}”',
        true_type=ConfigurationBackend,
        argparse_action=ArgparseAction.STORE,
        argument_short='--sb',
        category='general',
    )] = ConfigurationBackend.FILE

    state_digest_backend: Annotated[ConfigurationBackend, Field(
        title='State Digest Backend',
        description='Sets the backend to use to store the digest of this program’s state. '
                    f'When set to “{ConfigurationBackend.DEFAULT.value}”, '
                    'the state digest will be merge with the state, according to `--state-backend`.',
        type=ConfigurationBackend,
        allowed=f'“{"”, “".join([e.value for e in ConfigurationBackend])}”',
        true_type=ConfigurationBackend,
        argparse_action=ArgparseAction.STORE,
        argument_short='--sdb',
        category='general',
    )] = ConfigurationBackend.FILE

    # arguments
    arg0: str = None
    arg1: str = None
    arg2: str = None
    arg3: str = None

    # [hq] bootstrap
    private_key_retrieval_method: Annotated[SecretRetrievalMethod, Field(
        title='PrivateKey Retrieval Method',
        description='Sets the method to retrieve the WireGuard private keys for wg-quick. '
                    f'“{SecretRetrievalMethod.WG_FEDERATION_COMMAND.value}” expects `--root-passphrase-command` '
                    ' to be set.'
                    f'“{SecretRetrievalMethod.TEST_INSECURE_CLEARTEXT.value}” is unsecure, thus discouraged.',
        type=SecretRetrievalMethod,
        allowed=f'“{"”, “".join([e.value for e in SecretRetrievalMethod])}”',
        true_type=SecretRetrievalMethod,
        argparse_action=ArgparseAction.STORE,
        argument_short='--PKrm',
        category='bootstrap',
    )] = SecretRetrievalMethod.WG_FEDERATION_ENV_VAR_OR_FILE

    # [hq] get-private-key
    interface_name: Annotated[str, Field(
        title='WireGuard Interface Name',
        description='Name of the WireGuard interface to retrieve the private key from.',
        type=str,
        true_type=str,
        argparse_action=ArgparseAction.STORE,
        argument_short='-i',
        category='get-private-key',
    )] = None

    interface_kind: Annotated[InterfaceKind, Field(
        title='WireGuard Interface Kind',
        description='Kind of the WireGuard interface to retrieve the private key from.',
        type=InterfaceKind,
        allowed=f'“{"”, “".join([e.value for e in InterfaceKind])}”',
        true_type=InterfaceKind,
        argparse_action=ArgparseAction.STORE,
        argument_short='-k',
        category='get-private-key',
    )] = None

    # pylint: disable=no-self-argument
    @validator('private_key_retrieval_method')
    def check_private_key_retrieval_method(cls, value: SecretRetrievalMethod, values: dict) -> SecretRetrievalMethod:
        """
        Validate private_key_retrieval_method
        :param value: passphrase_retrieval_method value
        :param values: rest of the current object’s attributes
        :return:
        """
        if value == SecretRetrievalMethod.WG_FEDERATION_COMMAND and not values.get('root_passphrase_command'):
            raise DataValidationError(
                f'The method to retrieve WireGuard interface’s private keys was set to '
                f'“{SecretRetrievalMethod.WG_FEDERATION_COMMAND.value}” '
                f'(the default value for this setting), '
                f'but you did not provide a command to get the root passphrase dynamically. '
                f'Please set --root-passphrase-command or choose another method.'
            )

        return value
