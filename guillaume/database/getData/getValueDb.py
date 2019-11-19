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


mydb = connectTo("localhost", "root", "", "python-upload")

values = getData(mydb, "data")

for v in values:
    print(v)
