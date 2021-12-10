from element import Element


class Image(Element):
    def __init__(self, source) -> None:
        self.source = source

    def get_content(self):
        return self.source