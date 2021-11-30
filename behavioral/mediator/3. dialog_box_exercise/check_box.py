from ui_control import UIControl


class CheckBox(UIControl):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.is_check = None

    def get_check(self):
        return self.is_check

    def set_check(self, check):
        self.is_check = check
        self.owner.changed(self)