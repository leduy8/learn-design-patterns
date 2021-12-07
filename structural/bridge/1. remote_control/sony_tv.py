from device import Device


class SonyTV(Device):
    def turn_on(self):
        print("Sony turn on")

    def turn_off(self):
        print("Sony turn off")

    def set_channel(self, number):
        print(f"Sony set channel {number}")