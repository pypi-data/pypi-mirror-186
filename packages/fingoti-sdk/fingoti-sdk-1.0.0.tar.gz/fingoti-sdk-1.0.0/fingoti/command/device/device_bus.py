from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class DeviceBus(Command):
    def __init__(self):
        self._data_store = {
            "property": "deviceBus"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)
    
    def write(self, mode:int):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = {"protocol": mode}
        return model_to_dict(self)

class BusMode():
    UART = 0
    I2C = 1

def addDeviceBus(self, mode:BusMode = None):
    """
    [Read & Write]

    Adds a deviceBus command to the builder

    Arguments
    ----------
    mode - BusMode, optional
    """
    if(mode is None):
        self.add(DeviceBus().read())
    else:
        valid = {0, 1}
        if mode not in valid:
            raise ValueError("mode must be one of %r." % valid)
        self.add(DeviceBus().write(mode))
