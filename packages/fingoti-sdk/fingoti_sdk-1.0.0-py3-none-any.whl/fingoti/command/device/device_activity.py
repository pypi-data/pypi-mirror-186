from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class DeviceActivity(Command):
    def __init__(self):
        self._data_store = {
            'property': 'deviceActivity'
        }

    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)
    
    def write(self, enabled:bool):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = {"enabled": enabled}
        return model_to_dict(self)

def addDeviceActivity(self, enabled:bool = None):
    """ 
    [Read & Write] 

    Adds a deviceActivity command to the builder 

    Arguments
    ----------
    enabled - bool, optional
    """
    if(enabled is None):
        self.add(DeviceActivity().read())
    else:
        self.add(DeviceActivity().write(enabled))
