import re

from ..common import CMD, CommandBase, LoggingLevel, ReturnCode, log_manager
from ..common.utils import get_traceback_str


class RegexTTC:
    def __init__(self, logging_level: LoggingLevel | None = None) -> None:
        self.logger = log_manager.get_logger(self.__class__.__name__, logging_level)
        # NOTE: The keys of the dictionary are regex patterns and the values are the corresponding command classes.
        self._patterns = {
            r'open (?P<app>.+)': CMD.OpenApp,
            r'launch (?P<app>.+)': CMD.OpenApp,
            r'increase volume': CMD.VolumeUp,
            r'(turn up volume|turn volume up)': CMD.VolumeDown,
            r'decrease volume': CMD.VolumeDown,
            r'(turn down volume|turn volume down)': CMD.VolumeDown,
            r'navigate (?P<location>.+)': CMD.SearchRoute,
            r'(show|find) (route|way|road) (?P<location>.+)': CMD.SearchRoute,
        }
        self._unnecessary_words = [
            'hi',
            'hello',
            'hey',
            'please',
            'kindly',
            'can you',
            'could you',
            'would you',
            'a',
            'an',
            'the',
            'my',
            'me',
            'the',
            'just',
            'maybe',
            'actually',
            'literally',
            'basically',
            'seriously',
            'like',
            'for me',
            'to',
        ]

    def __repr__(self) -> str:
        return self.__class__.__name__

    def __str__(self) -> str:
        return self.__repr__()

    def parse_command(self, text: str) -> tuple[ReturnCode, CommandBase | None]:
        self.logger.debug('Parsing command...', text=text)
        try:
            filtered_text = self._preprocess_input(text)
            for pattern, cmd in self._patterns.items():
                match = re.match(pattern, filtered_text, re.IGNORECASE)
                if match:
                    return ReturnCode.SUCCESS, cmd(**match.groupdict())
            return ReturnCode.TTC_PARSING_ERROR, None
        except Exception as e:
            self.logger.error('Error parsing command', error=e, traceback=get_traceback_str())
            return ReturnCode.TTC_ERROR, None

    def _preprocess_input(self, input_text: str) -> str:
        pattern = r'\b(' + '|'.join(self._unnecessary_words) + r')\b'
        text = re.sub(pattern, '', input_text, flags=re.IGNORECASE)
        text = re.sub(r'[^\w\s]', '', text)
        return re.sub(r'\s+', ' ', text).strip()
