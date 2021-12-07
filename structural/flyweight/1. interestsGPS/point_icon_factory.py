from point_icon import PointIcon


class PointIconFactory:
    def __init__(self) -> None:
        self.icons = {}

    def get_point_icon(self, type):
        if type not in self.icons:
            icon = PointIcon(type, None)
            self.icons[type] = icon

        return self.icons[type]

