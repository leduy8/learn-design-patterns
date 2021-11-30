from ui_control import UIControl


class Button(UIControl):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.is_enable = None

    def get_enable(self):
        return self.is_enable

    def set_enable(self, enable):
        self.is_enable = enable
        # self.owner.changed(self)