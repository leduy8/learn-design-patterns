from singleton_meta import SingletonMeta


class Logger(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.logs = []

    def add(self, log):
        self.logs.append(log)

    def display_all_logs(self):
        for log in self.logs:
            print(log)