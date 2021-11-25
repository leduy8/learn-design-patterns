
# ? This is an example using Undoable Command

from history import History
from html_document import HtmlDocument
from bold_command import BoldCommand
from undo_command import UndoCommand

history = History()
document = HtmlDocument()
document.set('Hello World')

bold_command = BoldCommand(document, history)
bold_command.execute()

print(document.get())

undo_command = UndoCommand(history)
undo_command.execute()

print(document.get())
