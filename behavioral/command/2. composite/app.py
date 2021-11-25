
# ? This is an example using Composite Command

from composite_command import CompositeCommand
from resize_command import ResizeCommand
from black_and_white_command import BlackAndWhiteCommand


composite = CompositeCommand()
composite.add(ResizeCommand())
composite.add(BlackAndWhiteCommand())
composite.execute()
composite.execute()
