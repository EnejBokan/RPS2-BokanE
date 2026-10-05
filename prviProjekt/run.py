#Sistemske knjižnice
from flask import Flask
from flask import render_template
from flask import request

#Moje knjižnice
from module import dbConfig
from module import dbLogic


app = Flask(__name__)

appAdress = "0.0.0.0"
appPort = 5000




@app.route("/", methods = ["GET", "POST"])
def index ():
    data = {
        "uspeh" : False,
        "itm" : None,
        "teza" : "",
        "visina" : ""
    }
    data["uspeh"] = dbLogic.getAll()
    if request.method == "POST":
        data["teza"] = request.form.get("teza")
        data["visina"] = request.form.get("visina")
        if data["teza"] and data["visina"]:
            data["itm"] = izracunItm (float(data["visina"]), float(data["teza"]))
            dbLogic.insertData(float(data["visina"]), float(data["teza"]), data ["itm"])
        
        print(data)
        
    return render_template("index.html", podatki = data)

def izracunItm (visinaCM, tezaKG):
    itm = tezaKG / (visinaCM/100)**2
    return itm


#@app.route("/")
#def hello_world():
#    return "Hello 2.Ri!"

app.config["DEBUG"] = True
app.run(host = appAdress, port = appPort)