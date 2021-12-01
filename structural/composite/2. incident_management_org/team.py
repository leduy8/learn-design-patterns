from component import Component


class Team(Component):
    def __init__(self) -> None:
        super().__init__()
        self.components = []

    def add(self, component: Component):
        self.components.append(component)

    def action_when_fire_occure(self):
        for component in self.components:
            component.action_when_fire_occure()