from typing import Iterator, Optional

from dcclog.cipher import Cipher


def read(logfile: str, cipher: Optional[Cipher] = None) -> Iterator[str]:
    with open(logfile, encoding="utf8") as file:
        for message in file:
            if message:
                if cipher:
                    try:
                        message = cipher.decrypt(message)
                    except ValueError:
                        pass
                yield message
