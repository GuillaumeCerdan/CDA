from flask import Flask, render_template, request
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

if __name__ == "__main__":
    app.run()


# Voir import sys pour récupérer les paramètres passés en ligne de commande
# Double linked list