from presentation_builder import PresentationBuilder
from pdf_document import PdfDocument


class PdfDocumentBuilder(PresentationBuilder):
    def __init__(self) -> None:
        self.document = PdfDocument()

    def add_slide(self, slide):
        self.document.add_slide(slide.get_text())

    def get_pdf_document(self):
        return self.document