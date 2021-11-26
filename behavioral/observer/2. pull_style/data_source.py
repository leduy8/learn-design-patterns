from subject import Subject


class DataSource(Subject):
    def __init__(self) -> None:
        super().__init__()
        self.value = None

    def get(self):
        return self.value

    def set(self, value):
        self.value = value
        super().notify_observers()

