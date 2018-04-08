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
