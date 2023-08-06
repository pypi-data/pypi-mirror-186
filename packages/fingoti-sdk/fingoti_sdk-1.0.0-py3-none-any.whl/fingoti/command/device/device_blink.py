from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class DeviceBlink(Command):
    def __init__(self):
        self._data_store = {
            "property": "deviceBlink",
        }

    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, state:int):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = {"state": state}
        return model_to_dict(self)

class BlinkSpeed():
    OFF = 0
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    FASTEST = 4


def addDeviceBlink(self, state:BlinkSpeed = None):
    """
    [Read & Write]

    Adds a deviceBlink command to the builder

    Arguments
    ----------
    state - BlinkSpeed, optional
    """
    if (state is None):
        self.add(DeviceBlink().read())
    else:
        valid = {0, 1, 2, 3, 4}
        if state not in valid:
            raise ValueError("state must be one of %r." % valid)
        self.add(DeviceBlink().write(state))


