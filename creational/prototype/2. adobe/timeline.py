class Timeline:
    def __init__(self) -> None:
        self.components = []

    def add(self, component):
        self.components.append(component)

    def print_timeline(self) -> None:
        for component in self.components:
            print(component)