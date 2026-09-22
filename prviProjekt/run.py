#Sistemske knjižnice
from flask import Flask
from flask import render_template

#Moje knjižnice
from module import dbConfig
from module import dbLogic


app = Flask(__name__)

appAdress = "0.0.0.0"
appPort = 5000




@app.route("/", methods = ["GET", "POST"])
def index ():
    data = {
        "uspeh" : False
    }
    data["uspeh"] = dbLogic.getAll()
    return render_template("index.html", podatki = data)


#@app.route("/")
#def hello_world():
#    return "Hello 2.Ri!"

app.config["DEBUG"] = True
app.run(host = appAdress, port = appPort)