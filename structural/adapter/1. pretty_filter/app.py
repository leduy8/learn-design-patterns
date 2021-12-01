from image_view import ImageView
from image import Image
from vivid_filter import VividFilter
from ava_filter.caramel_adapter import CaramelAdapter
from ava_filter.caramel import Caramel


image_view = ImageView(Image())
image_view.apply(VividFilter())
image_view.apply(CaramelAdapter(Caramel()))