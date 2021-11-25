class VideoEditor:
    def __init__(self) -> None:
        self.label = None
        self.contrast = '0.5f'

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    def remove_label(self):
        self.label = ''

    def get_contrast(self):
        return self.contrast

    def set_contrast(self, contrast):
        self.contrast = contrast

    def __str__(self) -> str:
        return f'Label: {self.label} and Contrast: {self.contrast}' 