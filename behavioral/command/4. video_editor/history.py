class History:
    def __init__(self) -> None:
        self.commands = []

    def push(self, command):
        self.commands.append(command)

    def pop(self):
        return self.commands.pop()

    def size(self):
        return len(self.commands)