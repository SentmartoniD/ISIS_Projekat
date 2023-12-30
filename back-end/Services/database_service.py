from DatabaseFunctions import database_functions
import pandas


def fill_loaddata_table(loaddata_files):
    for i in range(loaddata_files.__len__()):
        csv_files = loaddata_files[i]
        print(csv_files)
        for key, file in csv_files.items():
            try:
                with file.stream as f:
                    df = pandas.read_csv(f)
                    print(df)
                    for j in range(df.shape[0]):
                        row = df.iloc[j]

            except ValueError as e:
                    print(f"Error reading CSV file: {e}")
                #print(row[row.index[2]])
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
            row.index[0], row[row.index[1]], row[row.index[2]], row[row.index[3]]
        )
    return
