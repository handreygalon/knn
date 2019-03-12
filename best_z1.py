# -*- coding: utf-8 -*-

import csv
import knn_functions as knn_func

# k_value = int(raw_input("Best K value: "))


def bestZ1(k_value):
    i = 1
    predictions = []
    accuracy_list = []
    while(i <= 10):
        instance = "z1n{0}.txt".format(i)
        print("Testing instance: {0}".format(instance))

        with open(instance, 'r') as content:
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

        for x in range(length_z1):
            neighbors = knn_func.getNeighbors(dataset_z1, dataset_z2[x], k_value)
            result = knn_func.getResponse(neighbors)
            predictions.append(result)

        accuracy = knn_func.getAccuracy(dataset_z2, predictions)
        print("accuracy: ", accuracy)
        accuracy_list.append(accuracy)
        predictions = []

        i = i + 1

    maximum = 0
    for x in range(len(accuracy_list)):
        if accuracy_list[x] > maximum:
            maximum = accuracy_list[x]
            best_i = x + 1
    print("Best instance of Z1 is: z1n{0}, with {1}%% of approval".format(best_i, maximum))

    return best_i
