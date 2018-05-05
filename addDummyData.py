from dbConnect import connect_db
import random

def init_Employee():
    SupervisorID = 1
    email = ['employee1@test.com','employee2@test.com']
    Role = ['CSR','Admin']
    Date = "DATE_SUB(now(), INTERVAL 2 MONTH)"
    # Date = "now()"
    Salary = 10000
    connection = connect_db()
    for i in range(len(email)):
        query = "INSERT INTO Employee (SupervisorID,Email,Password,Role,Date_Joined,Salary) VALUES " \
        "("+ str(SupervisorID) +",\'"+ email[i] +"\',Password(\'"+ email[i] +"\'),\'"+ Role[i] +"\',"+ Date +","+ str(Salary) +");"
        print(query)
        cursor = connection.cursor()
        cursor.execute(query)
        print()
    connection.commit()
    connection.close()


def init_Transportation():
    # for i in range(7):
    type = ['Car','Cruise','Flight']
    connection = connect_db()
    query = "INSERT INTO Transportation (Transportation_Type) VALUES (\'" + random.choice(type) + "\');"
    # query = "INSERT INTO Transportation (Transportation_Type) VALUES (\'" + type[2] + "\');"
    cursor = connection.cursor()
    cursor.execute(query)

    query = "SELECT * FROM Transportation ORDER BY TransportationID DESC LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(query)
    data = (cursor.fetchall())[0]
    if data['Transportation_Type'] == 'Car':
        init_Car()

    connection.commit()
    connection.close()

def init_Car():
    connection = connect_db()
    Car_Types = ['Economy','Premium','SUV']
    Car_Company = ['Hertz']
    price = 25
    for i in Car_Types:
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

        query = "INSERT INTO Car (CarID,Car_Company,Car_Type,Rent) VALUES (" + str(id) + ",\'"+ str(Car_Company[0]) +"\',\'" + i + "\'," + str(price) + ");"
        price += 10
        cursor = connection.cursor()
        cursor.execute(query)
        print(query)

        query = "INSERT INTO Employee_Manages_Resources (EmployeeID,TransportationID) VALUES ((SELECT EmployeeID FROM Employee WHERE Role = 'Admin' ORDER BY RAND() LIMIT 1),"+str(id)+");"
        cursor = connection.cursor()
        cursor.execute(query)
        print(query)

        print()

    connection.commit()
    connection.close()

def init_Flight():
    #4 Beijing
    #1 Moscow
    #2 New York
    #3 New Delhi
    connection = connect_db()
    Flight_Carrier = ['Aeroflot','China Eastern']
    Flight_Number = ['AF1','CE1']
    Schedule_Date = ['2018-03-30 08:09:13','2018-03-31 08:09:13']
    Src_Location = [2,1]
    Dst_Location = [1,2]
    Fare = [100,200]
    Class = ['Economy',"Business"]
    for i in range(len(Flight_Carrier)):
        for j in Class:
            query = "INSERT INTO Transportation (Transportation_Type,Active) VALUES ('Flight',1);"
            cursor = connection.cursor()
            cursor.execute(query)
            print(query)

            query = "SELECT * FROM Transportation ORDER BY TransportationID DESC LIMIT 1"
            cursor = connection.cursor()
            cursor.execute(query)
            data = (cursor.fetchall())[0]
            print(query)

            id = data['TransportationID']
            query = "INSERT INTO Flight (FlightID,Flight_Carrier,Flight_Number,Schedule_Date,Src_Location,Dst_Location,Class,Fare) " \
                    "VALUES (" + str(id) + ",\'" + Flight_Carrier[i] + "\',\'" + Flight_Number[i] + "\',\'" + Schedule_Date[i] + "\'," + str(Src_Location[i]) + "," \
                    "" + str(Dst_Location[i]) + ",\'" + j + "\'," + ( str(Fare[i]/2) if j == 'Economy' else str(Fare[i]) ) + ");"
            cursor = connection.cursor()
            cursor.execute(query)
            print(query)

            query = "INSERT INTO Employee_Manages_Resources (EmployeeID,TransportationID) VALUES ((SELECT EmployeeID FROM Employee WHERE Role = 'Admin' ORDER BY RAND() LIMIT 1),"+str(id)+");"
            cursor = connection.cursor()
            cursor.execute(query)
            print(query)

            print()

    connection.commit()
    connection.close()

def init_Cruise():
    #4 Beijing
    #1 Moscow
    #2 New York
    #3 New Delhi
    connection = connect_db()
    Cruise_Name = ['Maid of the Mists','Caribbean Princess','Black Perl']
    Schedule_Date = ['2018-03-30 08:09:13','2018-03-31 08:09:13','2018-04-01 00:00:00']
    Src_Location = [4,1,2]
    Dst_Location = [1,4,2]
    Fare = [600,700,800]
    for i in range(len(Cruise_Name)):
        query = "INSERT INTO Transportation (Transportation_Type,Active) VALUES ('Cruise',1);"
        cursor = connection.cursor()
        cursor.execute(query)
        print(query)

        query = "SELECT * FROM Transportation ORDER BY TransportationID DESC LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(query)
        data = (cursor.fetchall())[0]
        print(query)

        id = data['TransportationID']
        query = "INSERT INTO Cruise (CruiseID,Cruise_Name,Schedule_Date,Src_Location,Dst_Location,Fare) " \
                "VALUES (" + str(id) + ",\'" + Cruise_Name[i] + "\',\'" + Schedule_Date[i] + "\'," + str(Src_Location[i]) + "," \
                "" + str(Dst_Location[i]) + "," + str(Fare[i]) + ");"
        cursor = connection.cursor()
        cursor.execute(query)
        print(query)

        query = "INSERT INTO Employee_Manages_Resources (EmployeeID,TransportationID) VALUES ((SELECT EmployeeID FROM Employee WHERE Role = 'Admin' ORDER BY RAND() LIMIT 1),"+str(id)+");"
        cursor = connection.cursor()
        cursor.execute(query)
        print(query)

        print()

    connection.commit()
    connection.close()

def init_Location():
    city = ['Moscow','Queens','New Delhi','Beijing']
    state = ['Moscow','New York','New Delhi','Hebei']
    country = ['Russia','USA','India','China']

    connection = connect_db()
    for i in range(len(city)):
        query = "INSERT INTO Location (City,State,Country) VALUES (\'"+ city[i] +"\',\'"+ state[i] +"\',\'"+ country[i] +"\');"
        print(query)
        # query = "INSERT INTO Transportation (Transportation_Type) VALUES (\'" + type[2] + "\');"
        cursor = connection.cursor()
        cursor.execute(query)
    connection.commit()
    connection.close()

def init_Accomodation():

    Accommodation_Type = ['Economy','King','Suite']
    Rate = [100,200,300]
    Facilities = ['2 Beds','2 Beds and Minibar','2 Beds, Minibar and Business Room']
    Location = [1,2,3]
    Size = [2,2,4]
    connection = connect_db()
    for i in range(len(Accommodation_Type)):
        query = "INSERT INTO Accommodation (Accommodation_Type,Rate,Facilities,Discount,Location,Size,Active) VALUES " \
        "(\'"+ Accommodation_Type[i] +"\',"+ str(Rate[i]) +",\'"+ Facilities[i] +"\',"+ str(0.0) +","+ str(Location[i]) +","+ str(Size[i]) +","+ str(1) +");"
        print(query)
        # query = "INSERT INTO Transportation (Transportation_Type) VALUES (\'" + type[2] + "\');"
        cursor = connection.cursor()
        cursor.execute(query)

        query = "SELECT AccommodationID FROM Accommodation ORDER BY AccommodationID DESC LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(query)
        data = (cursor.fetchall())[0]
        print(query)

        id = data['AccommodationID']
        query = "INSERT INTO Employee_Manages_Resources (EmployeeID,AccommodationID) VALUES ((SELECT EmployeeID FROM Employee WHERE Role = 'Admin' ORDER BY RAND() LIMIT 1),"+str(id)+");"
        cursor = connection.cursor()
        cursor.execute(query)
        print(query)

        print()

    connection.commit()
    connection.close()

def init_Passenger():
    Name = ["Jay","Feazan","Lucy"]
    email = ['passenger1@test.com','passenger2@test.com','passenger3@test.com']
    Gender = ["Male","Male","Female"]
    Age = [21,21,21]
# Password(\'"+ email[i] +"\'),
    connection = connect_db()
    for i in range(len(email)):
        query = "INSERT INTO Passenger (Name,Gender,Age,Email,Password) VALUES " \
        "(\'"+str( Name[i]) +"\',\'"+ Gender[i] +"\',"+ str(Age[i]) +",\'"+ email[i] +"\', Password(\'"+ email[i] +"\'));"
        print(query)
        cursor = connection.cursor()
        cursor.execute(query)

        print()

    connection.commit()
    connection.close()

def init_Passenger_Reviews_Resources():
    PassengerID = 1
    CruiseID = 8
    CruiseReview = "This is a cruise review"
    Rating = 5;
    #Passenger Reviews Cruise
    connection = connect_db()
    query = "INSERT INTO Passenger_Reviews_Resources(PassengerID, CruiseID,Review_Details,Rating) VALUES" \
    " ("+ str(PassengerID)+","+ str(CruiseID)+",\'"+ CruiseReview+"\',"+ str(Rating)+");"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    print()
    connection.commit()
    connection.close()

    #Passenger Reviews Accommodation
    AccommodationReview = "This is a accommodation review"
    AccommodationID = 1
    PassengerID = 2
    connection = connect_db()
    query = "INSERT INTO Passenger_Reviews_Resources(PassengerID, AccommodationID,Review_Details,Rating) VALUES" \
    " ("+ str(PassengerID)+","+ str(AccommodationID)+",\'"+ AccommodationReview +"\',"+ str(Rating)+");"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    print()

    connection.commit()
    connection.close()

def init_Party():
    Party_Leader = [1,3,1]
    Party_Size = [5,5,3]
    connection = connect_db()
    for i in range(len(Party_Leader)):
        query = "INSERT INTO Party(Party_Leader, Party_Size, Active) VALUES ("+ str(Party_Leader[i])+","+ str(Party_Size[i])+",1);"
        print(query)
        cursor = connection.cursor()
        cursor.execute(query)

        query = "SELECT PartyID FROM Party ORDER BY PartyID DESC LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(query)
        data = (cursor.fetchall())[0]
        print(query)

        id = data['PartyID']
        query = "INSERT INTO Employee_Helps_Party (EmployeeID,PartyID) VALUES ((SELECT EmployeeID FROM Employee WHERE Role = 'CSR' ORDER BY RAND() LIMIT 1),"+str(id)+");"
        cursor = connection.cursor()
        cursor.execute(query)
        print(query)

        query = "INSERT INTO Passenger_MemberOf_Party(PassengerID, PartyID) VALUES ("+ str(Party_Leader[i])+","+ str(id)+");"
        print(query)
        cursor = connection.cursor()
        cursor.execute(query)
        print()

    connection.commit()
    connection.close()

def init_Party_Selects_Transportation():
    connection = connect_db()
    query = "SELECT PartyID FROM Party ORDER BY PartyID DESC LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(query)
    lastPartyID = ((cursor.fetchall())[0])['PartyID']
    print(query)

    TransportationIDQuery = "(SELECT FlightID FROM Flight WHERE Src_Location = (SELECT LocationID FROM Location WHERE City = 'Queens') AND Dst_Location = (SELECT LocationID FROM Location Where City = 'Moscow') AND Class = 'Economy')"
    query = "INSERT INTO Party_Selects_Transportation (TransportationID, PartyID) VALUES ("+ TransportationIDQuery +","+ str(lastPartyID) +")"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    print()

    connection.commit()
    connection.close()

def init_Party_Books_Accommodation():
    connection = connect_db()
    query = "SELECT PartyID FROM Party ORDER BY PartyID DESC LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(query)
    lastPartyID = ((cursor.fetchall())[0])['PartyID']
    print(query)

    query = "INSERT INTO Party_Books_Accommodation (PartyID,AccommodationID) VALUES ("+ str(lastPartyID) +",(SELECT AccommodationID FROM Accommodation WHERE Location = (SELECT LocationID From Location where City = 'Moscow') AND Accommodation_Type = 'Economy') );"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    print()

    connection.commit()
    connection.close()


def init_Party_Default_Payment():
    connection = connect_db()
    query = "INSERT INTO Payment (Payment_Type, Card_Number, Card_Holder_Name ,Card_Exp_Date, Transaction_Time, Amount_Paid) VALUES ('VISA',1234567890123456,'Jay R',now(),now(),0);"
    cursor = connection.cursor()
    cursor.execute(query)

    query = "INSERT INTO Party_Makes_Payment (PartyID, PaymentID) VALUES (1,1);"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    print()

    connection.commit()
    connection.close()

if __name__ == '__main__':
    init_Employee()
    init_Location()
    init_Car()
    init_Flight()
    init_Cruise()
    init_Accomodation()
    init_Passenger()
    init_Passenger_Reviews_Resources()
    init_Party()
    init_Party_Selects_Transportation()
    init_Party_Books_Accommodation()
    init_Party_Default_Payment()
