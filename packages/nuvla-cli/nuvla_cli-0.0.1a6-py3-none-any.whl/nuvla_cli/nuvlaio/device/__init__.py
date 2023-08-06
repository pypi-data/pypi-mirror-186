from typing import Dict, Callable

from .device import DeviceConfiguration, DeviceTypes, Device
from .dummy import DummyDevice
from .local import LocalDevice
from .remote import RemoteDevice
from .release_control import ReleaseControl, Release, ReleaseSchema


DEVICE_FACTORY: Dict[str, Callable] = {
    DeviceTypes.DUMMY.name: DummyDevice,
    DeviceTypes.LOCAL.name: LocalDevice,
    DeviceTypes.REMOTE.name: RemoteDevice,
}
