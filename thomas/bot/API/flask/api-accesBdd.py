from flask import Flask, render_template, request
import mysql.connector

def connectTo(myHost, myUser, myPassword, myDatabase):
    myconnection = mysql.connector.connect(
        host = myHost,
        user = myUser,
        passwd = myPassword,
        database = myDatabase
    )
    return myconnection


def getData(mydb, table):
    mycursor = mydb.cursor()

    sql = "SELECT * FROM data ORDER BY title"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return myresult

def uploadData(mydb, vals):
    mycursor = mydb.cursor()

    requete = "INSERT INTO data (title, content, keyword, comments) VALUES (%s, %s, %s, %s)"
    values = (vals)
    mycursor.execute(requete, values)

    mydb.commit()

    print(mycursor.rowcount, " lignes insérées !")

def updateData(mydb, id, valueToChange, newValue):
    mycursor = mydb.cursor()

    requete = "UPDATE data SET " + valueToChange + " = '" + newValue + "' WHERE id = " + str(id)
    mycursor.execute(requete)

    mydb.commit()


mydb = connectTo("localhost", "root", "", "python-upload")

values = getData(mydb, "data")

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html", message = "Page home")

@app.route("/recueils")
def recueils():
    username = request.args.get('username')
    password = request.args.get('password')
    return render_template("recueils.html", message = "Liste de recueils", username = username, password = password)

@app.route("/profile/<name>", methods=['GET'])
def name(name):
    return render_template("name.html", name = name)



@app.route("/getDonnee")
def getDonnee():
    return str(values)

@app.route("/setDonnee")
def setDonnee():
    titre = request.args.get('titre')
    content = request.args.get('content')
    keyword = request.args.get('keyword')
    comments = request.args.get('comments')
    print(titre+' ' + content+' ' + keyword +' '+ comments)
    if all([titre,content, keyword, comments]):
        uploadData(mydb,(titre,content,keyword,comments))
        return ("ca marche")
    else:
        return ("tu a oublier des param")



@app.route("/modifDonnee")
def modifDonnee():
    ids = request.args.get('id')
    champs = request.args.get('champs')
    valeur = request.args.get('valeur')
    print(ids+' ' + champs+' ' + valeur)
    if all([ids,champs, valeur]):
        updateData(mydb,ids,champs,valeur)
        return ("ca marche")
    else:
        return ("tu a oublier des param")
if __name__ == "__main__":
    app.run(debug=True)

# Voir import sys pour récupérer les paramètres passés en ligne de commande
# Double linked list