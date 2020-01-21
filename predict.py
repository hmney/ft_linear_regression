import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def estimatePrice(mileage, theta0, theta1):
    return (theta0 + (theta1 * mileage))
    
def normalizeData(data, minData, maxData):
    return ((data - minData) / (maxData - minData))

def denormalizeData(data, minData, maxData):
    return (data * (maxData - minData) + minData)

def main():
    fileReadData = open('slopeAndIntercept.txt', 'r')
    data = pd.read_csv("data.csv")
    solpeIntercept = fileReadData.read()
    solpeIntercept = solpeIntercept.split(',')
    theta0 = float(solpeIntercept[0])
    theta1 = float(solpeIntercept[1])
    xMin = min(data['km'])
    xMax = max(data['km'])
    yMin = min(data['price'])
    yMax = max(data['price'])
    mileage = input("Enter The mileage you want: ")
    mileage = normalizeData(float(mileage), xMin, xMax)
    theta0, theta1 = denormalizeData(theta0, yMin, yMax), denormalizeData(theta1, yMin, yMax)
    price = estimatePrice(float(mileage), theta0, theta1)
    print('This is the estimated price for your car: ', price)

if __name__ == '__main__':
    main()