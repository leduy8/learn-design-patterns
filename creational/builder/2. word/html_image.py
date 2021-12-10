from html_element import HtmlElement


class HtmlImage(HtmlElement):
    def __init__(self, source) -> None:
        self.source = source

    def get_content(self):
        return f'<img src="{self.source}"/>'