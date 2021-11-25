from abstract_undoable_command import AbstractUndoableCommand


class SetLabelCommand(AbstractUndoableCommand):
    def __init__(self, text, video_editor, history) -> None:
        super().__init__(video_editor, history)

        self.text = text

    def _do_exectute(self):
        print(super().video_editor.set_label(self.text))
        super().video_editor.set_label(self.text)

    def unexecute(self):
        super().video_editor.remove_label()