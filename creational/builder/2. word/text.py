from element import Element


class Text(Element):
    def __init__(self, content) -> None:
        self.content = content

    def get_content(self):
        return self.content