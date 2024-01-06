import preprocessing_service
from HelperClasses.custom_preparer import CustomPreparer
from HelperClasses.ann_regression import AnnRegression
import time

NUMBER_OF_COLUMNS = 3
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

    return
