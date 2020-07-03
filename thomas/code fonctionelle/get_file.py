import os



def getAllfile (path , extention = '.pdf'):
    '''
    path = la variable du chemin ou l'on veut cherhcer les pdf 
    extention = la variable qui selection 'lextention rechercher par default PDF
    return une liste de path vers des pdf a partir de la racine (C:)
    '''
    
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if extention in file:
                files.append(os.path.join(r, file))
    return(files)

# print(get_all_pdf(path))