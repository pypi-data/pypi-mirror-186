import logging
from collections.abc import Iterable
from typing import Optional, Union


def get_logger(
    name: Optional[str] = None,
    *,
    level: Union[str, int, None] = None,
    handlers: Optional[
        Union[Iterable[logging.Handler], logging.Handler]
    ] = None,
) -> logging.Logger:
    logger = logging.getLogger(name)
    if level is not None:
        logger.setLevel(level)
    if isinstance(handlers, logging.Handler):
        logger.addHandler(handlers)
    elif isinstance(handlers, Iterable):
        for hdlr in handlers:
            if isinstance(hdlr, logging.Handler):
                logger.addHandler(hdlr)
    return logger


getLogger = get_logger
