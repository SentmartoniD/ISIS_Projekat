import mysql.connector

DATABASE_NAME = "isisdatabase"

# INSERT OPERATIONS


def insert_into_usholidays_table(year, day, date, holiday_name):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database=f"{DATABASE_NAME}"
    )
    my_cursor = db.cursor()
    my_cursor.execute("INSERT INTO USHolidays (year, day, date, holiday_name) "
                      "VALUES (%s,%s,%s,%s)", (year, day, date, holiday_name))
    db.commit()
    my_cursor.close()
    db.close()
    return


def insert_into_loaddata_table(timestamp, timezone, name, ptid, load):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database=f"{DATABASE_NAME}"
    )
    my_cursor = db.cursor()
    my_cursor.execute("INSERT INTO LoadData (timestamp, timezone, name, ptid, load_) "
                      "VALUES (%s,%s,%s,%s,%s)", (timestamp, timezone, name, ptid, load))
    db.commit()
    my_cursor.close()
    db.close()
    return


def insert_into_weatherdata_table(name, datetime, temp, feelslike, dew, humidity, precip, precipprob, preciptype,
                                  snow, snowdepth, windgust, windspeed, winddir, sealevelpressure, cloudclover,
                                  visibility, solarradiation, solarenergy, uvindex, severerisk, conditions):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database=f"{DATABASE_NAME}"
    )
    my_cursor = db.cursor()
    my_cursor.execute("INSERT INTO WeatherData (name, datetime, temp, feelslike, dew, humidity, "
                      "precip, precipprob, preciptype, snow, snowdepth, windgust, windspeed, winddir, "
                      "sealevelpressure, cloudclover, visibility, solarradiation, solarenergy, uvindex, "
                      "severerisk, conditions) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, "
                      "%s,%s,%s,%s,%s,%s,%s)", (name, datetime, temp, feelslike, dew, humidity, precip,
                      precipprob, preciptype, snow, snowdepth, windgust, windspeed, winddir, sealevelpressure,
                      cloudclover, visibility, solarradiation, solarenergy, uvindex, severerisk, conditions))
    db.commit()
    my_cursor.close()
    db.close()
    return


def insert_into_predictedloaddata_table(timestamp, predicted_load):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database=f"{DATABASE_NAME}"
    )
    my_cursor = db.cursor()
    my_cursor.execute("INSERT INTO LoadData (timestamp,  predicted_load) "
                      "VALUES (%s,%s)", (timestamp, predicted_load))
    db.commit()
    my_cursor.close()
    db.close()
    return
