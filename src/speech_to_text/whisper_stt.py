from enum import StrEnum
from pathlib import Path
from typing import Any

import numpy as np
import torch
import whisper

from ..common import LoggingLevel, ReturnCode, log_manager, utils


class WhisperModel(StrEnum):
    TINY = 'tiny'
    BASE = 'base'
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'


class WhisperSTT:
    def __init__(
        self,
        model_name: WhisperModel,
        model_folder: str = './whisper_models',
        initial_prompt: str = '',
        no_speech_threshold: float = 0.6,
        condition_on_previous_text: bool = False,
        logging_level: LoggingLevel | None = None,
    ) -> None:
        self.logger = log_manager.get_logger(self.__class__.__name__, logging_level)
        self.logger.info('Initializing Whisper STT...')
        self._model_name = model_name
        self._model_folder = model_folder
        self._initial_prompt = initial_prompt
        self._no_speech_threshold = no_speech_threshold
        self._condition_on_previous_text = condition_on_previous_text
        try:
            self._model: whisper.Whisper = whisper.load_model(name=str(model_name), download_root=model_folder, in_memory=True)
        except Exception as e:
            self.logger.error('Failed to load Whisper STT model', exception=e, traceback=utils.get_traceback_str())
            return
        self._use_gpu = torch.cuda.is_available()
        if self._use_gpu:
            self.logger.info('CUDA is available. The code will run on GPU.')
        else:
            self.logger.warning('CUDA is NOT available. The code will run on CPU.')

    def transcribe(self, audio_file: str | Path, language_code: str) -> tuple[ReturnCode, str]:
        error, text, _ = self._transcribe(audio_file, language_code)
        return error, text

    def transcribe_auto(self, audio_file: str | Path) -> tuple[ReturnCode, str, str]:
        return self._transcribe(audio_file, None)

    def detect_language(self, audio_file: str | Path) -> tuple[ReturnCode, str]:
        self.logger.trace('Detecting language using Whisper STT', audio_file=audio_file)
        if Path(audio_file).exists() is False:
            self.logger.error('The audio file does not exist', audio_file=audio_file)
            return ReturnCode.STT_FILE_NOT_FOUND, ''
        try:
            audio: np.ndarray = whisper.load_audio(str(audio_file))
            audio: np.ndarray = whisper.pad_or_trim(audio)
            mel = whisper.log_mel_spectrogram(audio).to(self._model.device)
            _, probs = self._model.detect_language(mel)
            return ReturnCode.SUCCESS, {max(probs, key=probs.get)}.pop()
        except Exception as e:
            self.logger.error('Failed to detect language using Whisper STT', audio_file=audio_file, exception=e)
            return ReturnCode.STT_DETECT_LANGUAGE_FAILED, ''
        finally:
            self.logger.trace('Finished detecting language', audio_file=audio_file)

    def _transcribe(self, audio_file: str | Path, language_code: str | None) -> tuple[ReturnCode, str, str]:
        self.logger.trace('Transcribing audio file using Whisper STT', audio_file=audio_file)
        if Path(audio_file).exists() is False:
            self.logger.error('The audio file does not exist', audio_file=audio_file)
            return ReturnCode.STT_FILE_NOT_FOUND, '', ''

        try:
            result: dict[str, Any] = self._model.transcribe(  # type: ignore
                str(audio_file),
                language=language_code,
                initial_prompt=self._initial_prompt,
                no_speech_threshold=self._no_speech_threshold,
                condition_on_previous_text=self._condition_on_previous_text,
                fp16=self._use_gpu,
            )
            detect_language: str = ''

            if 'language' in result:
                detect_language = str(result['language'])

            if 'text' not in result:
                self.logger.error('The Whisper STT result does not have "text" key', audio_file=audio_file, result=result)
                return ReturnCode.STT_TRANSCRIPT_FAILED, '', detect_language

            if not isinstance(result['text'], str):
                self.logger.error('The value of "text" in Whisper STT result is not "str"', audio_file=audio_file, result=result)
                return ReturnCode.STT_TRANSCRIPT_FAILED, '', detect_language

            return ReturnCode.SUCCESS, str(result['text']), detect_language
        except Exception as e:
            self.logger.error('Failed to transcribe using Whisper STT', audio_file=audio_file, exception=e)
            return ReturnCode.STT_TRANSCRIPT_FAILED, '', ''
        finally:
            self.logger.trace('Finished transcribing audio file', audio_file=audio_file)
