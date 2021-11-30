from dialog_box import DialogBox
from button import Button
from check_box import CheckBox
from text_box import TextBox


class SignUpDialogBox(DialogBox):
    def __init__(self) -> None:
        super().__init__()
        self.username_text_box = TextBox(self)
        self.password_text_box = TextBox(self)
        self.check_box = CheckBox(self)
        self.button = Button(self)

    def print_states(self):
        print(f'Username text box: {self.username_text_box.get_content()}')
        print(f'Password text box: {self.password_text_box.get_content()}')
        print(f'Check box: {self.check_box.get_check()}')
        print(f'Button: {self.button.get_enable()}')

    def simulateUserInteraction(self):
        self.username_text_box.set_content('duy123')
        self.print_states()
        self.password_text_box.set_content('duy123456')
        self.print_states()
        self.check_box.set_check(True)
        self.print_states()

    def changed(self, control):
        if control == self.username_text_box or control == self.password_text_box or self.check_box:
            self.check_changed()

    def check_changed(self):
        username = self.username_text_box.get_content()
        password = self.password_text_box.get_content()
        checked = self.check_box.get_check()
        if username is not None and password is not None and checked:
            self.button.set_enable(True)
            return
        self.button.set_enable(False)