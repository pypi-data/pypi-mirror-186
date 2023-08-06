import json
from base64 import b64decode, b64encode
from typing import TYPE_CHECKING, Optional

from Crypto.Cipher import AES
from Crypto.Hash import SHA512
from Crypto.Protocol.KDF import PBKDF2

if TYPE_CHECKING:  # fixed in #b1794ca
    from typing import Any, Union

    from Crypto.Cipher import _mode_gcm

    CIPHER = Union[_mode_gcm.GcmMode, Any]
else:
    CIPHER = None


class AESEncryption:
    KEYSIZE = 32
    ITER_COUNT = 100000

    def __init__(self, password: str, salt: Optional[bytes] = None) -> None:
        if salt is None:
            salt = SHA512.new(password.encode("utf8")).digest()
        self._key = PBKDF2(
            password=password,
            salt=salt,
            dkLen=self.KEYSIZE,
            count=self.ITER_COUNT,
            hmac_hash_module=SHA512,
        )
        self._salt = salt

    def encrypt(self, plaintext: str, level: str) -> str:
        cipher: CIPHER = AES.new(self._key, AES.MODE_GCM)
        cipher.update(level.encode("utf8"))
        ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode("utf8"))
        result = json.dumps(
            {
                "nonce": b64encode(cipher.nonce).decode("utf8"),
                "tag": b64encode(tag).decode("utf8"),
                "message": b64encode(ciphertext).decode("utf8"),
            }
        )
        return (
            f"{level: <8} :: {b64encode(result.encode('utf8')).decode('utf8')}"
        )

    def decrypt(self, ciphertext: str) -> str:
        parts = ciphertext.split("::")
        if len(parts) != 2:
            return ciphertext
        level, b64_json = parts[0].strip(), parts[1].strip()
        try:
            cipher_dict: dict[str, str] = json.loads(b64decode(b64_json))
            tag = b64decode(cipher_dict["tag"])
            message = b64decode(cipher_dict["message"])
            nonce = b64decode(cipher_dict["nonce"])
            cipher: CIPHER = AES.new(self._key, AES.MODE_GCM, nonce=nonce)
            cipher.update(level.encode("utf8"))
            return cipher.decrypt_and_verify(message, tag).decode("utf8")
        except (ValueError, KeyError) as key_error:
            raise ValueError("Invalid ciphertext or password.") from key_error

    @property
    def key(self) -> bytes:
        return self._key

    @property
    def salt(self) -> bytes:
        return self._salt
