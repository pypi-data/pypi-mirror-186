from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class DeviceVersion(Command):
    def __init__(self):
        self._data_store = {
            "property": "deviceVersion"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

def addDeviceVersion(self):
    """
    [Read]

    Adds a deviceVersion command to the builder
    """
    self.add(DeviceVersion().read())