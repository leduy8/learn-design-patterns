class CellContext:
    def __init__(self, font_family, font_size, is_bold) -> None:
        self.font_family = font_family
        self.font_size = font_size
        self.is_bold = is_bold

    def get_font_family(self):
        return self.font_family

    def set_font_family(self, font_family):
        self.font_family = font_family
    
    def get_font_size(self):
        return self.font_size

    def set_font_size(self, font_size):
        self.font_size = font_size

    def get_is_bold(self):
        return self.is_bold

    def set_is_bold(self, is_bold):
        self.is_bold = is_bold