from dialogBox import DialogBox
from listBox import ListBox
from textBox import TextBox
from button import Button


class ArticlesDialogBox(DialogBox):
    def __init__(self) -> None:
        super().__init__()
        self.articlesListBox = ListBox(self)
        self.titleTextBox = TextBox(self)
        self.saveButton = Button(self)

    def simulateUserInteraction(self):
        self.articlesListBox.set_selection('Article 1')
        self.titleTextBox.set_content('')
        self.titleTextBox.set_content('Article 2')
        print(f'Text box: {self.titleTextBox.get_content()}')
        print(f'Button: {self.saveButton.get_enable()}')

    def changed(self, control):
        if control == self.articlesListBox:
            self.articleSelected()
        elif control == self.titleTextBox:
            self.titleChanged()

    def articleSelected(self):
        self.titleTextBox.set_content(self.articlesListBox.get_selection())
        self.saveButton.set_enable(True)

    def titleChanged(self):
        content = self.titleTextBox.get_content()
        is_empty = content is None or len(content) == 0
        self.saveButton.set_enable(not is_empty)