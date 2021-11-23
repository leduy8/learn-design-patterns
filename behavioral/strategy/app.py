from abc import ABC, abstractmethod


class Compressor(ABC):
    @abstractmethod
    def compress(self, filename):
        pass


class JpegCompressor(Compressor):
    def compress(self, filename):
        print('Compressing using JPEG.')


class PngCompressor(Compressor):
    def compress(self, filename):
        print('Compressing using PNG.')


class Filter:
    @abstractmethod
    def apply(self, filename):
        pass
            

class BlackAndWhiteFilter(Filter):
    def apply(self, filename):
        print('Apply B&W filter.')


class HighContrastFilter(Filter):
    def apply(self, filename):
        print('Apply high-contrast filter.')


class ImageStorage:
    def store(self, filename, compressor, filter):
        compressor.compress(filename)
        filter.apply(filename)


imgstore = ImageStorage()
imgstore.store('HelloWorld.png', PngCompressor(), HighContrastFilter())
imgstore.store('HelloWorld2.jpeg', JpegCompressor(), HighContrastFilter())
