from flask import Flask

app = Flask(__name__)

appAdress = "0.0.0.0"
appPort = 5000

app.cofig["DEBUG"] = True
app.run(host = appAdress, port = appPort)

@app.route("/")
def hello_world():
    return "Hello 2.Ri!"