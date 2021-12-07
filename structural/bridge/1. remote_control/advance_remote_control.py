from remote_control import RemoteControl
from device import Device


class AdvanceRemoteControl(RemoteControl):
    def __init__(self, device: Device) -> None:
        super().__init__(device)

    def set_channel(self, number):
        self.device.set_channel(number)