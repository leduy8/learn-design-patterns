from undoable_command import UndoableCommand


class BoldCommand(UndoableCommand):
    def __init__(self, document, history) -> None:
        self.prev_content = None
        self.document = document
        self.history = history

    def unexecute(self):
        self.document.set(self.prev_content)

    def execute(self):
        self.prev_content = self.document.get()
        self.document.make_bold()
        self.history.push(self)