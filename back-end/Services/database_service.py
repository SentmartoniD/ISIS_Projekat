from DatabaseFunctions import database_functions
import pandas


def fill_loaddata_table(loaddata_files):
    for key, file in loaddata_files.items():
        df = pandas.read_csv(file)
        for i in range(df.shape[0]):
            row = df.iloc[i]
            if row[row.index[0]][14:16] == "00" and row[row.index[2]] == "N.Y.C.":
                database_functions.insert_into_loaddata_table(row[row.index[0]],
                row[row.index[1]], row[row.index[2]], row[row.index[3]], row[row.index[4]])
    return


def fill_weatherdata_table(weatherdata_files):
    for key, file in weatherdata_files.items():
        df = pandas.read_csv(file)
        for i in range(df.shape[0]):
            row = df.iloc[i]
            database_functions.insert_into_weatherdata_table(row[row.index[0]], row[row.index[1]],
            row[row.index[3]], row[row.index[4]], row[row.index[5]], row[row.index[6]], row[row.index[7]],
            row[row.index[8]], row[row.index[9]], row[row.index[10]], row[row.index[11]], row[row.index[12]],
            row[row.index[13]], row[row.index[14]], row[row.index[15]], row[row.index[16]], row[row.index[17]],
            row[row.index[18]], row[row.index[19]], row[row.index[20]], row[row.index[21]], row[row.index[22]])
    return


def fill_usholidays_table(usholidaysdata_files):
    df = pandas.read_excel(usholidaysdata_files)
    for i in range(df.shape[0]):
        row = df.iloc[i]
        database_functions.insert_into_usholidays_table(
            row.index[0], row[row.index[1]], row[row.index[2]], row[row.index[3]])
    return
