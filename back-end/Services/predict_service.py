import pandas
import csv

from Services.HelperClasses.custom_preparer import CustomPreparer
from Services.HelperClasses.ann_regression import AnnRegression
from DatabaseFunctions import database_read_functions
from Services import database_service, preprocessing_service

CSV_FILE_NAME = "prognoza_elektricne_energije(load).csv"
MODEL_PATH = 'Services/Models/model_t_d_h_wg_ws_wd_cc_prevtemp_months1-12_l_973_934'
NUMBER_OF_COLUMNS = 11
SHARE_FOR_TRAINING = 0


def predict(start_date, days):

    # get weather data
    weatherdata_list = database_read_functions.read_from_weatherdata_table_by_date_and_days(start_date, days)

    df = preprocessing_service.preprocess_for_prediction(start_date, days)

    # prepare data
    preparer = CustomPreparer(df, NUMBER_OF_COLUMNS, SHARE_FOR_TRAINING)

    testX, testY = preparer.prepare_for_predict()

    # predict results
    ann_regression = AnnRegression()
    testPredict = ann_regression.predict_with_model_from_path(testX, MODEL_PATH)

    # inverse data
    testPredict = preparer.inverse_transform_test_predict(testPredict)

    predictedloaddata_list = []
    for i in range(weatherdata_list.__len__()):
        elem = [weatherdata_list[i][2], testPredict[i]]
        predictedloaddata_list.append(elem)
    # writre to db
    database_service.fill_predictedloaddata_table(predictedloaddata_list)

    predictedloaddata_dataframe = pandas.DataFrame(predictedloaddata_list)
    df = predictedloaddata_dataframe.rename(columns={0: 'Datum i vrijeme', 1: 'Prognozirano opterecenje'})
    # export it to csv file
    df.to_csv(CSV_FILE_NAME, index=False)

    return
