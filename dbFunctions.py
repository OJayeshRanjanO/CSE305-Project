from dbConnect import connect_db


def register_user():
    #This is just test CODE
    connection = connect_db()
    query = "CREATE TABLE TEST (A INT, B INT)"
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    register_user()
