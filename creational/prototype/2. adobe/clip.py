from component import Component


class Clip(Component):
    def __init__(self, clipname) -> None:
        self.clipname = clipname

    def clone(self):
        return Clip(self.clipname)

    def __str__(self) -> str:
        return f'Clip: {self.clipname}'