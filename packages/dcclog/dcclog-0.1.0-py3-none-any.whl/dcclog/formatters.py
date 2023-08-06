from __future__ import annotations

import logging
from typing import Any, Callable, Literal, Optional, Union

from dcclog import colors
from dcclog.cipher import Cipher


class Formatter(logging.Formatter):
    _color_fn: Optional[Callable[[int], str]] = None
    _DEFAULT_FORMAT = (
        "%(asctime)s :: %(levelname)-8s :: %(name)s"
        " :: %(message)s (%(filename)s:%(lineno)d)"
    )

    def __init__(
        self,
        fmt: str = _DEFAULT_FORMAT,
        *,
        color: Union[Literal[False, True], Callable[[int], str]] = False,
        cipher: Optional[Cipher] = None,
        **kwargs: Any,
    ):
        super().__init__(fmt, **kwargs)
        self.set_color(color)
        self.set_cipher(cipher)

    def set_cipher(self, cipher: Optional[Cipher] = None) -> Formatter:
        self._cipher = cipher
        return self

    def set_color(
        self, color: Union[Literal[False, True], Callable[[int], str]]
    ) -> Formatter:
        if color is True:
            self._color_fn = self.default_color_fn
        elif color is False:
            self._color_fn = None
        else:
            self._color_fn = color
        return self

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)

        if self._color_fn is not None:
            level_color = self._color_fn(record.levelno)
            message = f"{level_color}{message}{colors.RESET}"

        if self._cipher and message:
            message = self._cipher.encrypt(message, record.levelname)
        return message

    @staticmethod
    def default_color_fn(level: int) -> str:
        if level == logging.CRITICAL:
            return colors.RED_BG
        if level == logging.ERROR:
            return colors.RED
        if level == logging.WARNING:
            return colors.YELLOW
        if level == logging.INFO:
            return colors.GREEN
        if level == logging.DEBUG:
            return colors.ORANGE
        return colors.DEFAULT
