import pdfkit
import markdown
import sys

output_filename = sys.argv[1]
markdown.markdownFromFile(input='markdown.md', output='index.html', extensions=['extra'])
pdfkit.from_file('index.html', output_filename)