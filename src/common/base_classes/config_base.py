import json
import os
from typing import Any

from ..log_management import log_manager
from ..protocols.logger_protocol import LoggingLevel
from ..utils import Singleton, get_traceback_str


class ConfigBase(metaclass=Singleton):
    """Singleton class for managing service configurations.

    Example:
    ```
    class MyServiceConfig(ConfigBase):
        def __init__(self):
            super().__init__()
            self.service_port = 0
            self.user_name = ""
            self.password = ""
            self.data_list = []
    cfg = MyServiceConfig()
    cfg.load_config_from_json('service_config.json')
    print(cfg.service_port)
    ```
    """

    def __init__(self, logging_level: LoggingLevel | None = None) -> None:
        """Initialize the ServiceConfig instance with default values."""
        self._logger = log_manager.get_logger(self.__class__.__name__, logging_level)
        self._is_initialized = False
        self._json_config_keys: set[Any] = set()
        self._env_config_keys: set[Any] = set()

    @property
    def configs_dict(self) -> dict[str, Any]:
        """Return a dictionary of all configuration variables"""
        return {key: value for key, value in self.__dict__.items() if not key.startswith('_')}

    def load_config_from_json(self, json_file: str) -> bool:
        """Load configuration from a JSON file."""
        if not os.path.isfile(json_file):
            self._logger.warning('Configuration file not found.', file=json_file)
            return False

        try:
            with open(json_file, 'r') as f:
                config = json.load(f)
                self._apply_config(config, self._json_config_keys)
            return True
        except Exception:
            self._logger.warning(f'Error while loading configs.\n{get_traceback_str()}')
            return False

    def save_config_to_json(self, json_file: str) -> None:
        """Save configuration to a JSON file."""
        with open(json_file, 'w') as f:
            filtered_dict = {k: v for k, v in self.configs_dict.items() if not k.startswith('_') and k not in self._env_config_keys}
            json.dump(filtered_dict, f, indent=4)

    def load_config_from_env(self) -> None:
        """Load configuration from environment variables."""
        for key in self.__dict__:
            if key.startswith('_'):
                continue
            env_var = os.getenv(key.upper())
            if env_var is not None:
                self._env_config_keys.add(key)
                setattr(self, key, self._convert_type(key, env_var))

    def _apply_config(self, config: dict[str, Any], source_set: set[Any]) -> None:
        """Apply configuration settings from a given source.

        Args:
            config (dict[str, Any]): Configuration settings to apply.
            source_set (set): The set to record the source of the configuration.
        """
        for key, value in config.items():
            if hasattr(self, key):
                source_set.add(key)
                setattr(self, key, self._convert_type(key, value))
            else:
                self._logger.warning(f'Unknown configuration key: {key}')

    def _convert_type(self, key: str, value: Any) -> Any:
        """Convert the configuration value to the type of the existing value, if possible.

        Args:
            key (str): The configuration key.
            value (Any): The value to be converted.

        Returns:
            Any: The converted value or the previous value if conversion fails.
        """
        previous_value = getattr(self, key)
        try:
            return type(previous_value)(value)
        except ValueError:
            self._logger.warning(f'Failed to convert "{key}" ({value}) to {type(previous_value)}. Keeping the previous value.')
            return previous_value
