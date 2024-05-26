from enum import StrEnum
from typing import Any, Protocol


class LoggingLevel(StrEnum):
    TRACE = 'TRACE'
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    SUCCESS = 'SUCCESS'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'


class LoggerProtocol(Protocol):
    """The protocol used to implement a logger."""

    def trace(self, log_message: str, **extra: Any):
        """Represents a very detailed debugging information, typically used during development or troubleshooting."""
        ...

    def debug(self, log_message: str, **extra: Any):
        """Represents debugging information, typically used during development or troubleshooting."""
        ...

    def info(self, log_message: str, **extra: Any):
        """Represents informational messages that provide general information about the application's state or progress."""
        ...

    def warning(self, log_message: str, **extra: Any):
        """Represents potentially harmful situations or potential issues."""
        ...

    def error(self, log_message: str, **extra: Any):
        """Represents errors that are not critical but should be addressed."""
        ...

    def critical(self, log_message: str, **extra: Any):
        """Represents critical errors that may lead to application failure."""
        ...


class LogManagerProtocol(Protocol):
    """The protocol used to implement a log manager."""

    def get_logger(self, component_name: str, logging_level: LoggingLevel | None = None) -> LoggerProtocol:
        """Get a logger for the given component."""
        ...

    def set_logging_level(self, component_name: str, logging_level: LoggingLevel) -> bool:
        """Set the logging level for a specific component. If the message level is lower than the logging level, the message will be ignored"""
        ...
