
# ! This is not a good practice, I'm just lazy.
class AppleStock:
    def __init__(self, value) -> None:
        self.value = value

    def get(self):
        return self.value

    def set(self, value):
        self.value = value

    def print(self):
        print(f'AAPL[Apple]: ${self.value}')


class GoogleStock:
    def __init__(self, value) -> None:
        self.value = value

    def get(self):
        return self.value

    def set(self, value):
        self.value = value

    def print(self):
        print(f'GOOGL[Google]: ${self.value}')


class AmazonStock:
    def __init__(self, value) -> None:
        self.value = value

    def get(self):
        return self.value

    def set(self, value):
        self.value = value

    def print(self):
        print(f'AMZN[Amazon]: ${self.value}')


class FacebookStock:
    def __init__(self, value) -> None:
        self.value = value

    def get(self):
        return self.value

    def set(self, value):
        self.value = value

    def print(self):
        print(f'FB[Facebook]: ${self.value}')
