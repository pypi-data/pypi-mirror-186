from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class DeviceTime(Command):
    def __init__(self):
        self._data_store = {
            "property": "deviceTime"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

def addDeviceTime(self):
    """
    [Read]

    Adds a deviceTime command to the builder
    """
    self.add(DeviceTime().read())