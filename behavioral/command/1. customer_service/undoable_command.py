from abc import abstractmethod
from command import Command

class UndoableCommand(Command):
    @abstractmethod
    def unexecute(self):
        return super().execute()