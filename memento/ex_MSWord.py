
# * Our Document class has three attributes:
# * - content
# * - fontName
# * - fontSize
# * We should allow the user to undo the changes to any of these
# * attributes. In the future, we may add additional attributes in this
# * class and these attributes should also be undoable.
# * Implement the undo feature using the memento pattern.

class EditorState:
    def __init__(self, content, font_name, font_size) -> None:
        self.content = content
        self.font_name = font_name
        self.font_size = font_size

    def get_content(self):
        return self.content

    def get_font_name(self):
        return self.font_name

    def get_font_size(self):
        return self.font_size


class History:
    def __init__(self, states=[]) -> None:
        self.states = states or []

    def push(self, state):
        self.states.append(state)

    def pop(self):
        return self.states.pop()


class Editor:
    def __init__(self, content=None, font_name='Arial', font_size=14) -> None:
        self.content = content
        self.font_name = font_name
        self.font_size = font_size

    def get_content(self):
        return self.content

    def get_font_name(self):
        return self.font_name

    def get_font_size(self):
        return self.font_size

    def set_content(self, content):
        self.content = content

    def set_font_name(self, font_name):
        self.font_name = font_name

    def set_font_size(self, font_size):
        self.font_size = font_size

    def create_state(self):
        return EditorState(self.content, self.font_name, self.font_size)

    def restore(self, state):
        self.content = state.get_content()
        self.font_name = state.get_font_name()
        self.font_size = state.get_font_size()


editor = Editor()
history = History()

editor.set_content('a')
print(f'Content: {editor.get_content()}')
print(f'Font name: {editor.get_font_name()}')
print(f'Font size: {editor.get_font_size()}')
history.push(editor.create_state())

editor.set_content('b')
print(f'Content: {editor.get_content()}')
print(f'Font name: {editor.get_font_name()}')
print(f'Font size: {editor.get_font_size()}')
history.push(editor.create_state())

editor.set_font_size(26)
print(f'Content: {editor.get_content()}')
print(f'Font name: {editor.get_font_name()}')
print(f'Font size: {editor.get_font_size()}')
history.push(editor.create_state())

editor.set_font_name('Times New Roman')
print(f'Content: {editor.get_content()}')
print(f'Font name: {editor.get_font_name()}')
print(f'Font size: {editor.get_font_size()}')

editor.restore(history.pop())
print(f'Content: {editor.get_content()}')
print(f'Font name: {editor.get_font_name()}')
print(f'Font size: {editor.get_font_size()}')

editor.restore(history.pop())
print(f'Content: {editor.get_content()}')
print(f'Font name: {editor.get_font_name()}')
print(f'Font size: {editor.get_font_size()}')
