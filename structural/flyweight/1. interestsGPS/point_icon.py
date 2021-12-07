class PointIcon:
    def __init__(self, type, icon) -> None:
        self.type = type # * 4 bytes
        self.icon = icon # * 20KB -> 20MB

    def get_type(self):
        return self.type