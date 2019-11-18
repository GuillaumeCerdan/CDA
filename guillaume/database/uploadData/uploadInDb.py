import mysql.connector


def connectTo(myHost, myUser, myPassword, myDatabase):
    myconnection = mysql.connector.connect(
        host = myHost,
        user = myUser,
        passwd = myPassword,
        database = myDatabase
    )
    return myconnection


def uploadData(mydb, vals):
    mycursor = mydb.cursor()

    requete = "INSERT INTO data (title, content, keyword, comments) VALUES (%s, %s, %s, %s)"
    values = (vals)
    mycursor.execute(requete, values)

    mydb.commit()

    print(mycursor.rowcount, " lignes insérées !")

mydb = connectTo("localhost", "root", "", "python-upload")

uploadData(mydb, ("Arrêt n°2", "Mon contenu tiré d'un pdf !", "Environnement", "Pas de commentaire"))