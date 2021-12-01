from filter import Filter


class CaramelAdapter(Filter):
    def __init__(self, caramel) -> None:
        self.caramel = caramel

    def apply(self, image):
        self.caramel.start()
        self.caramel.render(image)