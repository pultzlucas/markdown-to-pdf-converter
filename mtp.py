import pdfkit
import markdown
import sys

mark_filename = sys.argv[1]
pdf_filename = sys.argv[2]
mark_text = open(mark_filename, 'r').read()
html = markdown.markdown(mark_text, extensions=['extra'])
pdfkit.from_string(html, pdf_filename)