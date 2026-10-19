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
        data["teza"] = request.form.get("teza") #Pridobi težo ki jo je vnesel uporabnik
        data["visina"] = request.form.get("visina") #Pridobi višino, ki jo je vnosil uporabnik 
        if data["teza"] and data["visina"]:
            print("***********DEBUG***********") #ZA iskanje problemov
            data["itm"] = round(izracunItm (float(data["visina"]), float(data["teza"])), 2) #izračun ITM zaokroži na 2 decimalki
            dbLogic.insertData(float(data["visina"]), float(data["teza"]), data ["itm"]) # prenese podatke v dbLogic 
        
    print("*********DEBUG*********") #Za iskanje problemov 
        
    return render_template("index.html", podatki = data) # spremenjivka podatki v index.html je ista kot spremenljivka data v run.py 
    
@app.route("/izbrisi/<sID>")
def dnevnikIzbrisi(sID):
    ID = int(sID)
    dbLogic.deleteItm(ID)
    return redirect("/dnevnik")

def izracunItm (visinaCM, tezaKG): #Izračuna ITM 
    itm = tezaKG / (visinaCM/100)**2
    return itm


#@app.route("/")
#def hello_world():
#    return "Hello 2.Ri!"

@app.route("/dnevnik", methods = ["GET", "POST"])
def dnevnik ():
    data = {}
    
    data["seznam"] = dbLogic.getAll()
    return render_template("dnevnik.html", podatki = data)

# zagon aplikacije
app.config["DEBUG"] = True
app.run(host = appAdress, port = appPort)