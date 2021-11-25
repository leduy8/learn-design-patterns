from video_editor import VideoEditor
from history import History
from set_label_command import SetLabelCommand
from set_contrast_command import SetContrastCommand
from undo_command import UndoCommand

video_editor = VideoEditor()
history = History()

set_label_command = SetLabelCommand('Video Title', video_editor, history)
set_label_command.execute()
print(f'TEXT: {video_editor}')

set_contrast_command = SetContrastCommand(1, video_editor, history)
set_contrast_command.execute()
print(f'CONTRAST: {video_editor}')

undo_command = UndoCommand(history)
undo_command.execute()
print(f'UNDO: {video_editor}')

undo_command.execute()
print(f'UNDO: {video_editor}')

undo_command.execute()
print(f'UNDO: {video_editor}')

