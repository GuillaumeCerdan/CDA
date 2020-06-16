import PyPDF2
import os

for file in os.listdir("test_metadata"):
    if file.endswith(".pdf"):
        print(file)
        pdfFileObj = open('test_metadata/' + file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        count = pdfReader.numPages
        for i in range(count):
            page = pdfReader.getPage(i)
            print(page.extractText())
            print (40*"_")
            print ('brouette')

            