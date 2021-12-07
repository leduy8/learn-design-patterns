class Cell:
    def __init__(self, row, col, context) -> None:
        self.row = row
        self.col = col
        self.context = context
        self.content = None

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content

    def get_context(self):
        return self.content

    def set_context(self, context):
        self.context = context

    def render(self):
        print(f'({self.row}, {self.col}): {self.content} [{self.context.get_font_family()}]')