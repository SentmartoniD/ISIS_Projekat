from Services import preprocessing_service
from Services.HelperClasses.custom_preparer import CustomPreparer
from Services.HelperClasses.ann_regression import AnnRegression
from Services.HelperClasses.scorer import Scorer
import time

NUMBER_OF_COLUMNS = 11
SHARE_FOR_TRAINING = 0.85


def train_model_and_predict():
    dataframe = preprocessing_service.preprocess_all()
    print(dataframe)

    # prepare data
    preparer = CustomPreparer(dataframe, NUMBER_OF_COLUMNS, SHARE_FOR_TRAINING)
    trainX, trainY, testX, testY = preparer.prepare_for_training()

    print("trainX")
    print(trainX)
    print("trainY")
    print(trainY)
    print("testX")
    print(testX)
    print("testY")
    print(testY)

    # make predictions
    ann_regression = AnnRegression()
    time_begin = time.time()
    trainPredict, testPredict = ann_regression.compile_fit_predict(trainX, trainY, testX)
    print("trainPredict")
    print(trainPredict)
    print("testPredict")
    print(testPredict)
    time_end = time.time()
    print('Training duration: ' + str((time_end - time_begin)) + ' seconds')

    # invert predictions
    trainPredict, trainY, testPredict, testY = preparer.inverse_transform(trainPredict, testPredict)
    print("trainPredict")
    print(trainPredict)
    print("trainY")
    print(trainY)
    print("testPredict")
    print(testPredict)
    print("testY")
    print(testY)

    # calculate root mean squared error
    scorer = Scorer()
    trainScore, testScore = scorer.get_score(trainY, trainPredict, testY, testPredict)
    trainScore2, testScore2 = scorer.get_mape(trainY, trainPredict, testY, testPredict)

    print('Train Score: %.2f RMSE' % (trainScore))
    print('Test Score: %.2f RMSE' % (testScore))
    print('Train Score: %.2f MAPE' % (trainScore2))
    print('Test Score: %.2f MAPE' % (testScore2))

    return


def train_model(start_date, end_date):
    dataframe = preprocessing_service.preprocess(start_date, end_date)

    # prepare data
    preparer = CustomPreparer(dataframe, NUMBER_OF_COLUMNS, SHARE_FOR_TRAINING)
    trainX, trainY, testX, testY = preparer.prepare_for_training()

    # train model
    ann_regression = AnnRegression()
    ann_regression.compile_and_fit(trainX, trainY)

    return
