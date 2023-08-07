__version__ = "0.1.8"

import logging
from logging.handlers import RotatingFileHandler
from typing import Optional
from pathlib import Path
from logutils.consts import (
    lila,
    lime_green,
    grey,
    yellow,
    blue,
    red,
    sand,
    reset,
    background_red,
)


class CustomFormatter(logging.Formatter):
    def __init__(self, colored=True):
        self.colored = colored

    def get_fmt_string(self, level):
        if self.colored:
            time_fmt = f"{lime_green}[%(asctime)s]{reset}"
            location_fmt = f"{lila}%(filename)s:%(funcName)s:%(lineno)d{reset}"
            match level:
                case logging.DEBUG:
                    level_fmt = f"{grey}%(levelname)s{reset}"
                    message_fmt = f"{sand}%(message)s{reset}"
                case logging.INFO:
                    level_fmt = f"{blue}%(levelname)s{reset}"
                    message_fmt = f"{sand}%(message)s{reset}"
                case logging.WARNING:
                    level_fmt = f"{yellow}%(levelname)s{reset}"
                    message_fmt = f"{sand}%(message)s{reset}"
                case logging.ERROR:
                    level_fmt = f"{red}%(levelname)s{reset}"
                    message_fmt = f"{red}%(message)s{reset}"
                case logging.CRITICAL:
                    level_fmt = f"{background_red}{sand}%(levelname)s{reset}{reset}"
                    message_fmt = f"{background_red}{sand}%(message)s{reset}{reset}"
                case _:
                    raise Exception("Wrong log level")
        else:
            time_fmt = "[%(asctime)s]"
            level_fmt = "%(levelname)s"
            message_fmt = "%(message)s"
            location_fmt = "%(filename)s:%(funcName)s:%(lineno)d"
        fmt = f"{time_fmt} | {level_fmt} | {location_fmt} | {message_fmt}"
        return fmt

    def format(self, record):
        log_fmt = self.get_fmt_string(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_logger(
    name,
    handler_list=["stream"],
    level=logging.INFO,
    propagate=False,
    colored=True,
    filepath: Optional[Path] = None,
):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handlers = []
    if "stream" in handler_list:
        handler = logging.StreamHandler()
        handler.setLevel(level)
        handler.setFormatter(CustomFormatter(colored=colored))
        handlers.append(handler)
    if "file" in handler_list and filepath is not None:
        if not filepath.exists():
            filepath.touch()
        handler = RotatingFileHandler(
            filepath, maxBytes=(1 * 100 * 1024 * 1024), backupCount=10
        )
        handler.setLevel(level)
        handler.setFormatter(CustomFormatter(colored=False))
        handlers.append(handler)
    if level not in (
        logging.DEBUG,
        logging.INFO,
        logging.WARNING,
        logging.ERROR,
        logging.CRITICAL,
    ):
        raise Exception(f"Level {level} not supported")
    for handler in handlers:
        logger.addHandler(handler)
    logger.propagate = propagate
    return logger
