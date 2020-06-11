from os import path

class PdfHandler:

    def __init__(self) :
        print('PdfHandler inited')

    def insertPdfAt(location, pdf) :
        # TODO asserts
        try:
            open(location, 'wb').write(pdf)
            return True
        except:
            return False

    def doesPdfExistsAt(location) :
        # TODO asserts
        if path.exists(location) :
            return True
        else:
            return False