from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class DevicePower(Command):
    def __init__(self):
        self._data_store = {
            "property": "devicePower"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

def addDevicePower(self):
    """
    [Read]

    Adds a devicePower command to the builder
    """
    self.add(DevicePower().read())