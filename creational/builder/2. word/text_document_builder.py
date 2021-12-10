from document_builder import DocumentBuilder
from text_document import TextDocument


class TextDocumentBuilder(DocumentBuilder):
    def __init__(self) -> None:
        self.document = TextDocument()

    def add(self, element):
        self.document.add(element.get_content())

    def get_text_document(self):
        return self.document