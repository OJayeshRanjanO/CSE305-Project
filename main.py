from flask import Flask, request, render_template, session,redirect,url_for
from dbFunctions import *
import json
from loginPageFunctions import *
from homePageFunction import *

app = Flask(__name__)
app.secret_key = "CSE305Team1"

@app.route('/')
# @app.route("/<user>")
def index():
    return render_template("login.html")

@app.route('/checkLogin',methods=['POST'])
def checkLogin():
    recvJson = request.get_json()
    email = recvJson['email']
    password = recvJson['pwd']
    returnValue = checkPassengerCredentials(email,password)
    if returnValue:
        session['email'] = email
    return str(json.dumps({"login":"true"})) if returnValue else str(json.dumps({"login":"false"}))


@app.route('/home')
def home():
    if 'email' not in session:
        return redirect(url_for('index'))
    print(session['email'])
    return render_template("home.html")

@app.route('/getLocation',methods=['POST'])
def getLocation():
    returnValue = getLocationList()
    return str(json.dumps({"location":returnValue}))

@app.route('/searchFlights',methods=['POST'])
def searchFlights():
    # if 'email' not in session:
    #     return redirect(url_for('index'))
    recvJson = request.get_json()
    print(recvJson)
    flightFrom = recvJson["flightFrom"]
    flightTo = recvJson["flightTo"]
    flightLeavingDate = recvJson["flightLeavingDate"]
    flightClass = recvJson["flightClass"]
    flightPassengers = recvJson["flightPassengers"]
    # print(flightFrom,flightTo,flightLeavingDate,flightClass,flightPassengers)

    returnValue = checkAvailableFlights(flightFrom,flightTo,flightLeavingDate,flightClass,flightPassengers)
    return str(json.dumps({"flightDetails":returnValue}))


@app.route('/searchCruises',methods=['POST'])
def searchCrusies():
    #{"cruiseFrom":"Moscow","cruiseTo":"Beijing","cruiseLeavingDate":"2018-04-07","cruisePassengers":1}
    recvJson = request.get_json()
    cruiseFrom = recvJson["cruiseFrom"]
    cruiseTo = recvJson["cruiseTo"]
    cruiseLeavingDate = recvJson["cruiseLeavingDate"]
    cruisePassengers = recvJson["cruisePassengers"]

    returnValue = checkAvailableCrusies(cruiseFrom,cruiseTo,cruiseLeavingDate,cruisePassengers)
    return str(json.dumps({"cruiseDetails":returnValue}))



@app.route('/logout')
def logout():
    print(session)
    if 'email' in session:
        session.pop('email', None)
        print(session)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

#Lucy made a comment
#comment
