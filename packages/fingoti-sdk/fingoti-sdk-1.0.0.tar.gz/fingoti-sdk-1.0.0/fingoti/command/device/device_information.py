from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class DeviceInformation(Command):
    def __init__(self):
        self._data_store = {
            "property": "deviceInformation"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

def addDeviceInformation(self):
    """
    [Read]

    Adds a deviceInformation command to the builder
    """
    self.add(DeviceInformation().read())