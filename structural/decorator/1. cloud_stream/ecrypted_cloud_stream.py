from stream import Stream


class EncryptedCloudStream(Stream):
    def __init__(self, stream) -> None:
        super().__init__()
        self.stream = stream

    def write(self, data):
        encrypted = self.encrypt(data)
        self.stream.write(encrypted)

    def encrypt(self, data):
        return '!@#$%^&'