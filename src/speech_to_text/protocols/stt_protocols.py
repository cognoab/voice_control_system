from pathlib import Path
from typing import Protocol

from ...common import ReturnCode


class STTProtocol:
    class Transcribe(Protocol):
        def transcribe(self, audio_file: str | Path, language_code: str) -> tuple[ReturnCode, str]:
            """Convert an audio file to text."""
            ...

    class TranscribeAuto(Protocol):
        def transcribe_auto(self, audio_file: str | Path) -> tuple[ReturnCode, str, str]:
            """Auto detect language from an audio file and convert it to text."""
            ...

    class DetectLanguage(Protocol):
        def detect_language(self, audio_file: str | Path) -> tuple[ReturnCode, str]:
            """Detect the language of an audio file."""
            ...
