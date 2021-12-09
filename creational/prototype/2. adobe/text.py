from component import Component


class Text(Component):
    def __init__(self, content) -> None:
        self.content = content

    def get(self):
        return self.content

    def clone(self):
        return Text(self.content)

    def __str__(self) -> str:
        return f'Text: {self.content}'