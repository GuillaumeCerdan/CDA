import pytesseract
from PIL import Image
from pdf2jpg import pdf2jpg


def reader_pdf_img(inputPath, output=r"temp"):
    '''
    inputPath = le fichier qui est a lire
    output = le dossier temporaire qui permet la lecture par l'ocr des fichier
    fonction qui recoit en entré un fichier pdf et qui renvois le fichier en
    texte
    '''
    retourtext = ''
    pytesseract.pytesseract.tesseract_cmd = r"D:/programme/Tesseract-OCR/tesseract.exe"
    # on garde les 300 dpi pour avoir une meilleur qualité
    result = pdf2jpg.convert_pdf2jpg(inputPath, output, dpi=300, pages="ALL")
    # lecture du texte dans l'image
    texteImg = pytesseract.image_to_string(Image.open(str(result[0].get("output_jpgfiles")[0])), lang='fra')
    retourtext += texteImg.strip()
    # boucle sur tout les fichier
    for i in range(0, len(result[0].get("output_jpgfiles"))):
        texteImg = pytesseract.image_to_string(Image.open(str(result[0].get("output_jpgfiles")[i])), lang='fra')
        retourtext += texteImg.strip()
    return retourtext
