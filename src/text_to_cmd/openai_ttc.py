import json

from openai import OpenAI

from ..common import CMD, CommandBase, LoggingLevel, ReturnCode, log_manager


class OpenAITTC:
    CMD_MAP = {
        'open_app': CMD.OpenApp,
        'search_route_to_location': CMD.SearchRoute,
        'volume_up': CMD.VolumeUp,
        'volume_down': CMD.VolumeDown,
        'set_volume': CMD.SetVolume,
    }

    def __init__(self, openai_api_key: str, logging_level: LoggingLevel | None = None) -> None:
        self.logger = log_manager.get_logger(self.__class__.__name__, logging_level)
        self._client = OpenAI(api_key=openai_api_key)

    def parse_command(self, text: str) -> tuple[ReturnCode, CommandBase | None]:
        openai_response = self._ask_openai(text)
        if not openai_response:
            self.logger.warning('Failed to get response from OpenAI.', text=text, response=openai_response)
            return ReturnCode.TTC_PARSING_ERROR, None
        cmd_str = openai_response.get('request')

        if not cmd_str:
            self.logger.warning('Failed to get command from OpenAI response.', text=text, response=openai_response)
            return ReturnCode.TTC_PARSING_ERROR, None

        cmd = self.CMD_MAP.get(cmd_str)
        if not cmd:
            self.logger.warning('Unknown command.', text=text, response=openai_response)
            return ReturnCode.TTC_UNKNOWN_COMMAND, None

        if cmd is CMD.OpenApp:
            if 'app_name' not in openai_response:
                self.logger.warning('Failed to get related data from OpenAI response.', text=text, response=openai_response)
                return ReturnCode.TTC_PARSING_ERROR, None
            app_name = openai_response['app_name']
            self.logger.debug(f'Command parsed: {cmd.__name__}', app_name=app_name, text=text, response=openai_response)
            return ReturnCode.SUCCESS, CMD.OpenApp(app_name)

        if cmd is CMD.SearchRoute:
            if 'location' not in openai_response:
                self.logger.warning('Failed to get related data from OpenAI response.', text=text, response=openai_response)
                return ReturnCode.TTC_PARSING_ERROR, None
            location = openai_response['location']
            self.logger.debug(f'Command parsed: {cmd.__name__}', location=location, text=text, response=openai_response)
            return ReturnCode.SUCCESS, CMD.SearchRoute(location)

        if cmd is CMD.SetVolume:
            if 'volume_value' not in openai_response:
                self.logger.warning('Failed to get related data from OpenAI response.', text=text, response=openai_response)
                return ReturnCode.TTC_PARSING_ERROR, None
            volume_value = openai_response['volume_value']
            self.logger.debug(f'Command parsed: {cmd.__name__}', volume_value=volume_value, text=text, response=openai_response)
            return ReturnCode.SUCCESS, CMD.SetVolume(volume_value)

        # NOTE: The following commands do not require any additional data
        self.logger.debug(f'Command parsed: {cmd.__name__}', text=text, response=openai_response)
        return ReturnCode.SUCCESS, cmd()  # type: ignore

    def _ask_openai(self, text: str) -> dict[str, str] | None:
        # NOTE: https://platform.openai.com/docs/guides/function-calling
        question = f'What is the request when user said:\n{text}'
        messages = [{'role': 'user', 'content': question}]
        tools = [
            {
                'type': 'function',
                'function': {
                    'name': 'get_user_request',
                    'description': 'Extract the user request from the text',
                    'parameters': {
                        'type': 'object',
                        'properties': {
                            'request': {'type': 'string', 'enum': ['none', 'unknown', 'other', *list(self.CMD_MAP.keys())]},
                            'volume_value': {'type': 'string'},
                            'location': {'type': 'string'},
                            'app_name': {'type': 'string'},
                        },
                        'required': ['request'],
                    },
                },
            }
        ]
        response = self._client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=messages,
            tools=tools,
            tool_choice='auto',
        )  # type: ignore
        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls
        if not tool_calls:
            return None
        for tool_call in tool_calls:
            if tool_call.function.name == 'get_user_request':
                return json.loads(tool_call.function.arguments)
        return None
