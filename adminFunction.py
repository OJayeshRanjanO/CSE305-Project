from dbConnect import *
import datetime
def listAllFlights():
    connection = connect_db()
    query = "SELECT FlightID, " \
            "Flight_Number, Flight_Carrier, Class," \
            "(SELECT City FROM Location WHERE Src_Location = LocationID) AS Src_Location," \
            "(SELECT City FROM Location WHERE Dst_Location = LocationID) AS Dst_Location," \
            "(SELECT Active FROM Transportation WHERE TransportationID = FlightID) AS Active ," \
            "Fare, Schedule_Date FROM Flight ORDER BY FlightID DESC"

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

def listAllCruises():
    connection = connect_db()
    query = "SELECT CruiseID, Cruise_Name, Schedule_Date, Fare," \
            "(SELECT City FROM Location WHERE Src_Location = LocationID) AS Src_Location," \
            "(SELECT City FROM Location WHERE Dst_Location = LocationID) AS Dst_Location," \
            "(SELECT Active FROM Transportation WHERE TransportationID = CruiseID) AS Active " \
            "FROM Cruise ORDER BY CruiseID DESC"

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cruiseList = cursor.fetchall()
    connection.close()
    # This is a list of dictionaries, Each row is a dictionary
    # Use this loop to convert datetime
    for eachCruise in cruiseList:
        eachCruise['Schedule_Date'] = eachCruise['Schedule_Date'].strftime('%Y-%m-%d')

        # print(eachFlight)
    return cruiseList

def listAllCars():
    connection = connect_db()
    query = "SELECT CarID,(SELECT Active FROM Transportation WHERE TransportationID = CarID) AS Active ,Car_Company,Car_Type FROM Car ORDER BY CarID DESC"

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    carsList = cursor.fetchall()
    connection.close()
    return carsList

def listAllHotels():
    connection = connect_db()
    query = "SELECT AccommodationID,Accommodation_Type,Facilities,Size," \
            "(SELECT City FROM Location WHERE Location = LocationID) AS Location" \
            " FROM Accommodation ORDER BY AccommodationID DESC"

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    carsList = cursor.fetchall()
    connection.close()
    return carsList

def toggleResourceOnOff(nodeValue):
    nodeValue = nodeValue.split("-")
    connection = connect_db()
    # query = "UPDATE "+ str(nodeValue[0]) + " SET "
    if nodeValue[0] == "Accommodation":
        query = "SELECT Active FROM " + str(nodeValue[0]) + " WHERE AccommodationID = " + str(nodeValue[1])
    else:
        query = "SELECT Active FROM Transportation WHERE TransportationID = " + str(nodeValue[1])
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    result = 0 if (cursor.fetchall()[0])['Active'] == 1 else 1
    connection.close()

    print(query)

    connection = connect_db()
    if nodeValue[0] == "Accommodation":
        query = "UPDATE Accommodation SET Active = " + str(result) + " WHERE AccommodationID = " + str(nodeValue[1])
    else:
        query = "UPDATE Transportation SET Active = " + str(result) + " WHERE TransportationID = " + str(nodeValue[1])
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

    print(query)
    return None

def addCarResource(price,car_type,car_company):
    connection = connect_db()
    query = "INSERT INTO Transportation (Transportation_Type,Active) VALUES ('Car',1);"
    cursor = connection.cursor()
    cursor.execute(query)
    print(query)

    query = "SELECT * FROM Transportation ORDER BY TransportationID DESC LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(query)
    data = (cursor.fetchall())[0]
    print(query)

    id = data['TransportationID']

    query = "INSERT INTO Car (CarID,Car_Company,Car_Type,Rent) VALUES (" + str(id) + ",\'"+ str(car_company) +"\',\'" + str(car_type) + "\'," + str(price) + ");"
    cursor = connection.cursor()
    cursor.execute(query)
    print(query)

    query = "INSERT INTO Employee_Manages_Resources (EmployeeID,TransportationID) VALUES ((SELECT EmployeeID FROM Employee WHERE Role = 'Admin' ORDER BY RAND() LIMIT 1),"+str(id)+");"
    cursor = connection.cursor()
    cursor.execute(query)
    print(query)


    connection.commit()
    connection.close()


if __name__ == '__main__':
    connection = connect_db()

    query = "SELECT * FROM Flight"

    cursor = connection.cursor()
    cursor.execute(query)
    print(cursor.fetchall())
    connection.commit()
    connection.close()
