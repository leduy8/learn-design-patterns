class ImageView:
    def __init__(self, image) -> None:
        self.image = image

    def apply(self, filter):
        filter.apply(self.image)