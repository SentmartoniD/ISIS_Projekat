from DatabaseFunctions import database_read_functions
import pandas


def preprocess():
    usholidays_list = database_read_functions.read_from_usholidays_table()
    weatherdata_list = database_read_functions.read_from_weatherdata_table()
    loaddata_list = database_read_functions.read_from_loaddata_table()
    data_list = []
    # GET ALL THE TIMESTAMPS FOR LOAD DATA
    for i in range(loaddata_list.__len__()):
        elem = []
        elem.append(loaddata_list[i][1])
        data_list.append(elem)

    # GET THE VALUES FROM WEATHER DATA
    for i in range(weatherdata_list.__len__()):
        for j in range(data_list.__len__()):
            if (data_list[j][0][6:10] == weatherdata_list[i][2][0:4] and
                 data_list[j][0][0:2] == weatherdata_list[i][2][5:7] and
                 data_list[j][0][3:5] == weatherdata_list[i][2][8:10] and
                 data_list[j][0][11:13] == weatherdata_list[i][2][11:13]):
                data_list[j].append(weatherdata_list[i][3])

    # GET THE OTHER VALUES FROM LOAD DATA
    for i in range(loaddata_list.__len__()):
        for j in range(data_list.__len__()):
            if loaddata_list[i][1] == data_list[j][0]:
                data_list[j].append(loaddata_list[i][4])
                data_list[j].append(loaddata_list[i][5])
    '''
    print(loaddata_list[1][1])
    print(loaddata_list[2])
    print(weatherdata_list[2])
    a = loaddata_list[2]
    b = weatherdata_list[2]
    print(weatherdata_list[2][2][0:4])
    
    if (a[1][6:10] == b[2][0:4] and a[1][0:2] == b[2][5:7] and a[1][3:5] == b[2][8:10] and a[1][11:13] == b[2][11:13]):
        print("yes")
    else:
        print("no")
    print(a[1][11:13])
    print(b[2][11:13])'''

    print(data_list)
    return





