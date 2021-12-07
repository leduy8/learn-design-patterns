from point_service import PointService
from point_icon_factory import PointIconFactory

service = PointService(PointIconFactory())

for point in service.get_points():
    point.draw()