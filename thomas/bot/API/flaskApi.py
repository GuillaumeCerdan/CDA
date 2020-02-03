from flask import Flask  # pip install flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"