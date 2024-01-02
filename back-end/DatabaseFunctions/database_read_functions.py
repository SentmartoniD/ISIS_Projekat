import mysql.connector

DATABASE_NAME = "isisdatabase"

# READ OPERATIONS


def read_from_usholidays_table():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database=f"{DATABASE_NAME}"
    )
    my_cursor = db.cursor()
    my_cursor.execute("SELECT * FROM WeatherData")
    result = my_cursor.fetchall()
    my_cursor.close()
    db.close()
    return result


def read_from_loaddata_table():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database=f"{DATABASE_NAME}"
    )
    my_cursor = db.cursor()
    my_cursor.execute("SELECT * FROM LoadData")
    result = my_cursor.fetchall()
    my_cursor.close()
    db.close()
    return result


def read_from_weatherdata_table():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database=f"{DATABASE_NAME}"
    )
    my_cursor = db.cursor()
    my_cursor.execute("SELECT * FROM USHolidays")
    result = my_cursor.fetchall()
    my_cursor.close()
    db.close()
    return result
