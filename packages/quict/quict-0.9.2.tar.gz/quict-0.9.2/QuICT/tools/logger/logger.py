import getpass
import logging
import os
import sys
import socket
from datetime import datetime
from enum import Enum


class LogFormat(Enum):
    """The Enum class of the log format.
    Example:
        - ''LogFormat.zero'': None
        - ''LogFormat.full'': time | host | user | pid | tag | level | msg
        - ''LogFormat.simple'': time | tag | level | msg
        - ''LogFormat.time_only'': time | msg
    """
    zero = None
    full = "%(asctime)s | %(host)s | %(user)s | %(process)d | %(tag)s | %(levelname)s | %(message)s"
    simple = "%(asctime)s | %(tag)s | %(levelname)s | %(message)s"
    time_only = "%(asctime)s | %(message)s"


LEVEL_MAP = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARN": logging.WARN,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}


def msgdecorate(func):
    """The decorator used to construct the log msg."""

    def _decorator(self, msg, *args):
        if not isinstance(msg, str):
            msg = repr(msg)

        if args:
            func(self, "%s %s", msg, repr(args))
        else:
            func(self, "%s", msg)

    return _decorator


class Logger(object):
    """ A wrapper for logging.

    The Logger hosts a file handler and a stdout handler.
    The file handler is set to DEBUG level and will dump all the logging info to the .log
    folder. It is controlled by environment variable "LOG_DUMP".
    The stdout handler's log level is set by the parameter log_level or the environment
    variable "LOG_LEVEL".

    Supported "LOG_LEVEL" includes: DEBUG, INFO, WARN, ERROR, CRITICAL.

    Example:
        $ export LOG_DUMP=True LOG_LEVEL=INFO

    Args:
        tag(str): Log tag for stream and file output.
        format_(LogFormat): Predefined formatter. Defaults to "LogFormat.simple".
        log_level(str): The log level, Defaults to "INFO".
    """

    def __init__(
        self,
        tag: str,
        format_: LogFormat = LogFormat.simple,
        log_level: str = "INFO"
    ):
        self._format = logging.Formatter(fmt=format_.value, datefmt='%Y-%m-%d %H:%M:%S') \
            if format_ is not None else None
        self._stdout_level = os.environ.get("LOG_LEVEL") or LEVEL_MAP[log_level]
        self._logger = logging.getLogger(tag)
        self._logger.setLevel(logging.DEBUG)

        # Set stdout handler
        sh = logging.StreamHandler(sys.stdout)
        sh.setLevel(self._stdout_level)
        sh.setFormatter(self._format)
        self._logger.addHandler(sh)
        self._extra = {"host": socket.gethostname(), "user": getpass.getuser(), "tag": tag}

        # Set foldout handler
        if os.environ.get("LOG_DUMP", False) == "True":
            log_dump_folder = os.path.join(
                os.path.abspath(os.path.curdir),
                ".log",
                str(os.getpid())
            )
            if not os.path.exists(log_dump_folder):
                os.makedirs(log_dump_folder)

            filename = f"{tag}.{datetime.now().strftime('%Y-%m-%d+%H:%M')}.log"

            # File handler
            fh = logging.FileHandler(filename=f"{os.path.join(log_dump_folder, filename)}", mode='w', encoding="utf-8")
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(self._format)
            self._logger.addHandler(fh)

    @msgdecorate
    def debug(self, msg, *args):
        """Add a log with ''DEBUG'' level."""
        self._logger.debug(msg, *args, extra=self._extra)

    @msgdecorate
    def info(self, msg, *args):
        """Add a log with ''INFO'' level."""
        self._logger.info(msg, *args, extra=self._extra)

    @msgdecorate
    def warn(self, msg, *args):
        """Add a log with ''WARN'' level."""
        self._logger.warning(msg, *args, extra=self._extra)

    @msgdecorate
    def error(self, msg, *args):
        """Add a log with ''ERROR'' level."""
        self._logger.error(msg, *args, extra=self._extra)

    @msgdecorate
    def critical(self, msg, *args):
        """Add a log with ''CRITICAL'' level."""
        self._logger.critical(msg, *args, extra=self._extra)
