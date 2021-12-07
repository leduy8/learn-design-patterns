from spreadsheet import SpreadSheet
from cell_context_factory import CellContextFactory

ss = SpreadSheet(CellContextFactory())
for cell in ss.get_cells():
    cell.render()