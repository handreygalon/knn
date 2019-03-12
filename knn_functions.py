# -*- coding: utf-8 -*-

import math
import operator
import csv
import random


def loadDataset(path, split, trainingSet=[], evaluationSet=[], testSet=[]):
    with open(path, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)

    for x in range(len(dataset) - 1):
        for y in range(4):
            dataset[x][y] = float(dataset[x][y])
        if random.random() < split:
            trainingSet.append(dataset[x])
        else:
            testSet.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance = distance + pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


def getNeighbors(trainingSet, instance, k):
    distances = []
    length = len(instance) - 1

    for x in range(len(trainingSet)):
        dist = euclideanDistance(instance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])

    return neighbors


def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] = classVotes[response] + 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


def getAccuracy(dataset, predictions):
    correct = 0
    incorrect = 0
    for x in range(len(dataset)):
        if dataset[x][-1] == predictions[x]:
            correct = correct + 1
        else:
            incorrect = incorrect + 1

    print("Correct = ", correct)
    print("Incorrect = ", incorrect)

    return (correct / float(len(dataset))) * 100.0


def createErrorFile(dataset, predictions):
    error_list = []

    for x in range(len(dataset)):
        if dataset[x][-1] == predictions[x]:
            error_list.append("1\n")
        else:
            error_list.append("0\n")

    f = open("error.txt", 'w')
    for x in range(len(predictions)):
        f.write(error_list[x])
    f.close()

    print("Error file created")
