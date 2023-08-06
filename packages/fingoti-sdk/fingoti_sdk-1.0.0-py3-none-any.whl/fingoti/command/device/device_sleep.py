from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class DeviceSleep(Command):
    def __init__(self):
        self._data_store = {
            "property": "deviceSleep"
        }
    
    def write(self, duration:int):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = {"duration":duration}
        return model_to_dict(self);

def addDeviceSleep(self, duration:int):
    """
    [Read & Write]

    Adds a deviceSleep command to the builder

    Arguments
    ----------
    duration - int, optional
    """
    if(duration >= 0 and duration < 1000):
        self.add(DeviceSleep().write(duration))
    else:
        raise ValueError("period must be between 0 and 1000.")