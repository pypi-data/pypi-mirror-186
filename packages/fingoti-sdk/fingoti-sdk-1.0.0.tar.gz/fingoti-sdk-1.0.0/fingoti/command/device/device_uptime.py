from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class DeviceUptime(Command):
    def __init__(self):
        self._data_store = {
            "property": "deviceUptime"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

def addDeviceUptime(self):
    """
    [Read]

    Adds a deviceUptime command to the builder

    Arguments
    ----------
    mode - BusMode, optional
    """
    self.add(DeviceUptime().read())