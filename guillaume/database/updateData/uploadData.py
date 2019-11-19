import mysql.connector

def connectTo(myHost, myUser, myPassword, myDatabase):
    myconnection = mysql.connector.connect(
        host = myHost,
        user = myUser,
        passwd = myPassword,
        database = myDatabase
    )
    return myconnection


def updateData(mydb, id, valueToChange, newValue):
    mycursor = mydb.cursor()

    requete = "UPDATE data SET " + valueToChange + " = '" + newValue + "' WHERE id = " + str(id)
    mycursor.execute(requete)

    mydb.commit()

    print(mycursor.rowcount, " lignes modifiées !")

mydb = connectTo("localhost", "root", "", "python-upload")

updateData(mydb, 4, "comments", "Commentaire ajouté en UPDATE")