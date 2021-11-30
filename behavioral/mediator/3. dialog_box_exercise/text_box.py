from ui_control import UIControl


class TextBox(UIControl):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.content = None

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content
        self.owner.changed(self)