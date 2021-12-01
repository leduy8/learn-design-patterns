from component import Component


class Shape(Component):
    def render(self) -> None:
        print("Render shape")