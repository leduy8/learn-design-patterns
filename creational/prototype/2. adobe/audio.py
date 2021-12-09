from component import Component


class Audio(Component):
    def __init__(self, soundtrack) -> None:
        self.soundtrack = soundtrack

    def clone(self):
        return Audio(self.soundtrack)
        
    def __str__(self) -> str:
        return f'Audio: {self.soundtrack}'