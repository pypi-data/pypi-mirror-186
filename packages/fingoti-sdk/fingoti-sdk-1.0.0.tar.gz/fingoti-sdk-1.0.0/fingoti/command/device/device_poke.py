from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class DevicePoke(Command):
    def __init__(self):
        self._data_store = {
            "property": "devicePoke",
        }

    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)


def addDevicePoke(self):
    """
    [Read]

    Adds a devicePoke command to the builder
    """
    self.add(DevicePoke().read())
