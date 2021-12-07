from point_icon import PointIcon


class Point:
    def __init__(self, x, y, icon: PointIcon) -> None:
        self.x = x # * 4 bytes
        self.y = y # * 4 bytes
        self.icon = icon

    def draw(self):
        print(f'{self.icon.get_type()} at ({self.x}, {self.y})')