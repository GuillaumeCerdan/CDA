import os

from components.PdfHandler import PdfHandler

ph = PdfHandler()

files = []

for file in os.listdir("pdf-ardeche"):
    print("file : {}".format(file))
    files.append('pdf-ardeche/' + file)

print(ph.get_matching_pages_from_pdfs(files))