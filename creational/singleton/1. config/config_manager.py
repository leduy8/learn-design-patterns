from singleton_meta import SingletonMeta


class ConfigManager(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.settings = {}

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key):
        return self.settings[key]