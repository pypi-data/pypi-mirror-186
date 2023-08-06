from Cryptodome.Cipher import AES

from wg_federation.crypto.cryptographic_key_deriver import CryptographicKeyDeriver
from wg_federation.crypto.data.encrypted_message import EncryptedMessage


class MessageEncrypter:
    """
    Able to encrypt and decrypt a message.
    """

    _cryptographic_key_deriver = None
    _cryptodome_aes = None

    def __init__(self, cryptographic_key_deriver: CryptographicKeyDeriver, cryptodome_aes: AES):
        """
        Constructor
        :param cryptographic_key_deriver:
        :param cryptodome_aes:
        """
        self._cryptographic_key_deriver = cryptographic_key_deriver
        self._cryptodome_aes = cryptodome_aes

    def encrypt(self, message: bytes) -> EncryptedMessage:
        """
        Encrypted a given message
        :param message: Message to encrypt
        :return: EncryptedMessage
        """
        cipher = self._cryptodome_aes.new(
            key=self._cryptographic_key_deriver.derive_32b_key_from_root_passphrase(),
            mode=AES.MODE_EAX
        )

        ciphertext, digest = cipher.encrypt_and_digest(message)

        return EncryptedMessage(
            ciphertext=ciphertext,
            digest=digest,
            nonce=cipher.nonce,
        )

    def decrypt(self, encrypted_message: EncryptedMessage) -> bytes:
        """
        Decipher a given ciphertext with the nonce and digest
        :param encrypted_message: EncryptedMessage
        :return:
        """
        return self._cryptodome_aes.new(
            key=self._cryptographic_key_deriver.derive_32b_key_from_root_passphrase(),
            mode=AES.MODE_EAX,
            nonce=encrypted_message.nonce
        ).decrypt_and_verify(encrypted_message.ciphertext, encrypted_message.digest)
