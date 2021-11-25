from command import Command


class UndoCommand(Command):
    def __init__(self, history) -> None:
        self.history = history

    def execute(self):
        if self.history.size() > 0:
            self.history.pop().unexecute()