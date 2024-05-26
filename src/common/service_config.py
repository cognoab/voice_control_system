from .base_classes.config_base import ConfigBase
from .protocols.logger_protocol import LoggingLevel


class MyServiceConfig(ConfigBase):
    def __init__(self, logging_level: LoggingLevel | None = None) -> None:
        super().__init__(logging_level)
        self.app_name = 'Voice Control System'
        self.logging_level = LoggingLevel.INFO
        self.openai_api_key = ''


config = MyServiceConfig()
