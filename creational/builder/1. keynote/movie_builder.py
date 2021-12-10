from presentation_builder import PresentationBuilder
from movie import Movie


class MovieBuilder(PresentationBuilder):
    def __init__(self) -> None:
        self.movie = Movie()

    def add_slide(self, slide):
        self.movie.add_frame(slide.get_text(), 3)

    def get_movie(self):
        return self.movie