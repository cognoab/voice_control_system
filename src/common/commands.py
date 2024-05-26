from .base_classes.command_base import CommandBase


class CMD:
    class VolumeUp(CommandBase):
        """The command to increase the volume."""

        def __init__(self):
            pass

    class VolumeDown(CommandBase):
        """The command to descrease the volume."""

        def __init__(self):
            pass

    class SetVolume(CommandBase):
        """The command to set the volume at a specific value."""

        def __init__(self, volume: str):
            self.volume = volume

    class SearchRoute(CommandBase):
        """The command to search for a route to a location."""

        def __init__(self, location: str):
            self.location = location

    class OpenApp(CommandBase):
        """The command to open an application."""

        def __init__(self, app: str):
            self.app = app
