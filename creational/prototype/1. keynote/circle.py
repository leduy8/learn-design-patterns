from component import Component


class Circle(Component):
    def __init__(self) -> None:
        self.radius = None

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def render(self):
        print("Render circle")

    def clone(self):
        clone = Circle()
        clone.set_radius(self.radius)
        return clone