from flask import Flask, request, render_template, session,redirect,url_for
from dbFunctions import *
import json
from loginPageFunctions import *
from homePageFunction import *

app = Flask(__name__)
app.secret_key = "CSE305Team1"

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/home')
def home():
    if 'email' not in session:
        return redirect(url_for('index'))
    print(session['email'])
    return render_template("home.html")

@app.route('/createGroup',methods=['POST'])
def createGroup():
    recvJson = request.get_json()
    session['passengers'] = recvJson['numPassengers']
    print("TEST",session['passengers'],session['email'])
    return str(json.dumps({"createGroup":"true"}))

@app.route('/checkLogin',methods=['POST'])
def checkLogin():
    recvJson = request.get_json()
    email = recvJson['email']
    password = recvJson['pwd']
    returnValue = checkPassengerCredentials(email,password)
    if returnValue:
        session['email'] = email
    return str(json.dumps({"login":"true"})) if returnValue else str(json.dumps({"login":"false"}))

@app.route('/register-page')
def register():
    return render_template("register.html")

@app.route('/registerUser',methods=['POST'])
def registerUser():
    registered_json = request.get_json()
    # Store name
    name = registered_json['name']
    # Store gender
    gender = registered_json['gender']
    # Store age
    age = registered_json['age']
    # Store email
    email = registered_json['email']
    # Store password
    password = registered_json['pwd']
    returnValue = registerPassenger(name, gender, age, email, password)
    return str(json.dumps({"registered":"true"})) if returnValue else str(json.dumps({"registered":"false"}))

@app.route('/employeePage')
def employeePage():
    # if 'email' not in session:
    #     return redirect(url_for('index'))
    # print(session['email'])
    return render_template("employee.html")

@app.route('/admin')
def admin():
    # if 'email' not in session:
    #     return redirect(url_for('index'))
    # print(session['email'])
    return render_template("admin.html")

@app.route('/review')
def review():
    # if 'email' not in session:
    #     return redirect(url_for('index'))
    # print(session['email'])
    return render_template("review.html")

@app.route('/getLocation',methods=['POST'])
def getLocation():
    returnValue = getLocationList()
    print("Passengers: " + str(session['passengers']))
    return json.dumps({"location":returnValue,"numPassengers":str(session['passengers'])})


@app.route('/flights')
def flights():
    if 'email' not in session:
        return redirect(url_for('index'))
    print(session['email'])
    return render_template("flights.html")

@app.route('/searchFlights',methods=['POST'])
def searchFlights():
    # if 'email' not in session:
    #     return redirect(url_for('index'))
    recvJson = request.get_json()
    flightFrom = recvJson["flightFrom"]
    flightTo = recvJson["flightTo"]
    flightLeavingDate = recvJson["flightLeavingDate"]
    flightClass = recvJson["flightClass"]
    flightPassengers = recvJson["flightPassengers"]
    # print(flightFrom,flightTo,flightLeavingDate,flightClass,flightPassengers)

    returnValue = checkAvailableFlights(flightFrom,flightTo,flightLeavingDate,flightClass,flightPassengers)
    x = json.dumps({"flightDetails":returnValue})
    return str(x)

@app.route('/listFlights',methods=['GET'])
def listFlights():
    returnValue = listAllFlights()
    print(returnValue)
    return str(json.dumps({"flightList":returnValue}))

@app.route('/cruises')
def cruises():
    if 'email' not in session:
        return redirect(url_for('cruises'))
    print(session['email'])
    return render_template("cruises.html")

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


@app.route('/cars')
def cars():
    if 'email' not in session:
        return redirect(url_for('cars'))
    print(session['email'])
    return render_template("cars.html")

@app.route('/getCarData',methods=['POST'])
def getCarData():
    returnValue1 = getCarCompany()
    returnValue2 = getCarType()
    return str(json.dumps({"carCompany":returnValue1,"carType":returnValue2}))

@app.route('/searchCars',methods=['POST'])
def searchCars():
    # {"carCompany":"Hertz","carType":"Economy"}
    recvJson = request.get_json()
    Car_Type = recvJson["carType"]
    Car_Company = recvJson["carCompany"]

    returnValue = checkAvailableCars(Car_Company,Car_Type)
    print(returnValue)
    return str(json.dumps({"carDetails":returnValue}))    # {"carDetails": [{"CarID": 1, "Car_Company": "Hertz", "Car_Type": "Economy", "Rent": 25.0}]}


@app.route('/hotels')
def hotels():
    if 'email' not in session:
        return redirect(url_for('hotels'))
    print(session['email'])
    return render_template("hotels.html")


@app.route('/getRoomType',methods=['POST'])
def getRoomType():
    returnValue = getRoomTypeList()
    return str(json.dumps({"roomList":returnValue}))


@app.route('/searchHotels',methods=['POST'])
def searchHotels():
    # {"accommodationType":"Economy","location":"Moscow","guests":2 }
    recvJson = request.get_json()
    print(recvJson)
    Accommodation_Type = recvJson["accommodationType"]
    Location = recvJson["location"]
    Guests = recvJson["guests"]

    returnValue = checkAvailableHotel(Accommodation_Type,Location,Guests)
    return str(json.dumps({"hotelDetails":returnValue})) #{"hotelDetails": [{"AccommodationID": 1, "Accommodation_Type": "Economy", "Rate": 100.0, "Facilities": "2 Beds", "Discount": 0.0, "Location": 1, "Size": 2, "Active": 1}]}


@app.route('/addToCart',methods=['POST'])
def addToCart():
    print(session)

    if 'cart' not in session:
        session['cart'] = []
    if session['cart'] is None:
        session['cart'] = []

    recvJson = request.get_json()
    x = session['cart']
    # print(recvJson['item'])
    x.append(recvJson['item'])
    session['cart'] = x
    # print(session['cart'])
    return str(json.dumps({"addToCart":"true"}))


@app.route('/checkout')
def checkout():
    # if 'email' not in session:
    #     return redirect(url_for('index'))
    # print(session['email'])
    print(session)
    return render_template("checkout.html")

@app.route('/generateCheckout',methods=['POST'])
def generateCheckout():
    returnValue = generateCheckoutList(session['passengers'],session['cart'])
    # print("TEST",returnValue)
    return str(json.dumps({"Car":returnValue[0],"Flight":returnValue[1],"Cruise":returnValue[2],"Accommodation":returnValue[3],"Passengers":session['passengers']}))


@app.route('/logout')
def logout():
    print(session)
    if 'email' in session:
        session.pop('email', None)
        session.pop('cart',None)
        session.pop('passengers',None)

        print(session)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

#Lucy made a comment
#comment
