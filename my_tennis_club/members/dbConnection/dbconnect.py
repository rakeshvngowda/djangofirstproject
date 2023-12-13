import mysql.connector



def connect_to_mysql(host,database,user,password,query):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        if connection.is_connected():
            print("Connected to mysql database")
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)

        results = cursor.fetchall()
        print(results)
        cursor.close()
        connection.close()
        return results
    except mysql.connector.Error as error:
        print(f"Error connecting to MySQL database: {error}")


