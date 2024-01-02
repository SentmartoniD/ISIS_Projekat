from DatabaseFunctions import database_read_functions
import pandas


def preprocess():
    usholidays_list = database_read_functions.read_from_usholidays_table()
    weatherdata_list = database_read_functions.read_from_weatherdata_table()
    loaddata_list = database_read_functions.read_from_loaddata_table()

    return





