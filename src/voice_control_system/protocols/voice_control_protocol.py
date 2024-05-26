from pathlib import Path
from typing import Protocol

from ...common.error_codes import VoiceControlError as Error


class VoiceControlProtocol(Protocol):
    def execute_command_by_text(self, input_text: str) -> Error | None: ...

    def execute_command_by_audio(self, audio_file: str | Path) -> Error | None: ...
