import os 
from io import StringIO
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


for file in os.listdir("echantillonTestPdf"):
    print(file)
    libele = ["forêt","destruction","espèce","environnement","écologie","parc naturel","loup","sanglier","dérogation"]
    compte = 0 
    testtext = pdf_to_text("echantillonTestPdf/"+ file)
    for mot in libele:
        compte +=  testtext.count(mot)
        print ("il y a {} fois le mot {}".format(compte, mot))
    print (compte)