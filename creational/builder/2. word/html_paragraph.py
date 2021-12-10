from html_element import HtmlElement


class HtmlParagraph(HtmlElement):
    def __init__(self, content) -> None:
        self.content = content

    def get_content(self):
        return f'<p>{self.content}</p>'