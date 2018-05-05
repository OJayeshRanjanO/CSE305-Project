from dbConnect import *

def checkPassengerCredentials(email,password):
    connection = connect_db()
    query = "SELECT * FROM Passenger where Email = \'"+email+"\' AND Password = Password(\'"+password+"\')"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    print(len(data))
    if len(data) != 0:
        connection.close()
        return "Passenger"
    query = "SELECT * FROM Employee where Email = \'"+email+"\' AND Password = Password(\'"+password+"\')"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    if len(data) != 0:
        connection.close()
        return "Employee"
    connection.close()
    return "None"


def registerPassenger(name, gender, age, email, password):
    connection = connect_db()
    query = "SELECT * FROM Passenger WHERE Email = \'" + str(email) + "\'"
    cursor = connection.cursor()
    cursor.execute(query)
    if len(cursor.fetchall()) != 0:
        return False

    query = "SELECT * FROM Employee WHERE Email = \'" + str(email) + "\'"
    cursor = connection.cursor()
    cursor.execute(query)
    if len(cursor.fetchall()) != 0:
        return False

    query = "INSERT INTO Passenger (Name, Gender, Age, Email, Password) VALUES (%s, %s, %s, %s, Password(\'"+ password +"\'))"
    data = (name, gender, age, email)
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()
    connection.close()
    return True


