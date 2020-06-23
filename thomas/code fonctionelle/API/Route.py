import flask
from DatabaseHandler import DatabaseHandler
import json


db_handler = DatabaseHandler('appli-cda', 'root', '','localhost')
app = flask.Flask(__name__)

@app.route("/")
def accueil():
    return ('page accueil')

@app.route("/get_all")
def get_all():
    return(json.dumps(db_handler.get_all_data()))

@app.route("/add_prefecture")
def add_prefecture():
    if flask.request.method=='POST':
        # do something
        return(1)
    else:
        return (0)

@app.route("/add_raa")
def add_raa():
    return('WIP')


@app.route("/add_arrete")
def add_arrete():
    return('WIP')

if __name__ == "__main__":
    app.run()
