from DatabaseFunctions import database_insert_functions, database_read_functions
import pandas

SPECIAL_NUMBER = 666999

# FILL TABLE FUNCTIONS


def fill_loaddata_table(loaddata_files):
    for key, file in loaddata_files.items():
        df = pandas.read_csv(file)
        for i in range(df.shape[0]):
            row = df.iloc[i]
            if row[row.index[0]][14:16] == "00" and row[row.index[2]] == "N.Y.C.":
                database_insert_functions.insert_into_loaddata_table(
                "0000-00-00T00:00:00" if pandas.isna(row[row.index[0]]) else row[row.index[0]],
                "000" if pandas.isna(row[row.index[1]]) else row[row.index[1]],
                f"{SPECIAL_NUMBER}" if pandas.isna(row[row.index[2]]) else row[row.index[2]],
                SPECIAL_NUMBER if pandas.isna(row[row.index[3]]) else int(row[row.index[3]]),
                SPECIAL_NUMBER if pandas.isna(row[row.index[4]]) else row[row.index[4]])
    return "Done inserting into loaddata table!"


def fill_weatherdata_table(weatherdata_files):
    for key, file in weatherdata_files.items():
        df = pandas.read_csv(file)
        for i in range(df.shape[0]):
            row = df.iloc[i]
            database_insert_functions.insert_into_weatherdata_table(
            "New York City, NY" if pandas.isna(row[row.index[0]]) else row[row.index[0]],
            "0000-00-00T00:00:00" if pandas.isna(row[row.index[1]]) else row[row.index[1]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[2]]) else row[row.index[2]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[3]]) else row[row.index[3]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[4]]) else row[row.index[4]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[5]]) else row[row.index[5]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[6]]) else row[row.index[6]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[7]]) else row[row.index[7]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[8]]) else row[row.index[8]],
            SPECIAL_NUMBER if pandas.isna(float(row[row.index[9]])) else float(row[row.index[9]]),
            SPECIAL_NUMBER if pandas.isna(float(row[row.index[10]])) else float(row[row.index[10]]),
            SPECIAL_NUMBER if pandas.isna(float(row[row.index[11]])) else float(row[row.index[11]]),
            SPECIAL_NUMBER if pandas.isna(float(row[row.index[12]])) else float(row[row.index[12]]),
            SPECIAL_NUMBER if pandas.isna(float(row[row.index[13]])) else float(row[row.index[13]]),
            SPECIAL_NUMBER if pandas.isna(float(row[row.index[14]])) else float(row[row.index[14]]),
            SPECIAL_NUMBER if pandas.isna(float(row[row.index[15]])) else float(row[row.index[15]]),
            SPECIAL_NUMBER if pandas.isna(float(row[row.index[16]])) else float(row[row.index[16]]),
            SPECIAL_NUMBER if pandas.isna(float(row[row.index[17]])) else float(row[row.index[17]]),
            SPECIAL_NUMBER if pandas.isna(float(row[row.index[18]])) else float(row[row.index[18]]),
            SPECIAL_NUMBER if pandas.isna(int(row[row.index[20]])) else int(row[row.index[20]]),
            SPECIAL_NUMBER if pandas.isna(float(row[row.index[20]])) else float(row[row.index[20]]),
            SPECIAL_NUMBER if pandas.isna(row[row.index[21]]) else row[row.index[21]])
    return "Done inserting into weatherdata table!"


def fill_usholidays_table(usholidaysdata_files):
    df = pandas.read_excel(usholidaysdata_files)
    row0 = df.iloc[0]
    listyears = [row0.index[0]]
    for i in range(df.shape[0]):
        row = df.iloc[i]
        if not pandas.isna(row[row.index[0]]):
            listyears.append(int(row[row.index[0]]))
    year_counter = 0
    for i in range(df.shape[0]):
        row = df.iloc[i]
        if pandas.isna(row[row.index[1]]):
            year_counter += 1
            continue
        database_insert_functions.insert_into_usholidays_table(
            listyears[year_counter], row[row.index[1]], row[row.index[2]].strftime('%Y-%m-%d'), row[row.index[3]])
    return "Done inserting into usholidays table!"


def fill_predictedloaddata_table(predictedloaddata_files):
    for i in range(predictedloaddata_files.__len__()):
        database_insert_functions.insert_into_predictedloaddata_table(
            predictedloaddata_files[i][0], predictedloaddata_files[i][1])

    return


def get_from_predictedloaddata_table_by_dates(start_date, end_date):
    data_list = database_read_functions.read_from_predictedloaddata_table_all(start_date, end_date)
    return data_list
