from dbConnect import *
import datetime

def checkAvailableFlights(flightFrom,flightTo,flightLeavingDate,flightClass,flightPassengers):
    # try:
        connection = connect_db()
        query = "SELECT * FROM Location WHERE City = %s"
        cursor = connection.cursor()
        cursor.execute(query,(flightFrom))
        src_location = int((cursor.fetchall()[0])['LocationID'])
        connection.close()

        connection = connect_db()
        query = "SELECT * FROM Location WHERE City = %s"
        cursor = connection.cursor()
        cursor.execute(query,(flightTo))
        dst_location = int(cursor.fetchall()[0]['LocationID'])
        connection.close()

        connection = connect_db()
        query = "SELECT * FROM Flight WHERE Src_Location = " + str(src_location) + " AND Dst_Location = " + str(dst_location) + " AND Class = '" + str(flightClass) + "' AND (SELECT TransportationID FROM Transportation WHERE TransportationID = FlightID AND Active = 1);"
        cursor = connection.cursor()
        cursor.execute(query)
        flightList = cursor.fetchall()
        connection.close()

        # Use this loop to convert datetime
        for eachFlight in flightList:
            eachFlight['Schedule_Date'] = eachFlight['Schedule_Date'].strftime('%Y-%m-%d')

            # print(eachFlight)

        # connection = connect_db()
        # query = "SELECT TransportationID FROM Transportation WHERE Transportation_Type ='Flight' AND Active = 1"
        # cursor = connection.cursor()
        # cursor.execute(query)
        # x = cursor.fetchall()
        # connection.close()
        # print(x)

        return flightList

    # except:
    #     print("Fail")
    #     connection.close()



def getLocationList():
    connection = connect_db()

    query = "SELECT * FROM Location"
    cursor = connection.cursor()
    cursor.execute(query)
    locations = cursor.fetchall()
    connection.close()

    return locations

def getRoomTypeList():
    connection = connect_db()

    query = "SELECT DISTINCT Accommodation_Type FROM Accommodation"
    cursor = connection.cursor()
    cursor.execute(query)
    roomType = cursor.fetchall()
    connection.close()

    return roomType


def checkAvailableCrusies(cruiseFrom,cruiseTo,cruiseLeavingDate,cruisePassengers):
    connection = connect_db()
    query = "SELECT * FROM Location WHERE City = %s"
    cursor = connection.cursor()
    cursor.execute(query,(cruiseFrom))
    src_location = int((cursor.fetchall()[0])['LocationID'])
    connection.close()

    connection = connect_db()
    query = "SELECT * FROM Location WHERE City = %s"
    cursor = connection.cursor()
    cursor.execute(query,(cruiseTo))
    dst_location = int(cursor.fetchall()[0]['LocationID'])
    connection.close()


    connection = connect_db()
    query = "SELECT * FROM Cruise WHERE Src_Location = " + str(src_location) +" AND Dst_Location = " + str(dst_location) + " AND (SELECT TransportationID FROM Transportation WHERE TransportationID = CruiseID AND Active = 1);"
    cursor = connection.cursor()
    cursor.execute(query)
    cruiseList = cursor.fetchall()
    connection.close()

    for eachCruise in cruiseList:
        eachCruise['Schedule_Date'] = eachCruise['Schedule_Date'].strftime('%Y-%m-%d')
    return cruiseList


def getCarCompany():
    connection = connect_db()

    query = "SELECT DISTINCT Car_Company FROM Car"
    cursor = connection.cursor()
    cursor.execute(query)
    carData = cursor.fetchall()
    connection.close()

    return carData

def getCarType():
    connection = connect_db()

    query = "SELECT DISTINCT Car_Type FROM Car"
    cursor = connection.cursor()
    cursor.execute(query)
    carData = cursor.fetchall()
    connection.close()

    return carData

def checkAvailableCars(Car_Company,Car_Type):
    connection = connect_db()
    query = "SELECT * FROM Car WHERE Car_Company = '" + str(Car_Company) +"' AND Car_Type = '" + str(Car_Type) + "' AND (SELECT TransportationID FROM Transportation WHERE TransportationID = CarID AND Active = 1);"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    carList = cursor.fetchall()
    connection.close()
    return carList

def checkAvailableHotel(Accommodation_Type,Location,Guests):
    connection = connect_db()
    query = "SELECT * FROM Location WHERE City = %s"
    cursor = connection.cursor()
    cursor.execute(query,(Location))
    city_name = int(cursor.fetchall()[0]['LocationID'])
    connection.close()

    connection = connect_db()
    query = "SELECT * FROM Accommodation WHERE Accommodation_Type = '" + str(Accommodation_Type) +"' AND Location = " + str(city_name) +" AND Size >= " + str(Guests) + " AND Active = 1;"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    accommodation_list = cursor.fetchall()
    connection.close()
    return accommodation_list

def generateCheckoutList(numPassengers,cartList):
    attr = {"Car":[],"Flight":[],"Cruise":[],"Accommodation":[]}
    car_list,flight_list,cruise_list,acccommodation_list = [],[],[],[]
    for i in cartList:
        data = i.split("-")
        lst = attr[data[0]]
        lst.append(int(data[1]))
        attr[data[0]] = lst
    # print(attr)
    if len(attr['Car']) > 0:

        for i in attr['Car']:
            connection = connect_db()
            query = "SELECT * FROM Car WHERE CarID = " + str(i)
            # print(query)
            cursor = connection.cursor()
            cursor.execute(query)
            car_list.append(cursor.fetchall()[0])
            connection.close()

    if len(attr['Flight']) > 0:
        for i in attr['Flight']:
            connection = connect_db()
            query = "SELECT * FROM Flight WHERE FlightID = " +str(i)
            # print(query)
            cursor = connection.cursor()
            cursor.execute(query)
            eachFlight = cursor.fetchall()[0]
            eachFlight['Schedule_Date'] = eachFlight['Schedule_Date'].strftime('%Y-%m-%d')
            flight_list.append(eachFlight)
            connection.close()

    if len(attr['Cruise']) > 0:
        for i in attr['Cruise']:
            connection = connect_db()
            query = "SELECT * FROM Cruise WHERE CruiseID = " + str(i)
            # print(query)
            cursor = connection.cursor()
            cursor.execute(query)
            eachCruise = cursor.fetchall()[0]
            eachCruise['Schedule_Date'] = eachCruise['Schedule_Date'].strftime('%Y-%m-%d')
            cruise_list.append(eachCruise)
            connection.close()

    if len(attr['Accommodation']) > 0:
        for i in attr['Accommodation']:
            connection = connect_db()
            query = "SELECT * FROM Accommodation WHERE AccommodationID = " + str(i)
            # print(query)
            cursor = connection.cursor()
            cursor.execute(query)
            acccommodation_list.append(cursor.fetchall()[0])
            connection.close()
    return car_list,flight_list,cruise_list,acccommodation_list

def getReviewList(item):
    item = item.split("-")
    resource = "AccommodationID" if item[0] == "Accommodation" else "CruiseID"
    ID = item[1]

    connection = connect_db()

    query = "SELECT (SELECT Name FROM Passenger WHERE Passenger.PassengerID = PRR.PassengerID) AS Name ,Review_Details,Rating FROM Passenger_Reviews_Resources AS PRR WHERE " + str(resource) +" = " + str(ID)
    cursor = connection.cursor()
    cursor.execute(query)
    reviews = cursor.fetchall()
    connection.close()

    return reviews

if __name__ == '__main__':
    x = getReviewList("Accommodation-1")
    print(x)
    # connection = connect_db()
    # query = "SELECT * FROM Passenger_Reviews_Resources WHERE AccommodationID = 1"
    #
    # cursor = connection.cursor()
    # cursor.execute(query)
    # connection.commit()
    # carsList = cursor.fetchall()
    # print(carsList)
    # connection.close()
    #
    # connection = connect_db()
    # query = "SELECT * FROM Accommodation WHERE AccommodationID = 1"
    #
    # cursor = connection.cursor()
    # cursor.execute(query)
    # connection.commit()
    # carsList = cursor.fetchall()
    # print(carsList)
    # connection.close()

