from Services import preprocessing_service
from Services.HelperClasses.custom_preparer import CustomPreparer
from Services.HelperClasses.ann_regression import AnnRegression
from Services.HelperClasses.scorer import Scorer
import time

NUMBER_OF_COLUMNS = 5
SHARE_FOR_TRAINING = 0.85


def train_model():
    dataframe = preprocessing_service.preprocess()

    # prepare data
    preparer = CustomPreparer(dataframe, NUMBER_OF_COLUMNS, SHARE_FOR_TRAINING)
    trainX, trainY, testX, testY = preparer.prepare_for_training()

    # make predictions
    ann_regression = AnnRegression()
    time_begin = time.time()
    trainPredict, testPredict = ann_regression.compile_fit_predict(trainX, trainY, testX)
    time_end = time.time()
    print('Training duration: ' + str((time_end - time_begin)) + ' seconds')

    # invert predictions
    trainPredict, trainY, testPredict, testY = preparer.inverse_transform(trainPredict, testPredict)

    # calculate root mean squared error
    scorer = Scorer()
    trainScore, testScore = scorer.get_score(trainY, trainPredict, testY, testPredict)

    print('Train Score: %.2f RMSE' % (trainScore))
    print('Test Score: %.2f RMSE' % (testScore))


    return
