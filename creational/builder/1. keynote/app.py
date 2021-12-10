from presentation import Presentation
from pdf_document_builder import PdfDocumentBuilder
from slide import Slide


presentation = Presentation()
presentation.add_slide(Slide('1'))
presentation.add_slide(Slide('2'))
presentation.add_slide(Slide('3'))
builder = PdfDocumentBuilder()
presentation.export(builder)
print(builder.get_pdf_document())