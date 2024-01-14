import pandas
import csv

from Services.HelperClasses.custom_preparer import CustomPreparer
from Services.HelperClasses.ann_regression import AnnRegression
from DatabaseFunctions import database_read_functions

MODEL_PATH = 'Services/Models/model_87_55'
NUMBER_OF_COLUMNS = 10
SHARE_FOR_TRAINING = 0


def predict(start_date, days):

    # get weather data
    weatherdata_list = database_read_functions.read_from_weatherdata_table_by_date_and_days(start_date, days)
    # create list with all data
    data_list = []
    for i in range(weatherdata_list.__len__()):
        elem = [weatherdata_list[i][3], weatherdata_list[i][5], weatherdata_list[i][6],
                weatherdata_list[i][12], weatherdata_list[i][13], weatherdata_list[i][14],
                weatherdata_list[i][16], -1, -1, -1]
        data_list.append(elem)
    dataframe = pandas.DataFrame(data_list)
    print(dataframe)

    # prepare data
    preparer = CustomPreparer(dataframe, NUMBER_OF_COLUMNS, SHARE_FOR_TRAINING)

    testX, testY = preparer.prepare_for_training()
    '''
    print("trainX")
    print(trainX)
    print("trainY")
    print(trainY)
    print("testX")
    print(testX)
    print("testY")
    print(testY)
    '''

    # predict results
    ann_regression = AnnRegression()
    testPredict = ann_regression.predict_with_model_from_path(testX, MODEL_PATH)

    print("testPredict")
    print(testPredict)

    #model = ann_regression.get_model_from_path(MODEL_PATH)
    #print(model)
    testPredict, testY = preparer.inverse_transform_plot(testPredict)
    print("trainPredict")
    print(trainPredict)
    print("trainY")
    print(trainY)
    print("testPredict")
    print(testPredict)
    print("testY")
    print(testY)

    # writre to db
    predictedloaddata_list = []
    for i in range(weatherdata_list.__len__()):
        elem = [weatherdata_list[0]]
        predictedloaddata_list.append(elem)

    # export it to csv file

    return


def write_to_csv(csv_file_name, data):
    with open(csv_file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)
    return
