class Product():
    def __init__(self, id) -> None:
        self.id = id
        self.name = None

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name