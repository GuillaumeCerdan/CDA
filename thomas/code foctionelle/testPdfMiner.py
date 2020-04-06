
from io import StringIO
import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter #process_pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams


def pdf_to_text(pdfname):

    # PDFMiner boilerplate
    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, sio,  laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # Extract text
    fp = open(pdfname, 'rb')
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    fp.close()

    # Get text from StringIO
    text = sio.getvalue()

    # Cleanup
    device.close()
    sio.close()

    return text

for doc in os.listdir("test_metadata"):
    if doc.endswith(".pdf"):
        print("test_metadata/{}".format(doc))
        print(pdf_to_text("test_metadata/{}".format(doc)))