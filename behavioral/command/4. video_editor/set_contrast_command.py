from abstract_undoable_command import AbstractUndoableCommand


class SetContrastCommand(AbstractUndoableCommand):
    def __init__(self, contrast, video_editor, history) -> None:
        super().__init__(video_editor, history)

        self.prev_contrast = video_editor.get_contrast()
        self.contrast = contrast

    def _do_exectute(self):
        super().video_editor.set_contrast(self.contrast)

    def unexecute(self):
        super().video_editor.set_contrast(self.prev_contrast)