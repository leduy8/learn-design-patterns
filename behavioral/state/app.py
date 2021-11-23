from abc import ABC, abstractmethod


class Tool(ABC):
    @abstractmethod
    def mouse_down(self):
        pass

    @abstractmethod
    def mouse_up(self):
        pass


class SelectionTool(Tool):
    def mouse_down(self):
        print('Selection tool.')

    def mouse_up(self):
        print('Draw dashed triangle.')

    def __repr__(self) -> str:
        return 'Selection Tool'

    def __str__(self) -> str:
        return 'Selection Tool'


class BrushTool(Tool):
    def mouse_down(self):
        print('Brush tool.')

    def mouse_up(self):
        print('Draw a line.')

    def __repr__(self) -> str:
        return 'Brush Tool'

    def __str__(self) -> str:
        return 'Brush Tool'


class EraserTool(Tool):
    def mouse_down(self):
        print('Eraser tool.')

    def mouse_up(self):
        print('Erase something.')

    def __repr__(self) -> str:
        return 'Eraser Tool'

    def __str__(self) -> str:
        return 'Eraser Tool'


class Canvas:
    def __init__(self) -> None:
        self.current_tool = None

    def mouse_up(self):
        self.current_tool.mouse_up()

    def mouse_down(self):
        self.current_tool.mouse_down()

    def get_current_tool(self):
        return self.current_tool

    def set_current_tool(self, tool):
        self.current_tool = tool


canvas = Canvas()
canvas.set_current_tool(SelectionTool())
canvas.mouse_down()
canvas.mouse_up()
canvas.set_current_tool(BrushTool())
canvas.mouse_down()
canvas.mouse_up()
print(canvas.get_current_tool())