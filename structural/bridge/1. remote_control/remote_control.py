from device import Device


class RemoteControl:
    def __init__(self, device: Device) -> None:
        self.device = device
        
    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()