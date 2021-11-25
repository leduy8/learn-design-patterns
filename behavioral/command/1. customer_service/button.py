class Button:
    def __init__(self, command) -> None:
        self.command = command

    def set(self, label):
        self.label = label

    def get(self):
        return self.label

    def click(self):
        self.command.execute()