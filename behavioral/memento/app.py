class EditorState:
    def __init__(self, content) -> None:
        self.content = content

    def get(self):
        return self.content


class History:
    def __init__(self, states = []) -> None:
        self.states = states or []

    def push(self, state):
        self.states.append(state)

    def pop(self):
        return self.states.pop()


class Editor:
    def __init__(self, content = None) -> None:
        self.content = content

    def get(self):
        return self.content

    def set(self, content):
        self.content = content

    def create_state(self):
        return EditorState(self.content)

    def restore(self, state):
        self.content = state.get()


editor = Editor()
history = History()

editor.set('a')
print(editor.get())
history.push(editor.create_state())

editor.set('b')
print(editor.get())
history.push(editor.create_state())

editor.set('c')
print(editor.get())
editor.restore(history.pop())

print(editor.get())

editor.restore(history.pop())
print(editor.get())