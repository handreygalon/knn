# -*- coding: utf-8 -*-

import csv
import knn_functions as knn_func

# k_value = int(raw_input("Best K value: "))
# best_instance_z1 = raw_input("Best Z1 instance: ")
# instance_z1 = "z1n{0}.txt".format(best_instance_z1)


def classifyZ3(k_value, instance_z1):
    k_value = int(k_value)

    with open(instance_z1, 'r') as content:
        lines = csv.reader(content)
        dataset_z1 = list(lines)
    length_z1 = len(dataset_z1)

    for x in range(length_z1):
        for y in range(4):
            dataset_z1[x][y] = float(dataset_z1[x][y])

    with open('z3.txt', 'r') as content:
        lines = csv.reader(content)
        dataset_z3 = list(lines)
    length_z3 = len(dataset_z3)

    for x in range(length_z3):
        for y in range(4):
            dataset_z3[x][y] = float(dataset_z3[x][y])

    predictions = []
    accuracy_list = []
    for x in range(length_z3):
        neighbors = knn_func.getNeighbors(dataset_z1, dataset_z3[x], k_value)
        result = knn_func.getResponse(neighbors)
        predictions.append(result)

    accuracy = knn_func.getAccuracy(dataset_z3, predictions)
    print("accuracy: ", accuracy)
    accuracy_list.append(accuracy)
    predictions = []

    maximum = 0
    for x in range(len(accuracy_list)):
        if accuracy_list[x] > maximum:
            maximum = accuracy_list[x]
    print("Result Z3 classification with K = {0}, using {1} instance of Z1, presents {2}%% efficiency".format(k_value, instance_z1, maximum))

    return maximum
