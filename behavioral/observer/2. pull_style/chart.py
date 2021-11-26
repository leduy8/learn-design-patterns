from observer import Observer


class Chart(Observer):
    def __init__(self, data_source) -> None:
        self.data_source = data_source

    def update(self):
        print(f'Chart got updated: {self.data_source.get()}')