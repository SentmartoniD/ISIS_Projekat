import mysql.connector

DATABASE_NAME = "isisdatabase"


def create_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root"
    )
    my_cursor = db.cursor()
    my_cursor.execute("SHOW DATABASES")
    databases = [database[0] for database in my_cursor.fetchall()]
    if DATABASE_NAME not in databases:
        my_cursor.execute(f"CREATE DATABASE {DATABASE_NAME}")
    my_cursor.close()
    db.close()
    return


def table_exists(cursor, table_name):
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    return cursor.fetchone() is not None


def create_us_holidays_table():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database=f"{DATABASE_NAME}"
    )
    my_cursor = db.cursor()
    if not table_exists(my_cursor, 'USHolidays'):
        my_cursor.execute("CREATE TABLE USHolidays (USH_ID int PRIMARY KEY AUTO_INCREMENT, year smallint UNSIGNED, "
                          "day VARCHAR(10),  date VARCHAR(11), holiday_name VARCHAR(50))")
    my_cursor.close()
    db.close()
    return
