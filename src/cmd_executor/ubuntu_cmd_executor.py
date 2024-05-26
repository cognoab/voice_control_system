import subprocess

from ..common import CMD, LoggingLevel, ReturnCode, log_manager, utils
from .base_classes.cmd_executor_base import CMDExecutorBase


class ExampleRouteFinder:
    def __init__(self, logging_level: LoggingLevel | None = None) -> None:
        self.logger = log_manager.get_logger(self.__class__.__name__, logging_level)
        self.last_position = ''

    def find_route(self, location: str) -> ReturnCode:
        if self.last_position == '':
            route = f'Findingroute from current location to {location}...'
        route = f'Finding route from {self.last_position} to {location}...'
        self.last_position = location
        self.logger.info(route)
        return ReturnCode.SUCCESS


class UbuntuCMDExecutor(CMDExecutorBase):
    def __init__(self, logging_level: LoggingLevel | None = None) -> None:
        super().__init__(logging_level)
        self.route_finder = ExampleRouteFinder()
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
        if app_name.lower() in ['chrome', 'google chrome']:
            self._run_application('google-chrome')
        return ReturnCode.SUCCESS

    def volume_up(self, cmd: CMD.VolumeUp) -> ReturnCode:
        self.logger.info('Increase volume by 5%...')
        try:
            subprocess.run(['amixer', 'set', 'Master', '5%+'], check=True)
        except subprocess.CalledProcessError as e:
            self.logger.error('Error while increasing volume.', error=e)
        return ReturnCode.SUCCESS

    def volume_down(self, cmd: CMD.VolumeDown) -> ReturnCode:
        self.logger.info('Descrease volume by 5%...')
        try:
            subprocess.run(['amixer', 'set', 'Master', '5%-'], check=True)
        except subprocess.CalledProcessError as e:
            self.logger.error('Error while descreasing volume.', error=e)
        return ReturnCode.SUCCESS

    def search_route(self, cmd: CMD.SearchRoute) -> ReturnCode:
        location = cmd.location
        self.logger.info(f'Searching route to {location}...')
        return ReturnCode.SUCCESS

    def _run_application(self, application: str) -> ReturnCode:
        try:
            subprocess.run([application], check=True)
            return ReturnCode.SUCCESS
        except subprocess.CalledProcessError as e:
            self.logger.error('Error while running application.', error=e, traceback=utils.get_traceback_str())
            return ReturnCode.CX_ERROR
