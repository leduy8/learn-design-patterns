from widget_factory import WidgetFactory
from material_textbox import MaterialTextBox
from material_button import MaterialButton


class MaterialWidgetFactory(WidgetFactory):
    def create_button(self):
        return MaterialButton()

    def create_textbox(self):
        return MaterialTextBox()