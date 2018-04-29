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

def listAllFlights():
    try:
        connection = connect_db()
        query = "SELECT * FROM Flight"

        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        flightList = cursor.fetchall()
        connection.close()
        # This is a list of dictionaries, Each row is a dictionary
        # Use this loop to convert datetime
        for eachFlight in flightList:
            eachFlight['Schedule_Date'] = eachFlight['Schedule_Date'].strftime('%Y-%m-%d')

            # print(eachFlight)
        return flightList
    except:
        connection.close()
        return False


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

    query = "SELECT Accommodation_Type FROM Accommodation"
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

def getReviewList():
    connection = connect_db()

    query = "SELECT * FROM Review"
    cursor = connection.cursor()
    cursor.execute(query)
    reviews = cursor.fetchall()
    connection.close()

    return reviews
