"""Contains the logger for the application."""
import logging

from config.cfg import LOGGING_CONFIG
from typing import cast, Iterable


def get_logger() -> logging.Logger:
    """
    Get the logger for the application.

    :return: The logger for the application.
    """

    # Get logging configuration
    level = cast(str, LOGGING_CONFIG["level"])
    format = cast(str, LOGGING_CONFIG["format"])
    datefmt = cast(str, LOGGING_CONFIG["datefmt"])
    handlers = cast(Iterable, LOGGING_CONFIG["handlers"])

    # Set up logging
    logging.basicConfig(
        level=level,
        format=format,
        datefmt=datefmt,
        handlers=handlers,
    )
    logger = logging.getLogger("rich")

    return logger
