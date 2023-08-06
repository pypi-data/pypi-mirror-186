import os
from binascii import unhexlify

from Cryptodome.Cipher import AES
from Cryptodome.Hash import Poly1305

from wg_federation.crypto.cryptographic_key_deriver import CryptographicKeyDeriver
from wg_federation.exception.user.data_transformation.state_signature_cannot_be_verified import \
    StateSignatureCannotBeVerified


class MessageSigner:
    """
    Able to sign a message. Able to check a signature matches a given message.
    """

    _cryptographic_key_deriver = None
    _cryptodome_poly1305: Poly1305 = None

    def __init__(self, cryptographic_key_deriver: CryptographicKeyDeriver, cryptodome_poly1305: Poly1305):
        """
        Constructor
        :param cryptographic_key_deriver:
        :param cryptodome_poly1305:
        """
        self._cryptographic_key_deriver = cryptographic_key_deriver
        self._cryptodome_poly1305 = cryptodome_poly1305

    def sign(self, message: str) -> tuple[str, ...]:
        """
        Signs a bytes message with the context user root passphrase.
        :param message: Data to extract a signature from.
        :return: [1] the message digest of the data [2] the nonce used to get the digest
        """

        mac = self._cryptodome_poly1305.new(
            key=self._cryptographic_key_deriver.derive_32b_key_from_root_passphrase(),
            cipher=AES,
            data=message.encode('UTF-8')
        )

        return mac.hexdigest(), mac.nonce.hex()

    def verify_sign(self, message: str, nonce: str, digest: str) -> bool:
        """
        Verify that a given digest/nonce are indeed signatures of the given message.
        :param message: Message to be verified
        :param nonce: Nonce used to generate the digest
        :param digest: Signature of a message
        :raise StateSignatureCannotBeVerified if message fails to verify against the digest
        :return:
        """
        try:
            self._cryptodome_poly1305.new(
                key=self._cryptographic_key_deriver.derive_32b_key_from_root_passphrase(),
                nonce=unhexlify(nonce),
                cipher=AES,
                data=message.encode('UTF-8')
            ).hexverify(digest)
            return True
        except ValueError as error:
            raise StateSignatureCannotBeVerified(
                f'State integrity failed. Are you sure you used the correct passphrase?{os.linesep}'
                f'The state signature verification failed. There might be several reasons:{os.linesep}'
                f'Either (1) the state file has been modified,'
                f' (2) the signature has been modified,'
                f' (3) state file got corrupted '
                f' (4) or the given root passphrase is wrong. {os.linesep}'
                f'Original error: {error}'
            ) from error
