from DatabaseFunctions import database_read_functions
import pandas

SPECIAL_NUMBER = 666999

def preprocess():
    usholidays_list = database_read_functions.read_from_usholidays_table()
    weatherdata_list = database_read_functions.read_from_weatherdata_table()
    loaddata_list = database_read_functions.read_from_loaddata_table()
    data_list = []
    for i in range(loaddata_list.__len__()):
        for j in range(weatherdata_list.__len__()):
            if (loaddata_list[i][1][6:10] == weatherdata_list[j][2][0:4] and
                 loaddata_list[i][1][0:2] == weatherdata_list[j][2][5:7] and
                 loaddata_list[i][1][3:5] == weatherdata_list[j][2][8:10] and
                 loaddata_list[i][1][11:13] == weatherdata_list[j][2][11:13]):
                elem = [weatherdata_list[j][3], loaddata_list[i][4], loaddata_list[i][5]]
                data_list.append(elem)
    '''
    s1=0
    s2=0
    s3=0
    for i in range(data_list.__len__()):
        if data_list[i][0] == SPECIAL_NUMBER:
            s1 += 1
        elif data_list[i][1] == SPECIAL_NUMBER:
            s2 += 1
        elif data_list[i][2] == SPECIAL_NUMBER:
            s3 += 1
    print(f"number of blank spaces in temp is : {s1}")
    print(f"number of blank spaces in ptid is : {s2}")
    print(f"number of blank spaces in load is : {s3}")
    '''

    dataframe = pandas.DataFrame(data_list)

    return dataframe





