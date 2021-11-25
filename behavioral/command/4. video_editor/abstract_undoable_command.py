from abc import abstractmethod
from undoable_command import UndoableCommand


# * The purpose of this class is to make sure all undoable commands have
# * a VideoEditor and a History. Plus, whenever a command is executed,
# * it's pushed in the history. This way, we don't have to remember to
# * store each individual command in the history.
class AbstractUndoableCommand(UndoableCommand):
    def __init__(self, video_editor, history) -> None:
        self.video_editor = video_editor
        self.history = history

    def execute(self):
        # * Another application of the template method pattern. This method
        # * is defining a template for executing commands.
        self._do_exectute()

        self.history.push(self)

    @abstractmethod
    def _do_exectute(self):
        pass