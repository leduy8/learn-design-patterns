from stream import Stream


class CompressedCloudStream(Stream):
    def __init__(self, stream) -> None:
        super().__init__()
        self.stream = stream

    def write(self, data):
        compressed = self.compress(data)
        self.stream.write(compressed)

    def compress(self, data):
        return data[0:5]