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
    my_cursor.execute("SELECT * FROM USHolidays")
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


def read_from_weatherdata_table_all():
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


def read_from_weatherdata_table_by_dates(start_date, end_date):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database=f"{DATABASE_NAME}"
    )
    my_cursor = db.cursor()
    #my_cursor.execute("select datetime from weatherdata where datetime BETWEEN (select datetime from weatherdata where (substring(datetime, 1, 10) = '2020-01-11') and substring(datetime, 12, 2) = '00') and (select datetime from weatherdata where (substring(datetime, 1, 10) = '2020-01-15' and substring(datetime, 12, 2) = '00')) ",)
    sql_query = """
    SELECT *
    FROM weatherdata
    WHERE datetime BETWEEN 
        (SELECT datetime FROM weatherdata WHERE SUBSTRING(datetime, 1, 10) = %s AND SUBSTRING(datetime, 12, 2) = '00') 
        AND 
        (SELECT datetime FROM weatherdata WHERE SUBSTRING(datetime, 1, 10) = %s AND SUBSTRING(datetime, 12, 2) = '00')
    """
    my_cursor.execute(sql_query, (start_date, end_date))
    result = my_cursor.fetchall()
    my_cursor.close()
    db.close()
    return result
