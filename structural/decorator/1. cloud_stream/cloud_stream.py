from stream import Stream


class CloudStream(Stream):
    def write(self, data):
        print(f'Storing {data}')