from uiControl import UIControl

class ListBox(UIControl):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.selection = None

    def get_selection(self):
        return self.selection
    
    def set_selection(self, selection):
        self.selection = selection
        self.owner.changed(self)