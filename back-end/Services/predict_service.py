import pandas
import csv

from Services.HelperClasses.custom_preparer import CustomPreparer
from Services.HelperClasses.ann_regression import AnnRegression
from DatabaseFunctions import database_read_functions
from Services import database_service

CSV_FILE_NAME = "prognoza_elektricne_energije(load).csv"
MODEL_PATH = 'Services/Models/model_t_d_h_wg_ws_wd_cc_prevtemp_months1-12_l_973_934'
NUMBER_OF_COLUMNS = 11
SHARE_FOR_TRAINING = 0


def predict(start_date, days):

    # get weather data
    weatherdata_list = database_read_functions.read_from_weatherdata_table_by_date_and_days(start_date, days)
    # create list with all data
    data_list = []
    # TEMP DEW HUMIDITY WINDGUST WINDSPEED WINDDIR SEALEVELPRESSURE CLOUDCOVER MONTHS PRETEMP LOAD
    for i in range(weatherdata_list.__len__()):
        elem = [weatherdata_list[i][3], weatherdata_list[i][5], weatherdata_list[i][6],
                weatherdata_list[i][12], weatherdata_list[i][13], weatherdata_list[i][14],
                weatherdata_list[i][15], weatherdata_list[i][16],
                weatherdata_list[i][3] if i == 0 else weatherdata_list[i-1][3],
                int(weatherdata_list[i][2][5:7]), -1]
        data_list.append(elem)
    dataframe = pandas.DataFrame(data_list)
    print(dataframe)
    num_rows = dataframe.shape[0]
    print(f"Number of rows: {num_rows}")
    # prepare data
    preparer = CustomPreparer(dataframe, NUMBER_OF_COLUMNS, SHARE_FOR_TRAINING)

    testX, testY = preparer.prepare_to_predict()

    # predict results
    ann_regression = AnnRegression()
    testPredict = ann_regression.predict_with_model_from_path(testX, MODEL_PATH)

    testPredict = preparer.inverse_transform_test_predict(testPredict)

    print(weatherdata_list.__len__())
    print(testPredict.__len__())
    print(testPredict)

    predictedloaddata_list = []
    for i in range(weatherdata_list.__len__() - 1):
        elem = [weatherdata_list[i][2], testPredict[i]]
        predictedloaddata_list.append(elem)

    print(predictedloaddata_list)
    # writre to db
    database_service.fill_predictedloaddata_table(predictedloaddata_list)

    predictedloaddata_dataframe = pandas.DataFrame(predictedloaddata_list)
    df = predictedloaddata_dataframe.rename(columns={0: 'Datum i vrijeme', 1: 'Prognozirano opterecenje'})
    # export it to csv file
    df.to_csv(CSV_FILE_NAME, index=False)

    return
