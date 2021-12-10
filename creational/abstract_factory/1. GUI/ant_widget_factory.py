from widget_factory import WidgetFactory
from ant_textbox import AntTextBox
from ant_button import AntButton


class AntWidgetFactory(WidgetFactory):
    def create_button(self):
        return AntButton()

    def create_textbox(self):
        return AntTextBox()