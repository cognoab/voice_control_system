import os
from pathlib import Path

from src.common import LoggingLevel, config, log_manager
from src.text_to_cmd import OpenAITTC

CURRENT_FOLDER = Path(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = str(CURRENT_FOLDER/'config.json')


def main():
    # TO USE OPENAI Text-To-Command, export OPENAI_API_KEY in your environment variables:
    # export OPENAI_API_KEY=[your_openai_api_key]
    # or store it in "config.json"
    config.load_config_from_json(CONFIG_FILE)
    config.load_config_from_env()

    log_manager.initialize('OpenAI TTC Example', logging_level=LoggingLevel.TRACE)
    logger = log_manager.get_logger('OpenAI TTC Example')

    
    if not config.openai_api_key or len(config.openai_api_key) == 0:
        logger.error(f'export OPENAI_API_KEY or save it in the JSON config file', config_file=CONFIG_FILE)
        return
    ttc = OpenAITTC(config.openai_api_key)

    result = ttc.parse_command('Open YouTube')
    logger.info(f'Parsed command: {result}', result=result)
    result = ttc.parse_command('Can you maximize the volume?')
    logger.info(f'Parsed command: {result}', result=result)
    result = ttc.parse_command('Reduce the volume')
    logger.info(f'Parsed command: {result}', result=result)
    result = ttc.parse_command('Find me a route to the nearest gas station')
    logger.info(f'Parsed command: {result}', result=result)
    result = ttc.parse_command('Show me the way to New York City')
    logger.info(f'Parsed command: {result}', result=result)
    result = ttc.parse_command('Nice to meet you')
    logger.info(f'Parsed command: {result}', result=result)
    result = ttc.parse_command('Can you search the Internet for information about the moon?')
    logger.info(f'Parsed command: {result}', result=result)


if __name__ == '__main__':
    main()
