import math
from sklearn.metrics import mean_squared_error
import numpy
# from scikit import mean_squared_error


class Scorer:
    def get_score(self, trainY, trainPredict, testY, testPredict):
        trainScore = math.sqrt(mean_squared_error(trainY, trainPredict))
        testScore = math.sqrt(mean_squared_error(testY, testPredict))
        return trainScore, testScore

    def get_mape(self, trainY, trainPredict, testY, testPredict):
        trainY, trainPredict = numpy.array(trainY), numpy.array(trainPredict)
        testY, testPredict = numpy.array(testY), numpy.array(testPredict)

        trainResult = numpy.mean(numpy.abs((trainY - trainPredict) / trainY)) * 100
        testResult = numpy.mean(numpy.abs((testY - testPredict) / testY)) * 100

        return trainResult, testResult
