from flask import Flask
from flask import render_template

app = Flask(__name__)

appAdress = "0.0.0.0"
appPort = 5000

"""
@app.route("/", methods = ["GET", "POST"])
def helloWorld ():
    return render_template("index.html")
"""

app.config["DEBUG"] = True
app.run(host = appAdress, port = appPort)


@app.route("/")
def hello_world():
    return "Hello 2.Ri!"
