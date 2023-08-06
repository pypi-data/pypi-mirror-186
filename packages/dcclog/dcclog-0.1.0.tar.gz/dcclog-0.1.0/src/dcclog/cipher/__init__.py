from typing import Protocol


class Cipher(Protocol):
    def encrypt(self, plaintext: str, level: str) -> str:
        ...

    def decrypt(self, ciphertext: str) -> str:
        ...
