from dbConnect import *

def checkPassengerCredentials(email,password):
    try:
        connection = connect_db()
        query = "SELECT * FROM Passenger where Email = %s AND Password = Password( %s )"
        print(query)
        cursor = connection.cursor()
        cursor.execute(query,(email,password))
        data = cursor.fetchall()
        connection.close()
        print(data)
        return False if len(data) == 0 else True
    except:
        connection.close()
        return False

def registerPassenger():
    return None
