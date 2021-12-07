from point import Point
from point_icon_factory import PointIconFactory


class PointService:
    def __init__(self, icon_factory: PointIconFactory) -> None:
        self.icon_factory = icon_factory

    def get_points(self):
        points = []
        point = Point(1, 2, self.icon_factory.get_point_icon("Cafe"))
        points.append(point)
        
        return points