from typing import Protocol

from ...common import CommandBase, ReturnCode


class TextToCMDProtocol(Protocol):
    def parse_command(self, text: str) -> tuple[ReturnCode, CommandBase | None]: ...
