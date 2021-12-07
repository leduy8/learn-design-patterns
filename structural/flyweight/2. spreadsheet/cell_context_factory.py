from cell_context import CellContext


class CellContextFactory:
    def __init__(self) -> None:
        self.contexts = {}

    def get_cell_context(self, font_family, font_size, is_bold):
        hash_code = hash((font_family, font_size, is_bold))
        if hash_code not in self.contexts:
            self.contexts[hash_code] = CellContext(font_family, font_size, is_bold)

        return self.contexts[hash_code]
        