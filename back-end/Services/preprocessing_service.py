from DatabaseFunctions import database_read_functions
import pandas
import numpy
from datetime import datetime

SPECIAL_NUMBER = 666999


def preprocess_all():
    usholidays_list = database_read_functions.read_from_usholidays_table()
    weatherdata_list = database_read_functions.read_from_weatherdata_table_all()
    dt_list = database_read_functions.read_from_loaddata_table()
    '''
    # TEMP DEW HUMIDITY WINDGUST WINDSPEED WINDDIR LOAD
    data_list = []
    load_sum = 0 ; load_count = 0
    temp_sum = 0 ; temp_count = 0
    dew_sum = 0 ; dew_count = 0
    humidity_sum = 0 ; humidity_count = 0
    windgust_sum = 0 ; windgust_count = 0
    windspedd_sum = 0 ; windspeed_count = 0
    winddir_sum = 0 ; winddir_count = 0
    for i in range(loaddata_list.__len__()):
        for j in range(weatherdata_list.__len__()):
            # GET MATCHING DAYS AND TIMES
            if (loaddata_list[i][1][6:10] == weatherdata_list[j][2][0:4] and
                 loaddata_list[i][1][0:2] == weatherdata_list[j][2][5:7] and
                 loaddata_list[i][1][3:5] == weatherdata_list[j][2][8:10] and
                 loaddata_list[i][1][11:13] == weatherdata_list[j][2][11:13]):
                elem = [weatherdata_list[j][3], weatherdata_list[j][5], weatherdata_list[j][6],
                        weatherdata_list[j][12], weatherdata_list[j][13],
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
                # GET SUM AND COUNT FOR WINDGUST COLUMN,
                if elem[3] >= 16 and elem[3] <= 61:
                    windgust_sum += elem[3]
                    windgust_count += 1
                # GET SUM AND COUNT FOR WINDSPEED COLUMN,
                if elem[4] >= 0 and elem[4] <= 33:
                    windspedd_sum += elem[4]
                    windspeed_count += 1
                # GET SUM AND COUNT FOR WINDDIR COLUMN, WINDDIR NOT BEETHWEN 0 AND 360 WILL BE CONSIDERD INVALID
                if elem[5] <= 360 and elem[5] >= 0:
                    winddir_sum += elem[5]
                    winddir_count += 1
                # GET SUM AND COUNT FOR LOAD COLUMN, LOAD EQUALE TO 666999 WILL BE CONSIDERD INVALID
                if elem[6] != SPECIAL_NUMBER:
                    load_sum += elem[6]
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
        # SET AVG FOR WINDGUST COLUMN WHERE THERE IS INVALID NUMBER
        if data_list[i][3] < 16 or data_list[i][3] > 61:
            data_list[i][3] = round(windgust_sum / windgust_count)
        # SET AVG FOR WINDSPEED COLUMN WHERE THERE IS INVALID NUMBER
        if data_list[i][4] < 0 or data_list[i][4] > 33:
            data_list[i][4] = round(windspedd_sum / windspeed_count)
        # SET AVG FOR WINDDIR COLUMN WHERE THERE IS INVALID NUMBER
        if data_list[i][5] < 0 or data_list[i][5] > 360:
            data_list[i][5] = round(winddir_sum / winddir_count)
        # SET AVG FOR LOAD COLUMN WHERE THERE IS INVALID NUMBER
        if data_list[i][6] == SPECIAL_NUMBER:
            data_list[i][6] = round(load_sum / load_count)

    print(f"temp avg = {round(temp_sum / temp_count)}")
    print(f"dew avg = {round(dew_sum / dew_count)}")
    print(f"humidity avg = {round(humidity_sum / humidity_count)}")
    print(f"windgust avg = {round(windgust_sum / windgust_count)}")
    print(f"windspeed avg = {round(windspedd_sum / windspeed_count)}")
    print(f"winddir avg = {round(winddir_sum / winddir_count)}")
    print(f"load avg = {round(load_sum / load_count)}")
    dataframe = pandas.DataFrame(data_list)
    '''
    loaddata_list = sort_list_by_dates(dt_list)
    # TEMP DEW HUMIDITY WINDGUST WINDSPEED WINDDIR CLOUDCOVER MONTHS PREVLOAD NEXTLOAD  LOAD
    data_list = []
    for i in range(loaddata_list.__len__()):
        # CHECK IF IT IS A HOLIDAY
        if (check_for_holiday(loaddata_list[i][1], usholidays_list) == True):
            continue
        for j in range(weatherdata_list.__len__()):
            # GET MATCHING DAYS AND TIMES
            if (loaddata_list[i][1][6:10] == weatherdata_list[j][2][0:4] and
                 loaddata_list[i][1][0:2] == weatherdata_list[j][2][5:7] and
                 loaddata_list[i][1][3:5] == weatherdata_list[j][2][8:10] and
                 loaddata_list[i][1][11:13] == weatherdata_list[j][2][11:13]):
                # get_month_1234(int(weatherdata_list[j][2][5:7])),
                # loaddata_list[i][5] if i == 0 else loaddata_list[i-1][5],
                # loaddata_list[i][5] if i == loaddata_list.__len__() - 1 else loaddata_list[i+1][5],
                elem = [weatherdata_list[j][3], weatherdata_list[j][5], weatherdata_list[j][6],
                        weatherdata_list[j][12], weatherdata_list[j][13], weatherdata_list[j][14],
                        weatherdata_list[j][15], weatherdata_list[j][16],
                        weatherdata_list[j][3] if j == 0 else weatherdata_list[j-1][3],

                        int(weatherdata_list[j][2][5:7]),
                        5835,

                        loaddata_list[i][5]]
                data_list.append(elem)

    df = pandas.DataFrame(data_list)

    # TEMP
    df[0] = df[0].mask((df[0] > 100.0) | (df[0] < 0.0), numpy.nan)
    # DEW
    df[1] = df[1].mask((df[1] > 78.0) | (df[1] < -17.0), numpy.nan)
    # HUMIDITY
    df[2] = df[2].mask((df[2] > 100.0) | (df[2] < 8.0), numpy.nan)
    # WINDGUST
    df[3] = df[3].mask((df[3] > 61.0) | (df[3] < 16.0), numpy.nan)
    # WINDSPEED
    df[4] = df[4].mask((df[4] > 33.0) | (df[4] < 0.0), numpy.nan)
    # WINDDIR
    df[5] = df[5].mask((df[5] > 360.0) | (df[5] < 0.0), numpy.nan)
    # SEALEVELPRESSURE
    df[6] = df[6].mask((df[6] > 1045) | (df[6] < 975.0), numpy.nan)
    # CLOUDCOVER
    df[7] = df[7].mask((df[7] > 100.0) | (df[7] < 0.0), numpy.nan)
    # LOAD
    df[11].replace(666999.0, numpy.nan, inplace=True)

    df[0] = df[0].interpolate(method='linear', limit_direction='both')
    df[1] = df[1].interpolate(method='linear', limit_direction='both')
    df[2] = df[2].interpolate(method='linear', limit_direction='both')
    df[3] = df[3].interpolate(method='linear', limit_direction='both')
    df[4] = df[4].interpolate(method='linear', limit_direction='both')
    df[5] = df[5].interpolate(method='linear', limit_direction='both')
    df[6] = df[6].interpolate(method='linear', limit_direction='both')
    df[7] = df[7].interpolate(method='linear', limit_direction='both')
    df[11] = df[11].interpolate(method='linear', limit_direction='both')

    return df


def preprocess(start_date, end_date):
    usholidays_list = database_read_functions.read_from_usholidays_table()
    weatherdata_list = database_read_functions.read_from_weatherdata_table_by_dates(start_date, end_date)
    dt_list = database_read_functions.read_from_loaddata_table()


    loaddata_list = sort_list_by_dates(dt_list)
    # TEMP DEW HUMIDITY WINDGUST WINDSPEED WINDDIR CLOUDCOVER MONTHS PREVLOAD NEXTLOAD LOAD
    data_list = []
    for i in range(loaddata_list.__len__()):
        # CHECK IF IT IS A HOLIDAY
        if (check_for_holiday(loaddata_list[i][1], usholidays_list) == True):
            continue
        for j in range(weatherdata_list.__len__()):
            # GET MATCHING DAYS AND TIMES
            if (loaddata_list[i][1][6:10] == weatherdata_list[j][2][0:4] and
                    loaddata_list[i][1][0:2] == weatherdata_list[j][2][5:7] and
                    loaddata_list[i][1][3:5] == weatherdata_list[j][2][8:10] and
                    loaddata_list[i][1][11:13] == weatherdata_list[j][2][11:13]):
                # get_month_123(int(weatherdata_list[j][2][5:7])),
                elem = [weatherdata_list[j][3], weatherdata_list[j][5], weatherdata_list[j][6],
                        weatherdata_list[j][12], weatherdata_list[j][13], weatherdata_list[j][14],
                        weatherdata_list[j][15], weatherdata_list[j][16],
                        weatherdata_list[j][3] if j == 0 else weatherdata_list[j - 1][3],
                        int(weatherdata_list[j][2][5:7]),
                        loaddata_list[i][5]]
                data_list.append(elem)

    df = pandas.DataFrame(data_list)

    # TEMP
    df[0] = df[0].mask((df[0] > 100.0) | (df[0] < 0.0), numpy.nan)
    # DEW
    df[1] = df[1].mask((df[1] > 78.0) | (df[1] < -17.0), numpy.nan)
    # HUMIDITY
    df[2] = df[2].mask((df[2] > 100.0) | (df[2] < 8.0), numpy.nan)
    # WINDGUST
    df[3] = df[3].mask((df[3] > 61.0) | (df[3] < 16.0), numpy.nan)
    # WINDSPEED
    df[4] = df[4].mask((df[4] > 33.0) | (df[4] < 0.0), numpy.nan)
    # WINDDIR
    df[5] = df[5].mask((df[5] > 360.0) | (df[5] < 0.0), numpy.nan)
    # SEALEVELPRESSURE
    df[6] = df[6].mask((df[6] > 1045) | (df[6] < 975.0), numpy.nan)
    # CLOUDCOVER
    df[7] = df[7].mask((df[7] > 100.0) | (df[7] < 0.0), numpy.nan)
    # LOAD
    df[10].replace(666999.0, numpy.nan, inplace=True)

    df[0] = df[0].interpolate(method='linear', limit_direction='both')
    df[1] = df[1].interpolate(method='linear', limit_direction='both')
    df[2] = df[2].interpolate(method='linear', limit_direction='both')
    df[3] = df[3].interpolate(method='linear', limit_direction='both')
    df[4] = df[4].interpolate(method='linear', limit_direction='both')
    df[5] = df[5].interpolate(method='linear', limit_direction='both')
    df[6] = df[6].interpolate(method='linear', limit_direction='both')
    df[7] = df[7].interpolate(method='linear', limit_direction='both')
    df[10] = df[10].interpolate(method='linear', limit_direction='both')

    return df


def sort_list_by_dates(my_list):
    date_format = '%m/%d/%Y %H:%M:%S'
    my_list.sort(key=lambda x: datetime.strptime(x[1], date_format))
    return my_list


def check_for_holiday(date, ush_list):

    for i in range(ush_list.__len__()):
        if (int(date[6:10]) == ush_list[i][1] and
                date[0:2] == ush_list[i][3][5:7] and
                date[3:5] == ush_list[i][3][8:10]):
            return True

    return False


def get_month_1234(dt):
    if (dt == 1 or dt == 12 or dt == 2):
        return 1
    elif (dt == 3 or dt == 11):
        return 2
    elif (dt == 4 or dt == 5 or dt == 10):
        return 3
    else:
        return 4

