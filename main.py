from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, John!</p>"


@app.route("/about")
def hello_world():
    return "<p>Hello, from about page!</p>"
