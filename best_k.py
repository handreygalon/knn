# -*- coding: utf-8 -*-
import math
import csv
import knn_functions as knn_func


def bestK():
    with open('z1.txt', 'r') as content:
        lines = csv.reader(content)
        dataset_z1 = list(lines)
    length_z1 = len(dataset_z1)

    for x in range(len(dataset_z1)):
        for y in range(4):
            dataset_z1[x][y] = float(dataset_z1[x][y])

    with open('z2.txt', 'r') as content:
        lines = csv.reader(content)
        dataset_z2 = list(lines)
    length_z2 = len(dataset_z2)

    for x in range(length_z2):
        for y in range(4):
            dataset_z2[x][y] = float(dataset_z2[x][y])

    k = 1
    limit = math.trunc(length_z1 / 2)
    predictions = []
    accuracy_list = []
    k_list = []
    while(k < limit):
        print("Testing K = ", k)
        for x in range(0, length_z1):
            neighbors = knn_func.getNeighbors(dataset_z1, dataset_z2[x], k)
            result = knn_func.getResponse(neighbors)
            predictions.append(result)
        accuracy = knn_func.getAccuracy(dataset_z2, predictions)
        knn_func.createErrorFile(dataset_z2, predictions)
        accuracy_list.append(accuracy)
        predictions = []
        print('Accuracy: ' + str(accuracy) + '%')
        k_list.append(k)
        k = k + 2

    maximum = 0
    for x in range(0, len(accuracy_list)):
        if accuracy_list[x] > maximum:
            maximum = accuracy_list[x]
            best_k = k_list[x]
    print("Best K is: {0} with {1}%%".format(best_k, maximum))

    return (best_k, maximum)
