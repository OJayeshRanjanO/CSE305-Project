from dbConnect import *
import datetime

def checkAvailableFlights(flightFrom,flightTo,flightLeavingDate,flightClass,flightPassengers):
    # try:
        print(flightFrom,flightTo,flightLeavingDate,flightClass,flightPassengers)
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
        query = "SELECT * FROM Flight WHERE Src_Location = " + str(src_location) + " AND Dst_Location = " + str(dst_location) + " AND Class = '" + str(flightClass) + "' AND Schedule_Date >= \'"+flightLeavingDate+" 00:00:00' AND Schedule_Date <= \'"+flightLeavingDate+" 23:59:59' AND (SELECT TransportationID FROM Transportation WHERE TransportationID = FlightID AND Active = 1);"
        cursor = connection.cursor()
        cursor.execute(query)
        flightList = cursor.fetchall()
        connection.close()
        print(query)

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
    query = "SELECT * FROM Cruise WHERE Src_Location = " + str(src_location) +" AND Dst_Location = " + str(dst_location) + " AND Schedule_Date >= \'"+cruiseLeavingDate+" 00:00:00' AND Schedule_Date <= \'"+cruiseLeavingDate+" 23:59:59' AND (SELECT TransportationID FROM Transportation WHERE TransportationID = CruiseID AND Active = 1);"
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
    print("TEST",accommodation_list)
    return accommodation_list

def generateCheckoutList(cartList):
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

def payTripFinal(userInfo,partySize,email,itemList):
    car_list,flight_list,cruise_list,acccommodation_list = itemList
    connection = connect_db()
    query = "INSERT INTO Party(Party_Leader, Party_Size, Active) VALUES ("+ \
            str("(SELECT PassengerID FROM Passenger WHERE Email = \'"+ email +"\' )")+\
            ","+ str(partySize)+",1);"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

    query = "SELECT PartyID FROM Party ORDER BY PartyID DESC LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(query)
    data = (cursor.fetchall())[0]
    print(query)

    id = data['PartyID']

    query = "INSERT INTO Employee_Helps_Party (EmployeeID,PartyID) VALUES ((SELECT EmployeeID FROM Employee WHERE Role = 'CSR' ORDER BY RAND() LIMIT 1),"+str(id)+");"
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    print(query)

    query = "INSERT INTO Passenger_MemberOf_Party(PassengerID, PartyID) VALUES ("+\
            str("(SELECT PassengerID FROM Passenger WHERE Email = \'"+ email +"\' )")+\
            ","+ str(id)+");"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    print()

    #Add to Relationship Types
    for data in acccommodation_list:
        query = "INSERT INTO Party_Books_Accommodation (PartyID,AccommodationID) VALUES ("+str(id)+","+ str(data['AccommodationID']) +");"
        print(query)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        # print(cursor.fetchall())
        print()
    for data in cruise_list:
        query = "INSERT INTO Party_Selects_Transportation (TransportationID, PartyID) VALUES ("+ str(data['CruiseID']) +","+ str(id) +")"
        print(query)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print(cursor.fetchall())
        print()
    for data in flight_list:
        query = "INSERT INTO Party_Selects_Transportation (TransportationID, PartyID) VALUES ("+ str(data['FlightID']) +","+ str(id) +")"
        print(query)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print(cursor.fetchall())
        print()
    for data in car_list:
        query = "INSERT INTO Party_Selects_Transportation (TransportationID, PartyID) VALUES ("+ str(data['CarID']) +","+ str(id) +")"
        print(query)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print(cursor.fetchall())
        print()

    #Payment# (Payment_Type, Card_Number, Card_Holder_Name ,Card_Exp_Date, Transaction_Time, Amount_Paid)
    query = "INSERT INTO Payment (Payment_Type, Card_Number, Card_Holder_Name ,Card_Exp_Date, Transaction_Time, Amount_Paid) VALUES " \
            "(\'"+str(userInfo[0])+"\',"+str(userInfo[1])+",\'"+str(userInfo[2])+"\',"+userInfo[3]+",now(),"+userInfo[4]+");"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

    query = "INSERT INTO Party_Makes_Payment (PartyID, PaymentID) VALUES ("+str(id)+",(SELECT PaymentID FROM Payment ORDER BY PaymentID DESC LIMIT 1));"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    print()

    connection.close()
    return None

def fetchParty(email):
    connection = connect_db()
    query = "SELECT PartyID,Party_Size FROM Party WHERE Party_Leader = (SELECT PassengerID FROM Passenger WHERE Email = \'"+str(email)+"\')"
    # query = "SELECT * FROM Party_Selects_Transportation"
    cursor = connection.cursor()
    cursor.execute(query)
    partyInfo = cursor.fetchall()
    print(partyInfo)
    print()
    finalList,transportList = {},{}

    #All Transportation Info From PARTY SELECTS TRANSPORTATION
    for party in partyInfo:
        query = "SELECT " \
                "(SELECT Transportation.Transportation_Type FROM Transportation WHERE Transportation.TransportationID = PST.TransportationID) AS Type," \
                " TransportationID FROM Party_Selects_Transportation AS PST WHERE " \
                "PartyID = " + str(party['PartyID']) + ""
        cursor = connection.cursor()
        cursor.execute(query)
        lst = cursor.fetchall()
        transportList[party['PartyID']] = lst
    print()
    print(transportList)
    for key in transportList.keys():
        value = transportList[key]
        for i in range(len(value)):
            types = value[i]
            if types['Type'] == "Car":
                query = "SELECT * FROM "+str(types['Type'])+" WHERE "+str(types['Type'])+"ID = "+str(types['TransportationID'])+""
            else:
                query = "SELECT *,(SELECT City FROM Location WHERE Location.LocationID = Src_Location) AS Src," \
                        "(SELECT City FROM Location WHERE Location.LocationID = Dst_Location) AS Dst " \
                        " FROM "+str(types['Type'])+" WHERE "+str(types['Type'])+"ID = "+str(types['TransportationID'])+""
            # print(query)
            cursor = connection.cursor()
            cursor.execute(query)
            tempValue = cursor.fetchall()[0]
            if 'Schedule_Date' in tempValue:
                tempValue['Schedule_Date'] = tempValue['Schedule_Date'].strftime('%Y-%m-%d')
            # print(tempValue)
            value[i] = tempValue
    # print(transportList)
    print()

    #All Accommodation Info From Party_Books_Accommodation
    for party in partyInfo:
        query = "SELECT AccommodationID, (SELECT Accommodation_Type FROM Accommodation WHERE PBA.AccommodationID = Accommodation.AccommodationID) AS Accommodation_Type, " \
                " (SELECT Rate FROM Accommodation WHERE PBA.AccommodationID = Accommodation.AccommodationID) AS Rate," \
                " (SELECT Facilities FROM Accommodation WHERE PBA.AccommodationID = Accommodation.AccommodationID) AS Facilities," \
                " (SELECT Discount FROM Accommodation WHERE PBA.AccommodationID = Accommodation.AccommodationID) AS Discount," \
                " (SELECT (SELECT City FROM Location WHERE Location.LocationID = Accommodation.Location) FROM Accommodation WHERE PBA.AccommodationID = Accommodation.AccommodationID) AS Location " \
                "FROM Party_Books_Accommodation AS PBA WHERE " \
                "PartyID = " + str(party['PartyID']) + ""
        # query = "SELECT * FROM Accommodation"
        cursor = connection.cursor()
        cursor.execute(query)
        lst = cursor.fetchall()

        finalList[party['PartyID']] = list(lst) + list(transportList[party['PartyID']])
        # print(lst)
    print()
    # print(hotelsList)

    connection.close()

    return finalList,partyInfo

def getReviewList(item):
    item = item.split("-")
    resource = "AccommodationID" if item[0] == "Accommodation" else "CruiseID"
    ID = item[1]

    connection = connect_db()

    query = "SELECT (SELECT Name FROM Passenger WHERE Passenger.PassengerID = PRR.PassengerID) AS Name, (SELECT Email FROM Passenger WHERE Passenger.PassengerID = PRR.PassengerID) AS Email ,Review_Details,Rating FROM Passenger_Reviews_Resources AS PRR WHERE " + str(resource) +" = " + str(ID)
    cursor = connection.cursor()
    cursor.execute(query)
    reviews = cursor.fetchall()
    connection.close()

    return reviews

def setReview(item,comment,rating,email):
    item = item.split("-")

    connection = connect_db()
    if item[0] == "Accommodation":
       query = "INSERT INTO Passenger_Reviews_Resources(PassengerID, AccommodationID,Review_Details,Rating) VALUES" \
    " ("+ str("(SELECT PassengerID FROM Passenger WHERE Email = \'"+ email +"\' )") +","+ str(item[1])+",\'"+ comment +"\',"+ str(rating)+");"
    else:
        query = "INSERT INTO Passenger_Reviews_Resources(PassengerID, CruiseID,Review_Details,Rating) VALUES" \
    " ("+ str("(SELECT PassengerID FROM Passenger WHERE Email = \'"+ email +"\' )") +","+ str(item[1])+",\'"+ comment +"\',"+ str(rating)+");"
    print("TEST " + query)
    cursor = connection.cursor()
    cursor.execute(query)
    print()
    connection.commit()
    connection.close()




# if __name__ == '__main__':
#     connection = connect_db()
#     email = "passenger1@test.com"
#     connection = connect_db()
#     query = "SELECT PartyID,Party_Size FROM Party WHERE Party_Leader = (SELECT PassengerID FROM Passenger WHERE Email = \'"+str(email)+"\')"
#     # query = "SELECT * FROM Party_Selects_Transportation"
#     cursor = connection.cursor()
#     cursor.execute(query)
#     partyInfo = cursor.fetchall()
#     print(partyInfo)
#     print()
#     finalList,transportList = {},{}
#
#     #All Transportation Info From PARTY SELECTS TRANSPORTATION
#     for party in partyInfo:
#         query = "SELECT " \
#                 "(SELECT Transportation.Transportation_Type FROM Transportation WHERE Transportation.TransportationID = PST.TransportationID) AS Type," \
#                 " TransportationID FROM Party_Selects_Transportation AS PST WHERE " \
#                 "PartyID = " + str(party['PartyID']) + ""
#         cursor = connection.cursor()
#         cursor.execute(query)
#         lst = cursor.fetchall()
#         transportList[party['PartyID']] = lst
#     print()
#     print(transportList)
#     for key in transportList.keys():
#         value = transportList[key]
#         for i in range(len(value)):
#             types = value[i]
#             if types['Type'] == "Car":
#                 query = "SELECT * FROM "+str(types['Type'])+" WHERE "+str(types['Type'])+"ID = "+str(types['TransportationID'])+""
#             else:
#                 query = "SELECT *,(SELECT City FROM Location WHERE Location.LocationID = Src_Location) AS Src," \
#                         "(SELECT City FROM Location WHERE Location.LocationID = Dst_Location) AS Dst " \
#                         " FROM "+str(types['Type'])+" WHERE "+str(types['Type'])+"ID = "+str(types['TransportationID'])+""
#             # print(query)
#             cursor = connection.cursor()
#             cursor.execute(query)
#             tempValue = cursor.fetchall()[0]
#             if 'Schedule_Date' in tempValue:
#                 tempValue['Schedule_Date'] = tempValue['Schedule_Date'].strftime('%Y-%m-%d')
#             # print(tempValue)
#             value[i] = tempValue
#     # print(transportList)
#     print()
#
#     #All Accommodation Info From Party_Books_Accommodation
#     for party in partyInfo:
#         query = "SELECT AccommodationID, (SELECT Accommodation_Type FROM Accommodation WHERE PBA.AccommodationID = Accommodation.AccommodationID) AS Accommodation_Type, " \
#                 " (SELECT Rate FROM Accommodation WHERE PBA.AccommodationID = Accommodation.AccommodationID) AS Rate," \
#                 " (SELECT Facilities FROM Accommodation WHERE PBA.AccommodationID = Accommodation.AccommodationID) AS Facilities," \
#                 " (SELECT Discount FROM Accommodation WHERE PBA.AccommodationID = Accommodation.AccommodationID) AS Discount," \
#                 " (SELECT (SELECT City FROM Location WHERE Location.LocationID = Accommodation.Location) FROM Accommodation WHERE PBA.AccommodationID = Accommodation.AccommodationID) AS Location " \
#                 "FROM Party_Books_Accommodation AS PBA WHERE " \
#                 "PartyID = " + str(party['PartyID']) + ""
#         # query = "SELECT * FROM Accommodation"
#         cursor = connection.cursor()
#         cursor.execute(query)
#         lst = cursor.fetchall()
#
#         finalList[party['PartyID']] = list(lst) + list(transportList[party['PartyID']])
#         # print(lst)
#     print()
#     # print(hotelsList)
#
#     connection.close()




