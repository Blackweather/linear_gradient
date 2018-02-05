import matplotlib.pyplot as plt
import numpy as np
import random


def calculateCostSum(function, dataX, dataY, dataCount):
    toReturn = 0
    for i in range(0, dataCount):
        functionValue = function(dataX[i])
        diff = functionValue - dataY[i]
        diff *= diff
        toReturn += diff
    toReturn *= (1 / (2 * dataCount))
    return toReturn


def calculateDerivativeSum(function, dataX, dataY, dataCount):
    toReturn = 0
    for i in range(0, dataCount):
        functionValue = function(dataX[i])
        diff = functionValue - dataY[i]
        toReturn += diff
    toReturn *= (1 / dataCount)
    return toReturn


def calculateDerivativeSum1(function, dataX, dataY, dataCount):
    toReturn = 0
    for i in range(0, dataCount):
        functionValue = function(dataX[i])
        diff = functionValue - dataY[i]
        # the difference from theta0
        diff *= dataX[i]
        toReturn += diff
    toReturn *= (1 / dataCount)
    return toReturn


# plots the passed function into graph
def graph(f, xRange, yRange, subplot):
    x = np.arange(0, xRange, 0.01)
    y = f(x)
    subplot.plot(x, y, 'r')


def main():
    # define ranges and data count
    xRange = random.randint(1, 100)
    yRange = random.randint(1, 100)
    numberOfValues = random.randint(1, 50)

    # randomize data set
    plotX = xRange * (np.random.random_sample((numberOfValues,))) + 1
    plotY = yRange * (np.random.random_sample((numberOfValues,))) + 1

    # define the plotting area
    fig = plt.figure()
    plt.ylabel('random data')
    ax1 = fig.add_subplot(111)

    # plot the data set
    ax1.plot(plotX, plotY, 'bo')

    # compute the gradient descent
    # starting parameters

    # learning rate
    alpha = 0.001

    # linear regression parameters
    theta0 = 0
    theta1 = 0

    # initial line function
    h = lambda x: theta1 * x + theta0

    # finish flag
    converges = False

    # used for checking if converges
    previousValue = calculateCostSum(h, plotX, plotY, numberOfValues)

    # gradient descent loop - loop while cost function minimum not found
    while not converges:
        # calculate the derivative of cost function

        # calculate for theta0
        derivative0 = calculateDerivativeSum(h, plotX, plotY, numberOfValues)
        derivative0 *= alpha
        derivative0 = theta0 - derivative0

        # calculate for theta1
        derivative1 = calculateDerivativeSum1(h, plotX, plotY, numberOfValues)
        derivative1 *= alpha
        derivative1 = theta1 - derivative1

        # create new linear function, don't substitute yet
        h = lambda x: derivative1 * x + derivative0

        # check if converges (cost function minimum found)
        # check current value of cost function
        currentValue = calculateCostSum(h, plotX, plotY, numberOfValues)

        # compare to previous cost function value
        if currentValue > previousValue:
            # local minimum in previous iteration
            converges = True
        else:
            previousValue = currentValue
            # update theta values
            theta0=derivative0
            theta1=derivative1

    # plot the final function
    graph(lambda x: theta1 * x + theta0, xRange, yRange, ax1)
    plt.show()


if __name__ == '__main__':
    main()
