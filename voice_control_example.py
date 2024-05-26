import os
from pathlib import Path

from src.cmd_executor import UbuntuCMDExecutor, WindowsCMDExecutor
from src.common import config, log_manager, utils
from src.speech_to_text import WhisperModel, WhisperSTT
from src.text_to_cmd import OpenAITTC, RegexTTC, TextToCMDProtocol
from src.voice_control_system import VoiceControl

CURRENT_FOLDER = Path(os.path.dirname(os.path.abspath(__file__)))
WHISPER_MODEL_FOLDER = str(CURRENT_FOLDER / 'data' / 'whisper_models')
CONFIG_FILE = str(CURRENT_FOLDER / 'config.json')


def main() -> None:
    # TO USE OPENAI Text-To-Command, export OPENAI_API_KEY in your environment variables:
    # export OPENAI_API_KEY=[your_openai_api_key]
    # or store it in "config.json"
    config.load_config_from_json(CONFIG_FILE)
    config.load_config_from_env()

    log_manager.initialize('Voice Control Example', log_folder=f'{CURRENT_FOLDER}/logs', log_to_file=True, log_to_stdout=True, logging_level=config.logging_level)
    logger = log_manager.get_logger(__name__)
    try:
        logger.info('Starting voice control system...')
        stt = WhisperSTT(WhisperModel.MEDIUM, WHISPER_MODEL_FOLDER)
        ttcs: list[TextToCMDProtocol] = [RegexTTC()]
        if config.openai_api_key and len(config.openai_api_key) > 0:
            ttcs.append(OpenAITTC(config.openai_api_key))

        if os.name == 'posix':
            logger.debug('Operating system is Unix or Linux')
            cmd_executor = UbuntuCMDExecutor()
        elif os.name == 'nt':
            logger.debug('Operating system is Windows')
            cmd_executor = WindowsCMDExecutor()
        else:
            logger.debug('Operating system is not recognized')
            return
        voice_control = VoiceControl(stt, ttcs, cmd_executor)

        path = Path(f'{CURRENT_FOLDER}/example_data')
        for mp3_file in path.rglob('*.mp3'):
            voice_control.execute_command_by_audio(mp3_file)

        logger.info('Done')
    except Exception as e:
        logger.error('Unexpected error', e=e, traceback=utils.get_traceback_str())


if __name__ == '__main__':
    main()
