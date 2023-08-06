from binascii import unhexlify

from pydantic import BaseModel


# mypy: ignore-errors
# https://github.com/pydantic/pydantic/issues/156


class EncryptedMessage(BaseModel, frozen=True):
    """
    Data class for an encrypted message
    """

    ciphertext: bytes = None
    digest: bytes = None
    nonce: bytes = None

    def get_hex_ciphertext(self) -> str:
        """
        Get ciphertext in hexadecimal format
        :return:
        """
        return self.ciphertext.hex()

    def get_hex_digest(self) -> str:
        """
        Get digest in hexadecimal format
        :return:
        """
        return self.digest.hex()

    def get_hex_nonce(self) -> str:
        """
        Get nonce in hexadecimal format
        :return:
        """
        return self.nonce.hex()

    @classmethod
    def from_hex(cls, ciphertext: str, digest: str, nonce: str) -> 'EncryptedMessage':
        """
        Returns a new EncryptedMessage instance base on hex strings inputs.
        :param ciphertext: Hexadecimal ciphertext
        :param digest: Hexadecimal digest
        :param nonce: Hexadecimal nonce
        :return:
        """
        return cls(
            ciphertext=unhexlify(ciphertext),
            digest=unhexlify(digest),
            nonce=unhexlify(nonce)
        )

    def hex_dict(self) -> dict:
        """
        Get this object as a dict, all field as hex.
        :return:
        """
        return {
            'ciphertext': self.get_hex_ciphertext(),
            'digest': self.get_hex_digest(),
            'nonce': self.get_hex_nonce(),
        }
