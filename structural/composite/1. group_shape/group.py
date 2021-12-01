from component import Component


class Group(Component):
    def __init__(self) -> None:
        self.components: Component = []

    def add(self, component: Component) -> None:
        self.components.append(component)

    def render(self) -> None:
        for component in self.components:
            component.render()