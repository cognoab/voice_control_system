from pathlib import Path
from typing import Sequence

from ..cmd_executor import CMDExecutorProtocol
from ..common import LoggingLevel, ReturnCode, log_manager, utils
from ..speech_to_text import STTProtocol
from ..text_to_cmd import TextToCMDProtocol


class VoiceControl:
    def __init__(self, stt: STTProtocol.TranscribeAuto, ttcs: Sequence[TextToCMDProtocol], cmd_executor: CMDExecutorProtocol, logging_level: LoggingLevel | None = None) -> None:
        self.logger = log_manager.get_logger(self.__class__.__name__, logging_level)
        self.logger.info('Initializing Ubuntu Voice Control System...')
        self.ttcs = ttcs
        self._stt = stt
        self._executor = cmd_executor

    def execute_command_by_text(self, input_text: str) -> ReturnCode:
        self.logger.trace(utils.get_current_function_name(), input_text=input_text)
        for parser in self.ttcs:
            return_code, cmd = parser.parse_command(input_text)
            if return_code != ReturnCode.SUCCESS or cmd is None:
                self.logger.error('Error while parsing user input. Skipping to next parser...', input_text=input_text, parser=parser.__class__.__name__, return_code=return_code)
                continue

            return_code = self._executor.execute(cmd)
            if return_code != ReturnCode.SUCCESS:
                self.logger.error('Error while executing command.', input_text=input_text, parser=parser.__class__.__name__, cmd=cmd, return_code=return_code)
                return return_code
            else:
                self.logger.trace('Command executed successfully.')
                return ReturnCode.SUCCESS

        return ReturnCode.TTC_PARSING_ERROR

    def execute_command_by_audio(self, audio_file: str | Path) -> ReturnCode:
        self.logger.trace(utils.get_current_function_name(), audio_file=audio_file)
        return_code, input_text, language = self._stt.transcribe_auto(audio_file)
        if return_code != ReturnCode.SUCCESS:
            self.logger.error('Error while transcribing audio.', audio_file=audio_file, return_code=return_code, language=language)
            return return_code

        return self.execute_command_by_text(input_text)
