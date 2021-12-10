from document_builder import DocumentBuilder
from html_document import HtmlDocument


class HtmlDocumentBuilder(DocumentBuilder):
    def __init__(self) -> None:
        self.document = HtmlDocument()

    def add(self, element):
        self.document.add(element.get_content())

    def get_html_document(self):
        return self.document