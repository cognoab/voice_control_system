import os
import subprocess
import traceback
import zipfile
from http import HTTPStatus
from io import BytesIO
from pathlib import Path

import requests
import vosk

from ..common import Language_ISO639_1 as Language
from ..common import LoggingLevel, ReturnCode, log_manager


class VoskSTT:
    LANGUAGE_MODEL: dict[str, str] = {Language.ENGLISH: 'vosk-model-en-us-0.42-gigaspeech', Language.VIETNAMESE: 'vosk-model-vn-0.4'}
    """Vosk Model URL can get from: https://alphacephei.com/vosk/models"""

    def __init__(self, model_folder: str = './vosk_models', logging_level: LoggingLevel | None = None) -> None:
        self.logger = log_manager.get_logger(self.__class__.__name__, logging_level)
        self._models: dict[str, vosk.Model] = {}
        self._model_folder = model_folder
        vosk.SetLogLevel(4)  # type: ignore

    def transcribe(self, audio_file: str | Path, language_code: str) -> tuple[ReturnCode, str]:
        self.logger.trace('Start transcribe using VOSK')
        model_name = self._get_model_name(language_code)
        if not model_name:
            return ReturnCode.STT_UNSUPPORT_LANGUAGE, ''
        model_path = self._get_model_path(model_name)
        if language_code not in self._models:
            self.download_model(model_name)
            self.logger.trace('Loading VOSK model', model_path=model_path, language_code=language_code)
            self._models[language_code] = vosk.Model(model_path=model_path)
        model = self._models[language_code]

        SAMPLE_RATE = 16000
        rec = vosk.KaldiRecognizer(model, SAMPLE_RATE)

        with subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i', audio_file, '-ar', str(SAMPLE_RATE), '-ac', '1', '-f', 's16le', '-'], stdout=subprocess.PIPE) as process:
            while True:
                if not process.stdout:
                    break
                data = process.stdout.read(4000)
                if len(data) == 0:
                    break
                rec.AcceptWaveform(data)

            self.logger.trace('Finish transcribe using VOSK')
            return ReturnCode.SUCCESS, ''

    def download_model(self, model_name: str) -> ReturnCode:
        self.logger.trace('Start downloading VOSK model', model_name=model_name)
        try:
            os.makedirs(self._model_folder, exist_ok=True)
            model_url = self._get_model_url(model_name)
            response = requests.get(model_url, stream=True)
            if response.status_code != HTTPStatus.OK:
                self.logger.warning('STT_FAILED_TO_DOWNLOAD_MODEL', response=response)
                return ReturnCode.STT_FAILED_TO_DOWNLOAD_MODEL
            with zipfile.ZipFile(BytesIO(response.content)) as z:
                z.extractall(self._model_folder)
            return ReturnCode.SUCCESS
        except Exception:
            self.logger.error('STT_FAILED_TO_DOWNLOAD_MODEL', traceback=traceback.format_exc())
            return ReturnCode.STT_FAILED_TO_DOWNLOAD_MODEL

    def _get_model_name(self, language_code: str) -> None | str:
        if language_code in self.LANGUAGE_MODEL:
            return self.LANGUAGE_MODEL[language_code]
        return None

    def _get_model_url(self, model_name: str) -> str:
        return f'https://alphacephei.com/vosk/models/{model_name}.zip'

    def _get_model_path(self, model_name: str) -> str:
        return f'{self._model_folder}/{model_name}'
