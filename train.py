import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def costFunction(x, y, dataLen, theta0, theta1):
    error = 0.0
    for index in range(dataLen):
        error += (y[index] - (theta1 * x[index] + theta0)) ** 2
    return (error / dataLen)

def gradientDescent(x, y, dataLen, theta0, theta1, learningRate, iters):
    for _ in range(iters):
        newTheta0 = 0
        newTheta1 = 0
        for index in range(dataLen):
            newTheta0 += theta0 + (theta1 * x[index]) - y[index]
            newTheta1 += (theta0 + (theta1 * x[index]) - y[index]) * x[index]
        theta0 = theta0 - (newTheta0 / dataLen) * learningRate
        theta1 = theta1 - (newTheta1 / dataLen) * learningRate
    return (theta0, theta1)

def predict(x, slope, intercept):
    return (x * slope + intercept)

def normalizeData(data, minData, maxData):
    return ((data - minData) / (maxData - minData))

def denormalizeData(data, minData, maxData):
    return (data * (maxData - minData) + minData)

def draw(x, y, yPredict):
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y, 'r.')
    plt.plot(x, yPredict)
    plt.show()

def main():
    data = pd.read_csv("data.csv")
    fileSaveDate = open('slopeAndIntercept.txt', 'w')
    xMin = min(data['km'])
    xMax = max(data['km'])
    x = normalizeData(data['km'], xMin, xMax)
    yMin = min(data['price'])
    yMax = max(data['price'])
    y = normalizeData(data['price'], yMin, yMax)
    theta0, theta1 = gradientDescent(x, y, len(data), 0, 0, 0.1, 1000)
    yPredict = denormalizeData(predict(x, theta1, theta0), yMin, yMax)
    draw(data['km'], data['price'], yPredict)
    fileSaveDate.write(str(theta0) + ',' + str(theta1))
    fileSaveDate.close()

if __name__ == '__main__':
    main()