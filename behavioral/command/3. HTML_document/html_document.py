class HtmlDocument:
    def __init__(self) -> None:
        self.content = None

    def get(self):
        return self.content

    def set(self, content):
        self.content = content

    def make_bold(self):
        self.content = f'<strong>{self.content}</strong>'