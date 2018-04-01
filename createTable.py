from dbConnect import connect_db

def Payment():
    connection = connect_db()
    query = """
CREATE TABLE Payment (
 PaymentID INTEGER NOT NULL AUTO_INCREMENT,
 Payment_Type VARCHAR(40) NOT NULL,
 Card_Number BIGINT NOT NULL,
 Card_Holder_Name VARCHAR(255) NOT NULL,
 Card_Exp_Date DATE NOT NULL,
 Transaction_Time TIMESTAMP NOT NULL,
 Amount_Paid DOUBLE NOT NULL DEFAULT 0,
CHECK (Card_Number >= 1000000000000000 AND Card_Number <= 9999999999999999),
CHECK(Card_Exp_Date > now()),
 PRIMARY KEY (PaymentID)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def Party():
    connection = connect_db()
    query = """
CREATE TABLE Party (
PartyID INTEGER NOT NULL AUTO_INCREMENT,
Party_Size INT NOT NULL,
Party_Leader INT NOT NULL,
CHECK (Party_Size > 0),
PRIMARY KEY (PartyID),
FOREIGN KEY (Party_Leader) References Passenger (PassengerID)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def Passenger():
    connection = connect_db()
    query = """
CREATE TABLE Passenger (
PassengerID INT NOT NULL AUTO_INCREMENT,
Name VARCHAR(255) NOT NULL,
Gender ENUM('Male','Female') NOT NULL,
Age TINYINT NOT NULL,
Email VARCHAR(255) NOT NULL,
Password VARCHAR(255) NOT NULL,
PRIMARY KEY (PassengerID),
UNIQUE (Email)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def Location():
    connection = connect_db()
    query = """
CREATE TABLE Location (
LocationID INT NOT NULL AUTO_INCREMENT,
City VARCHAR(255) NOT NULL,
State VARCHAR(255) NOT NULL,
Country VARCHAR(255) NOT NULL,
UNIQUE (City, State, Country),
PRIMARY KEY(LocationID)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def Transportation():
    connection = connect_db()
    query = """
CREATE TABLE Transportation (
TransportationID INT NOT NULL AUTO_INCREMENT,
Transportation_Type ENUM('Car','Flight','Cruise'),
Active TINYINT(1) NOT NULL DEFAULT 1,
PRIMARY KEY (TransportationID)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def Car():
    connection = connect_db()
    query = """
CREATE TABLE Car (
CarID INT NOT NULL,
Car_Company VARCHAR(255) NOT NULL,
Car_Type Enum('Economy','Premium','SUV') NOT NULL,
Rent DOUBLE NOT NULL,
CHECK (Rent >= 0),
UNIQUE (CarID),
UNIQUE (Car_Type,Rent),
FOREIGN KEY (CarID) REFERENCES Transportation (TransportationID)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def Flight():
    connection = connect_db()
    query = """
CREATE TABLE Flight (
FlightID INT NOT NULL,
Flight_Carrier VARCHAR(255) NOT NULL,
Flight_Number VARCHAR(255) NOT NULL,
Schedule_Date DATETIME NOT NULL,
Src_Location INT NOT NULL,
Dst_Location INT NOT NULL,
Class ENUM('Business','Economy'),
Fare DOUBLE NOT NULL,
CHECK(Src_Location != Dst_Location),
CHECK (Fare >= 0),
UNIQUE (FlightID),
UNIQUE(Flight_Carrier,Flight_Number,Schedule_Date,Src_Location,Dst_Location,Class,Fare),
FOREIGN KEY (FlightID) REFERENCES Transportation (TransportationID),
FOREIGN KEY (Src_Location) REFERENCES Location (LocationID),
FOREIGN KEY (Dst_Location) REFERENCES Location (LocationID)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def Cruise():
    connection = connect_db()
    query = """
CREATE TABLE Cruise (
CruiseID INT NOT NULL,
Cruise_Name VARCHAR (255)NOT NULL,
Schedule_Date DATETIME NOT NULL,
Src_Location INT NOT NULL,
Dst_Location INT NOT NULL,
Fare DOUBLE NOT NULL,
CHECK (Fare >= 0),
UNIQUE(CruiseID),
UNIQUE(Cruise_Name,Src_Location,Dst_Location, Schedule_Date),
FOREIGN KEY (CruiseID) REFERENCES Transportation (TransportationID),
FOREIGN KEY (Src_Location) REFERENCES Location (LocationID),
FOREIGN KEY (Dst_Location) REFERENCES Location (LocationID)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def Accommodation():
    connection = connect_db()
    query = """
CREATE TABLE Accommodation (
AccommodationID INT NOT NULL AUTO_INCREMENT,
Accommodation_Type VARCHAR(255) NOT NULL,
Rate DOUBLE NOT NULL,
Facilities TEXT,
Discount DOUBLE DEFAULT 0.0,
Location INT NOT NULL,
Size INT NOT NULL,
Active TINYINT(1) NOT NULL DEFAULT 1,
CHECK (Size > 0),
CHECK (Rate >= 0),
CHECK (Discount >= 0),
PRIMARY KEY (AccommodationID),
FOREIGN KEY (Location) REFERENCES Location(LocationID)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def Employee():
    connection = connect_db()
    query = """
CREATE TABLE Employee (
EmployeeID INT NOT NULL AUTO_INCREMENT,
SupervisorID INT NOT NULL,
Email VARCHAR(255) NOT NULL,
Password VARCHAR(255) NOT NULL,
Role ENUM('CSR','Admin') NOT NULL,
Date_Joined DATE NOT NULL,
Salary DOUBLE NOT NULL,
CHECK (Date_Joined <= now()),
CHECK (Salary >= 0),
PRIMARY KEY (EmployeeID),
UNIQUE (Email)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


def Party_Makes_Payment():
    connection = connect_db()
    query = """
CREATE TABLE Party_Makes_Payment (
PartyID INT NOT NULL,
PaymentID INT NOT NULL,
UNIQUE(PartyID),
UNIQUE(PaymentID),
FOREIGN KEY (PartyID) REFERENCES Party (PartyID),
FOREIGN KEY (PaymentID) REFERENCES Payment (PaymentID)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def Location_Has_Accommodation ():
    connection = connect_db()
    query = """
CREATE TABLE Location_Has_Accommodation (
LocationID INT NOT NULL,
AccommodationID INT NOT NULL,
UNIQUE(LocationID,AccommodationID),
FOREIGN KEY (LocationID) REFERENCES Location (LocationID),
FOREIGN KEY (AccommodationID) REFERENCES Accommodation (AccommodationID)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def Party_Books_Accommodation():
    connection = connect_db()
    query = """
CREATE TABLE Party_Books_Accommodation (
PartyID INT NOT NULL,
AccommodationID INT NOT NULL,
UNIQUE(PartyID,AccommodationID),
FOREIGN KEY (PartyID) REFERENCES Party (PartyID),
FOREIGN KEY (AccommodationID) REFERENCES Accommodation
(AccommodationID)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def Party_Selects_Transportation():
    connection = connect_db()
    query = """
CREATE TABLE Party_Selects_Transportation (
PartyID INT NOT NULL,
TransportationID INT NOT NULL,
UNIQUE(PartyID,TransportationID),
FOREIGN KEY (PartyID) REFERENCES Party (PartyID),
FOREIGN KEY (TransportationID) REFERENCES Transportation (TransportationID)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def Passenger_MemberOf_Party():
    connection = connect_db()
    query = """
CREATE TABLE Passenger_MemberOf_Party (
PassengerID INT NOT NULL,
PartyID INT NOT NULL,
UNIQUE(PassengerID, PartyID),
FOREIGN KEY (PassengerID) REFERENCES Passenger (PassengerID),
FOREIGN KEY (PartyID) REFERENCES Party (PartyID)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def Employee_Helps_Party ():
    connection = connect_db()
    query = """
CREATE TABLE Employee_Helps_Party (
EmployeeID INT NOT NULL,
PartyID INT NOT NULL,
CHECK((SELECT COUNT(*) FROM Employee WHERE Employee.Role = 'CSR' AND Employee_Helps_Party.EmployeeID = Employee.Role) != 0),
UNIQUE(EmployeeID, PartyID),
FOREIGN KEY (EmployeeID) REFERENCES Employee (EmployeeID),
FOREIGN KEY (PartyID) REFERENCES Party (PartyID)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def Employee_Manages_Resources ():
    connection = connect_db()
    query = """
CREATE TABLE Employee_Manages_Resources (
EmployeeID INT NOT NULL,
TransportationID INT,
AccommodationID INT,
CHECK((SELECT COUNT(*) FROM Employee WHERE Employee.Role = 'Admin' AND Employee_Manages_Resources.EmployeeID = Employee.Role) != 0),
UNIQUE(EmployeeID, TransportationID, AccommodationID),
CHECK ((TransportationID IS NULL XOR AccommodationID IS NULL) = 1),
FOREIGN KEY (EmployeeID) REFERENCES Employee (EmployeeID),
FOREIGN KEY (TransportationID ) REFERENCES Transportation (TransportationID ),
FOREIGN KEY(AccommodationID) REFERENCES Accommodation(AccommodationID)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def Passenger_Reviews_Resources ():
    connection = connect_db()
    query = """
CREATE TABLE Passenger_Reviews_Resources (
PassengerID INT NOT NULL,
CruiseID INT,
AccommodationID INT,
Review_Details TEXT,
Rating TINYINT NOT NULL,
CHECK (RATING >= 1 AND RATING <= 5),
CHECK ( (CruiseID >= 1) XOR (AccommodationID >= 1) ),
UNIQUE(PassengerID,CruiseID),
UNIQUE(PassengerID,AccommodationID),
FOREIGN KEY (PassengerID) REFERENCES Passenger (PassengerID),
FOREIGN KEY (CruiseID ) REFERENCES Cruise (CruiseID ),
FOREIGN KEY(AccommodationID) REFERENCES Accommodation(AccommodationID)
);
"""
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()
if __name__ == '__main__':
    Payment()
    Passenger()
    Party()
    Location()
    Transportation()
    Car()
    Flight()
    Cruise()
    Accommodation()
    Employee()
    Party_Makes_Payment()
    Location_Has_Accommodation()
    Party_Books_Accommodation()
    Party_Selects_Transportation()
    Passenger_MemberOf_Party()
    Employee_Helps_Party()
    Employee_Manages_Resources()
    Passenger_Reviews_Resources()
