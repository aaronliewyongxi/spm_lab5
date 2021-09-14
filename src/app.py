import flask, time

app = flask.Flask(__name__)


@app.route("/")
def index():
    return "Welcome!!! Hello1111",time.localtime
