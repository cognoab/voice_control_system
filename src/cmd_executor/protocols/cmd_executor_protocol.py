from typing import Protocol, Type

from ...common import ReturnCode


class CMDExecutorProtocol(Protocol):
    def execute(self, cmd: Type) -> ReturnCode: ...
