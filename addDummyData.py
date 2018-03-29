from dbConnect import connect_db
import random

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
    Car_Types = ['Compact','Economy','Mid-Size','Full-Size','Premium','Luxury','Minivan','Convertible','SUV']
    price = 25
    for i in Car_Types:
        query = "INSERT INTO Transportation (Transportation_Type) VALUES ('Car');"
        cursor = connection.cursor()
        cursor.execute(query)
        print(query)

        query = "SELECT * FROM Transportation ORDER BY TransportationID DESC LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(query)
        data = (cursor.fetchall())[0]
        print(query)

        id = data['TransportationID']

        query = "INSERT INTO Car (CarID,Car_Type,Rent) VALUES (" + str(id) + ",\'" + i + "\'," + str(price) + ");"
        price += 10
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





if __name__ == '__main__':
    # init_Location()
    init_Car()
