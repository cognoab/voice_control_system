import os
from pathlib import Path

from src.common import Language_ISO639_1 as Language
from src.common import LoggingLevel, log_manager
from src.speech_to_text import STTProtocol, WhisperModel, WhisperSTT

CURRENT_FOLDER = Path(os.path.dirname(os.path.abspath(__file__)))
WHISPER_MODEL_FOLDER = str(CURRENT_FOLDER / 'data' / 'whisper_models')
EXAMPLE_AUDIO_FILE = str(CURRENT_FOLDER / 'example_data' / 'example_1.mp3')

log_manager.initialize('Single File STT Example', log_folder=f'{CURRENT_FOLDER}/logs', log_to_file=True, log_to_stdout=True, logging_level=LoggingLevel.TRACE)
logger = log_manager.get_logger(__name__)


def transcribe(audio_file: str, stt_service: STTProtocol.Transcribe) -> str:
    error, text = stt_service.transcribe(audio_file, Language.ENGLISH)
    if error:
        logger.error('Error transcribing audio file', audio_file=audio_file, error=error)
        return ''
    return text


def transcribe_auto(audio_file: str, stt_service: STTProtocol.TranscribeAuto) -> str:
    error, text, language = stt_service.transcribe_auto(audio_file)
    if error:
        logger.error('Error transcribing audio file', audio_file=audio_file, error=error)
        return ''
    else:
        logger.info(f'Detected language: "{language}"')
    return text


def detect_language(audio_file: str, stt_service: STTProtocol.DetectLanguage) -> str:
    error, language = stt_service.detect_language(audio_file)
    if error:
        logger.error('Error transcribing audio file', audio_file=audio_file, error=error)
        return ''
    return language


def main() -> None:
    logger.info('Starting the main function')
    stt = WhisperSTT(WhisperModel.MEDIUM, WHISPER_MODEL_FOLDER)

    language = detect_language(EXAMPLE_AUDIO_FILE, stt)
    logger.info(f'Detected language: "{language}"')

    text = transcribe(EXAMPLE_AUDIO_FILE, stt)
    logger.info(f'Transcribed text: "{text}"')

    text = transcribe_auto(EXAMPLE_AUDIO_FILE, stt)
    logger.info(f'Transcribed text: "{text}"')


if __name__ == '__main__':
    main()
