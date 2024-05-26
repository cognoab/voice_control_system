import subprocess

from ..common import CMD, LoggingLevel, ReturnCode, log_manager, utils
from .base_classes.cmd_executor_base import CMDExecutorBase

class WindowsCMDExecutor(CMDExecutorBase):
    def __init__(self, logging_level: LoggingLevel | None = None) -> None:
        super().__init__(logging_level)
        self._cmd_handers = {
            CMD.OpenApp: self.open_app,
            CMD.VolumeUp: self.volume_up,
            CMD.VolumeDown: self.volume_down,
            CMD.SearchRoute: self.search_route,
        }
        print('H')

    def open_app(self, cmd: CMD.OpenApp) -> ReturnCode:
        app_name = cmd.app
        self.logger.info(f'Opening {app_name}...')
        return ReturnCode.SUCCESS

    def volume_up(self, cmd: CMD.VolumeUp) -> ReturnCode:
        self.logger.info('Increase volume by 5%...')
        return ReturnCode.SUCCESS

    def volume_down(self, cmd: CMD.VolumeDown) -> ReturnCode:
        self.logger.info('Descrease volume by 5%...')
        return ReturnCode.SUCCESS

    def search_route(self, cmd: CMD.SearchRoute) -> ReturnCode:
        location = cmd.location
        self.logger.info(f'Searching route to {location}...')
        return ReturnCode.SUCCESS