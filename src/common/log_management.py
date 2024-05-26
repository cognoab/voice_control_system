import sys
from datetime import timedelta
from pathlib import Path
from typing import Any

import loguru
from colorama import Fore, Style

from .protocols.logger_protocol import LoggerProtocol, LoggingLevel
from .utils import Singleton

"""Logging levels."""


class LogManager(metaclass=Singleton):
    """A singleton logger class that uses loguru for logging."""

    # fmt: off
    _LOG_COLORS = {
        LoggingLevel.TRACE   : Fore.LIGHTBLACK_EX,
        LoggingLevel.DEBUG   : Fore.LIGHTGREEN_EX,
        LoggingLevel.INFO    : Fore.CYAN,
        LoggingLevel.SUCCESS : Fore.BLUE + Style.BRIGHT,
        LoggingLevel.WARNING : Fore.MAGENTA,
        LoggingLevel.ERROR   : Fore.RED,
        LoggingLevel.CRITICAL: Fore.RED + Style.BRIGHT,
    }
    """Logging color for each levels."""
    # fmt: on

    def __init__(self) -> None:
        self._loggers: dict[str, LoggerProtocol] = {}
        self._levels: dict[str, LoggingLevel] = {}
        self._logging_level = LoggingLevel.INFO

    @property
    def logging_level(self) -> LoggingLevel:
        return self._logging_level

    @logging_level.setter
    def logging_level(self, level: LoggingLevel) -> None:
        self._logging_level = level
        for logger in self._loggers.values():
            logger.level(level.name)  # type: ignore

    def initialize(self, service_name: str, log_folder: Path | str | None = None, log_to_file: bool = True, log_to_stdout: bool = True, logging_level: LoggingLevel | None = None) -> None:
        loguru.logger.remove()

        if not log_folder:
            log_folder = Path(__file__).parent
        if isinstance(log_folder, str):
            log_folder = Path(log_folder)
        log_folder.mkdir(parents=True, exist_ok=True)
        self._service_name = service_name
        self._log_folder = log_folder

        format_string = '{time:DD-MM-YY HH:mm:ss.SSS} - {level:<7} - {extra[component]} - {file.path}:{line}\n{message} - {extra[params]}\n\n'

        if log_to_file:
            loguru.logger.add(
                f'{self._log_folder}/{self._service_name}_{{time:YYYY_MM_DD}}.log',
                level=LoggingLevel.TRACE,
                format=format_string,
                filter=self._filter_log_record,  # type: ignore
                enqueue=True,
                retention=timedelta(days=30),
                rotation='00:00',
                compression='zip',
                catch=True,
                backtrace=True,
            )
        if log_to_stdout:
            loguru.logger.add(
                sys.stdout,
                level=LoggingLevel.TRACE,
                format=self._get_color_format,  # type: ignore
                filter=self._filter_log_record,  # type: ignore
                enqueue=True,
                colorize=True,
            )  # type: ignore
        if logging_level:
            self.logging_level = logging_level

    @property
    def component_levels(self) -> dict[str, LoggingLevel]:
        """Returns a dictionary of component names and their logging levels."""
        return self._levels

    def _get_color_format(self, record: dict[str, Any]) -> str:
        name = record['level'].name
        level_color = self._LOG_COLORS[name]  # type: ignore # NOTE: We know that name is a key in the dictionary (no need to check for it explicitly)
        reset = Style.RESET_ALL
        params_color = Fore.LIGHTBLACK_EX + (Style.BRIGHT if name == 'SUCCESS' else '')
        return f'{level_color}{{time:DD-MM-YY HH:mm:ss.SSS}} - {{level:<7}} - {{extra[component]}}{reset} - {params_color}{{file.path}}:{{line}}{reset}\n{level_color}{{message}}{reset} - {params_color}{{extra[params]}}{reset}\n\n'

    def get_logger(self, component_name: str, logging_level: LoggingLevel | None = None) -> LoggerProtocol:
        """Returns a loguru logger bound to a specific component."""
        self._levels[component_name] = logging_level if logging_level else self._logging_level
        if component_name not in self._loggers:
            self._loggers[component_name] = loguru.logger.bind(component=component_name)  # type: ignore
        return self._loggers[component_name]

    def set_logging_level(self, component_name: str, logging_level: LoggingLevel) -> bool:
        """Changes the logging level for a specific component logger."""
        if component_name not in self._levels:
            return False
        self._levels[component_name] = logging_level
        self._loggers[component_name].level(logging_level.name)  # type: ignore
        return True

    def _filter_log_record(self, record: dict[str, Any]) -> bool:
        """Filters the log record to separate out 'component' from other parameters."""
        component = record['extra'].get('component')
        if component in self._levels:
            try:
                level_no = loguru.logger.level(self._levels[component]).no  # type: ignore
            except Exception:
                level_no = 20
            record['extra']['params'] = {k: v for k, v in record['extra'].items() if k not in ['component', 'params']}  # type: ignore
            return record['level'].no >= level_no  # type: ignore
        return False


log_manager = LogManager()
