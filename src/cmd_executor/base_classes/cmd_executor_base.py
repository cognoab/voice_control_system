from abc import ABC
from typing import Any, Callable, Type

from ...common import CommandBase, LoggingLevel, ReturnCode, log_manager


class CMDExecutorBase(ABC):
    def __init__(self, logging_level: LoggingLevel | None = None) -> None:
        self.logger = log_manager.get_logger(self.__class__.__name__, logging_level)
        self._cmd_handers: dict[Type, Callable[[Type], ReturnCode]] = {}

    def execute(self, cmd: Type) -> ReturnCode:
        try:
            self.logger.trace('Executing command...', command=cmd.__class__.__name__)
            cmd_type = type(cmd)
            if cmd_type not in self._cmd_handers:
                self.logger.warning('Does not have handler for command', command=cmd)
                return ReturnCode.CX_NO_HANDLER
            return self._cmd_handers[cmd_type](cmd)
        except Exception as e:
            self.logger.error('Error executing command', error=e)
            return ReturnCode.CX_ERROR
