from document import Document

from image import Image
from text import Text
from text_document_builder import TextDocumentBuilder

from html_image import HtmlImage
from html_paragraph import HtmlParagraph
from html_document_builder import HtmlDocumentBuilder



document = Document()
document.add(Text("123456"))
document.add(Text("654321"))
document.add(Image("C"))
builder = TextDocumentBuilder()
document.export(builder, "text1.txt")
print(builder.get_text_document())

print('---------------------------------------------')

html = Document()
html.add(HtmlParagraph("Brooooo"))
html.add(HtmlImage("http://google1.com/some-picture"))
builder2 = HtmlDocumentBuilder()
html.export(builder2, "test.html")
print(builder2.get_html_document())