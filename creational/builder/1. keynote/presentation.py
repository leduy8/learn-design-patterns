from presentation_builder import PresentationBuilder
from slide import Slide


class Presentation:
    def __init__(self) -> None:
        self.slides = []

    def add_slide(self, slide):
        self.slides.append(slide)

    def export(self, builder: PresentationBuilder):
        builder.add_slide(Slide("Copyright"))
        for slide in self.slides:
            builder.add_slide(slide)