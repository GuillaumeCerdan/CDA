import flask
from DatabaseHandler import DatabaseHandler
import json

# logger ce qui est passer
db_handler = DatabaseHandler('appli-cda', 'root', '', 'localhost')
app = flask.Flask(__name__)


@app.route("/get_all", methods=['GET'])
def get_all():
    return(json.dumps(db_handler.get_all_data()))


@app.route("/add_arrete", methods=['GET', 'POST'])
def add_arrete():
    if flask.request.method == 'POST':
        id_arrete = flask.request.form['id_arrete']
        extrait = flask.request.form['extrait']
        # score = flask.request.form['score']
        # titre_raa = flask.request.form['titre_raa']
        db_handler.add_arrete(id_arrete, extrait)
        return(1)
    else:
        return (0)


if __name__ == "__main__":
    app.run(debug=True)
