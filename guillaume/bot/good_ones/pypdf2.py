import PyPDF2
import os

#

for file in os.listdir("test_metadata"):
    if file.endswith(".pdf"):
        pdfFileObj = open('test_metadata/' + file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        info = pdfReader.getDocumentInfo()

        print(info)

# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# info = pdfReader.getDocumentInfo()

# author = info.author
# creator = info.creator
# producer = info.producer
# subject = info.subject
# title = info.title

# print("author : " + str(author))
# print("creator : " + str(creator))
# print("producer : " + str(producer))
# print("subject : " + str(subject))
# print("title : " + str(title))

# print(pdfReader.numPages)

# for i in range(1, 39):
#     pageObj = pdfReader.getPage(i)
#     # print(pageObj.extractText())
#     if ("Issamoulenc" in pageObj.extractText()):
#         print("Spotted at page : " + str(i + 1))