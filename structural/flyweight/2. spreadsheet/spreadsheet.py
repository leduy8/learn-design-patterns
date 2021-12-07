from cell_context_factory import CellContextFactory
from cell import Cell


class SpreadSheet:
    def __init__(self, cell_context_factory: CellContextFactory) -> None:
        self.cell_context_factory = cell_context_factory

    def get_cells(self):
        cells = []
        cell = Cell(3, 2, self.cell_context_factory.get_cell_context("Arial", 16, False))
        cell.set_content("Hello World")
        cell2 = Cell(3, 2, self.cell_context_factory.get_cell_context("Arial", 16, False))
        cell2.set_content("Hello World 22222")
        cells.append(cell)
        cells.append(cell2)

        return cells