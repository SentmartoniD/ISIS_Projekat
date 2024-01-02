from DatabaseFunctions import database_insert_functions
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
            SPECIAL_NUMBER if pandas.isna(row[row.index[9]]) else row[row.index[9]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[10]]) else row[row.index[10]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[11]]) else row[row.index[11]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[12]]) else row[row.index[12]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[13]]) else row[row.index[13]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[14]]) else row[row.index[14]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[15]]) else row[row.index[15]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[16]]) else row[row.index[16]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[17]]) else row[row.index[17]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[18]]) else row[row.index[18]],
            SPECIAL_NUMBER if pandas.isna(row[row.index[19]]) else int(row[row.index[19]]),
            SPECIAL_NUMBER if pandas.isna(row[row.index[20]]) else row[row.index[20]],
            f"{SPECIAL_NUMBER}" if pandas.isna(row[row.index[21]]) else row[row.index[21]])
    return "Done inserting into weatherdata table!"


def fill_usholidays_table(usholidaysdata_files):
    df = pandas.read_excel(usholidaysdata_files)
    for i in range(df.shape[0]):
        row = df.iloc[i]
        if pandas.isna(row[row.index[1]]):
            continue
        database_insert_functions.insert_into_usholidays_table(
            row.index[0], row[row.index[1]], row[row.index[2]].strftime('%Y-%m-%d'), row[row.index[3]])
    return "Done inserting into usholidays table!"
