from DatabaseFunctions import database_read_functions
import pandas

SPECIAL_NUMBER = 666999


def preprocess():
    usholidays_list = database_read_functions.read_from_usholidays_table()
    weatherdata_list = database_read_functions.read_from_weatherdata_table()
    loaddata_list = database_read_functions.read_from_loaddata_table()
    data_list = []
    load_sum = 0 ; load_count = 0
    temp_sum = 0 ; temp_count = 0
    dew_sum = 0 ; dew_count = 0
    humidity_sum = 0 ; humidity_count = 0
    winddir_sum = 0 ; winddir_count = 0
    for i in range(loaddata_list.__len__()):
        for j in range(weatherdata_list.__len__()):
            # GET MATCHING DAYS AND TIMES
            if (loaddata_list[i][1][6:10] == weatherdata_list[j][2][0:4] and
                 loaddata_list[i][1][0:2] == weatherdata_list[j][2][5:7] and
                 loaddata_list[i][1][3:5] == weatherdata_list[j][2][8:10] and
                 loaddata_list[i][1][11:13] == weatherdata_list[j][2][11:13]):
                elem = [weatherdata_list[j][3], weatherdata_list[j][5], weatherdata_list[j][6],
                        weatherdata_list[j][14], loaddata_list[i][5]]
                data_list.append(elem)
                # GET SUM AND COUNT FOR TEMP COLUMN, TEMP NOT BEETHWEN 0 AND 100 WILL BE CONSIDERD INVALID
                if elem[0] <= 100 and elem[0] >= 0:
                    temp_sum += elem[0]
                    temp_count += 1
                # GET SUM AND COUNT FOR DEW COLUMN, DEW NOT BEETHWEN -17 AND 78 WILL BE CONSIDERD INVALID
                if elem[1] >= -17 and elem[1] <= 78:
                    dew_sum += elem[1]
                    dew_count += 1
                # GET SUM AND COUNT FOR HUMIDITY COLUMN, HUMIDITY NOT BEETHWEN 8 AND 100 WILL BE CONSIDERD INVALID
                if elem[2] >= 8 and elem[2] <= 100:
                    humidity_sum += elem[2]
                    humidity_count += 1
                # GET SUM AND COUNT FOR WINDDIR COLUMN, WINDDIR NOT BEETHWEN 0 AND 360 WILL BE CONSIDERD INVALID
                if elem[3] <= 360 and elem[3] >= 0:
                    winddir_sum += elem[3]
                    winddir_count += 1
                # GET SUM AND COUNT FOR LOAD COLUMN, LOAD EQUALE TO 666999 WILL BE CONSIDERD INVALID
                if elem[4] != SPECIAL_NUMBER:
                    load_sum += elem[4]
                    load_count += 1

    for i in range(data_list.__len__()):
        # SET AVG FOR TEMP COLUMN WHERE THERE IS INVALID NUMBER
        if data_list[i][0] < 0 or data_list[i][0] > 100:
            data_list[i][0] = round(temp_sum / temp_count)
        # SET AVG FOR DEW COLUMN WHERE THERE IS INVALID NUMBER
        if data_list[i][1] < -17 or data_list[i][1] > 78:
            data_list[i][1] = round(dew_sum / dew_count)
        # SET AVG FOR DEW COLUMN WHERE THERE IS INVALID NUMBER
        if data_list[i][2] < 8 or data_list[i][2] > 100:
            data_list[i][2] = round(humidity_sum / humidity_count)
        # SET AVG FOR WINDDIR COLUMN WHERE THERE IS INVALID NUMBER
        if data_list[i][3] < 0 or data_list[i][3] > 360:
            data_list[i][3] = round(winddir_sum / winddir_count)
        # SET AVG FOR LOAD COLUMN WHERE THERE IS INVALID NUMBER
        if data_list[i][4] == SPECIAL_NUMBER:
            data_list[i][4] = round(load_sum / load_count)

    print(f"temp avg = {round(temp_sum / temp_count)}")
    print(f"dew avg = {round(dew_sum / dew_count)}")
    print(f"humidity avg = {round(humidity_sum / humidity_count)}")
    print(f"winddir avg = {round(winddir_sum / winddir_count)}")
    print(f"load avg = {round(load_sum / load_count)}")

    dataframe = pandas.DataFrame(data_list)

    return dataframe





