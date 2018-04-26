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
        query = "SELECT * FROM Flight WHERE Src_Location = " + str(src_location) +" AND Dst_Location = " + str(dst_location) + " AND Class = '" + str(flightClass) + "';"
        cursor = connection.cursor()
        cursor.execute(query)
        flightList = cursor.fetchall()
        connection.close()

        for eachFlight in flightList:
            eachFlight['Schedule_Date'] = eachFlight['Schedule_Date'].strftime('%Y-%m-%d')

            print(eachFlight)



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
    query = "SELECT * FROM Cruise WHERE Src_Location = " + str(src_location) +" AND Dst_Location = " + str(dst_location) + ";"
    cursor = connection.cursor()
    cursor.execute(query)
    cruiseList = cursor.fetchall()
    connection.close()

    for eachCruise in cruiseList:
        eachCruise['Schedule_Date'] = eachCruise['Schedule_Date'].strftime('%Y-%m-%d')

        print(eachCruise)
    return cruiseList


def checkAvailableCars(Car_Company,Car_Type):
    connection = connect_db()
    query = "SELECT * FROM Car WHERE Car_Company = '" + str(Car_Company) +"' AND Car_Type = '" + str(Car_Type) + "';"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    carList = cursor.fetchall()
    connection.close()

    return carList
