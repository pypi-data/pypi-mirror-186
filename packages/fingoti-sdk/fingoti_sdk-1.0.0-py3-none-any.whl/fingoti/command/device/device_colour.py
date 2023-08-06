from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict


class DeviceColour(Command):
    def __init__(self):
        self._data_store = {
            "property": "deviceColour",
        }

    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, r: int, g: int, b: int):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = {"colour": [r, g, b]}
        return model_to_dict(self)


def addDeviceColour(self, r: int = None, g: int = None, b: int = None):
    """
    [Read & Write]

    Adds a deviceColour command to the builder

    Arguments
    ----------
    r - int, optional

    g - int, optional
    
    b - int, optional
    """
    if (r is None or g is None or b is None):
        self.add(DeviceColour().read())
    else:
        for x in {r, g, b}:
            if (x < 0 or x > 255):
                raise ValueError("r, g, b must be between 0 and 255")

        self.add(DeviceColour().write(r, g, b))