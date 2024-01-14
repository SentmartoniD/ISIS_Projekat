import pandas
import csv

from Services.HelperClasses.custom_preparer import CustomPreparer
from Services.HelperClasses.ann_regression import AnnRegression
from DatabaseFunctions import database_read_functions

CSV_FILE_NAME = "prognoza_elektricne_energije(load).csv"
MODEL_PATH = 'Services/Models/model_t_d_h_wg_ws_wd_cc_l_11_11'
NUMBER_OF_COLUMNS = 8
SHARE_FOR_TRAINING = 0


def predict(start_date, days):

    # get weather data
    weatherdata_list = database_read_functions.read_from_weatherdata_table_by_date_and_days(start_date, days)
    # create list with all data
    data_list = []
    for i in range(weatherdata_list.__len__()):
        elem = [weatherdata_list[i][3], weatherdata_list[i][5], weatherdata_list[i][6],
                weatherdata_list[i][12], weatherdata_list[i][13], weatherdata_list[i][14],
                weatherdata_list[i][16], -1]
        data_list.append(elem)
    dataframe = pandas.DataFrame(data_list)
    print(dataframe)

    # prepare data
    preparer = CustomPreparer(dataframe, NUMBER_OF_COLUMNS, SHARE_FOR_TRAINING)

    testX, testY = preparer.prepare_to_predict()
    #trainX, trainY, testX, testY = preparer.prepare_for_training()
    print("testX")
    print(testX)
    print("testY")
    print(testY)


    # predict results
    ann_regression = AnnRegression()
    testPredict = ann_regression.predict_with_model_from_path(testX, MODEL_PATH)
    #ann_regression.use_current_model(MODEL_PATH, trainX)
    #trainPredict, testPredict = ann_regression.get_predict(testX)

    print("testPredict")
    print(testPredict)

    testPredict = preparer.inverse_transform_test_predict(testPredict)
    #trainPredict, trainY, testPredict, testY = preparer.inverse_transform(trainPredict, testPredict)

    print("testPredict")
    print(testPredict)
    print("testY")
    print(testY)

    print(weatherdata_list.__len__())
    print(testPredict.__len__())
    # writre to db
    predictedloaddata_list = []
    for i in range(weatherdata_list.__len__() - 1):
        elem = [weatherdata_list[i][2], testPredict[i]]
        predictedloaddata_list.append(elem)

    predictedloaddata_dataframe = pandas.DataFrame(predictedloaddata_list)
    df = predictedloaddata_dataframe.rename(columns={0: 'Datum i vrijeme', 1: 'Prognozirano opterecenje'})
    # export it to csv file
    df.to_csv(CSV_FILE_NAME, index=False)
    # write_to_csv(CSV_FILE_NAME, predictedloaddata_list)
    return


def write_to_csv(csv_file_name, data):
    with open(csv_file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)
    return
