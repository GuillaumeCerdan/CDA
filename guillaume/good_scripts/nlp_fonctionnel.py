from io import StringIO
import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import spacy

# pip install spacy
# Puis : python -m spacy download fr_core_news_sm
# https://www.stat4decision.com/fr/traitement-langage-naturel-francais-tal-nlp/


nlp = spacy.load('fr_core_news_md')

# Retourne tokens (mots)
def return_token(sentence):
    doc = nlp(sentence)
    return [X.text for X in doc]

# Retourne ligne à ligne
def return_token_sent(sentence):
    doc = nlp(sentence)
    return [X.text for X in doc.sents]

# Reconnaissance d'entités nommées
def entites_nommees(sentence):
    doc = nlp(sentence)
    return [(X.text, X.label_) for X in doc.ents]

# Retourne l'étiquetage morph-syntaxique
def morpho_syntaxique(sentence):
    doc = nlp(sentence)
    return [(X, X.pos_) for X in doc]



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

for doc in os.listdir("pdf"):
    if doc.endswith(".pdf"):
        print("pdf/{}".format(doc))
        sentence = pdf_to_text("pdf/{}".format(doc))


list_tuples = entites_nommees(sentence)

# print(list_tuples)

# Récupère toutes les locs
for tuples in list_tuples:
    if (tuples[1] == "LOC"):
        print(tuples)
