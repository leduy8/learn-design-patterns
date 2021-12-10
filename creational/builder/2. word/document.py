class Document:
    def __init__(self) -> None:
        self.elements = []

    def add(self, element):
        self.elements.append(element)

    def export(self, builder, filename):
        for element in self.elements:
            builder.add(element)