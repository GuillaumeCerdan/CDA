import mysql.connector


def connectTo(myHost, myUser, myPassword, myDatabase):
    myconnection = mysql.connector.connect(
        host = myHost,
        user = myUser,
        passwd = myPassword,
        database = myDatabase
    )
    return myconnection

mydb = connectTo("localhost", "root", "", "python-upload")



mycursor = mydb.cursor()

requete = "INSERT INTO data (title, content, keyword, comments) VALUES (%s, %s, %s, %s)"
values = ("Arrêt n°1", "Mon contenu tiré d'un pdf !", "Environnement", "Pas de commentaire")
mycursor.execute(requete, values)

mydb.commit()

print(mycursor.rowcount, " lignes insérées !")

