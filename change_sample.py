# -*- coding: utf-8 -*-

import os.path
import random
import csv
import knn_functions as knn_func


class SwapSamples(object):
    """
    Samples erroneously classified in Z2 are exchanged for samples of the same class in Z1, and the process is repeated by T iterations
    """

    def __init__(self):
        if os.path.isfile('z1.txt'):
            with open('z1.txt', 'r') as content:
                lines = csv.reader(content)
                self.dataset_z1 = list(lines)
            self.length_z1 = len(self.dataset_z1)

            for x in range(self.length_z1):
                for y in range(4):
                    self.dataset_z1[x][y] = float(self.dataset_z1[x][y])

        if os.path.isfile('z2.txt'):
            with open('z2.txt', 'r') as content:
                lines = csv.reader(content)
                self.dataset_z2 = list(lines)
            self.length_z2 = len(self.dataset_z2)

            for x in range(self.length_z2):
                for y in range(4):
                    self.dataset_z2[x][y] = float(self.dataset_z2[x][y])

    def changeSample(self, new_z1, actual_z1, actual_z2):
        with open('error.txt', 'r') as content:
            error = content.readlines()
        length_error = len(error)

        pos_error = []
        for x in range(length_error):
            if error[x].startswith('0'):
                pos_error.append(x)

        with open(actual_z1, 'r') as content:
            z1 = content.readlines()

        with open(actual_z2, 'r') as content:
            z2 = content.readlines()

        c = ''
        index = None

        for x in range(self.length_z1):
            if error[x].startswith('0'):
                new_sample_z1 = z2[x]

                class_z2 = z2[x].split(',')[-1]  # Take class from Z2

                # Take random element of the same class
                while(class_z2 != c and index != x):
                    index = random.randrange(self.length_z1)
                    new_sample_z2 = z1[index]
                    c = new_sample_z2.split(',')[-1]

                c = ''
                index = 0
                z1[x] = new_sample_z1
                z2[x] = new_sample_z2

        print("errors: ", error)
        print("len: {0} | pos errors list: {1} ".format(len(pos_error), pos_error))

        # create new z1
        with open(new_z1, "w") as f:
            for x in range(0, self.length_z1):
                f.write(z1[x])
        f.close()

        # create new z2
        with open("z2n.txt", "w") as f:
            for x in range(0, self.length_z2):
                f.write(z2[x])
        f.close()
        print("Sample changed")

    def classification(self, k_value, length, actual_z1, actual_z2):
        predicitions = []

        for x in range(length):
            neighbors = knn_func.getNeighbors(actual_z1, actual_z2[x], k_value)
            result = knn_func.getResponse(neighbors)
            predicitions.append(result)
        accuracy = knn_func.getAccuracy(self.dataset_z2, predicitions)
        knn_func.createErrorFile(self.dataset_z2, predicitions)

        return accuracy

    def classify(self, k_value):
        for i in range(1, 11):
            if i != 1:
                actual_z1 = "z1n{0}.txt".format(i - 1)
                actual_z2 = "z2n.txt"
            else:
                actual_z1 = "z1.txt"
                actual_z2 = "z2.txt"
            new_z1 = "z1n{0}.txt".format(i)

            self.changeSample(new_z1, actual_z1, actual_z2)

            with open(new_z1, 'r') as content:
                lines = csv.reader(content)
                dataset_z1 = list(lines)
            length_new_z1 = len(dataset_z1)
            for x in range(len(dataset_z1)):
                for y in range(4):
                    dataset_z1[x][y] = float(dataset_z1[x][y])

            with open('z2n.txt', 'r') as content:
                lines = csv.reader(content)
                dataset_z2 = list(lines)

            for x in range(len(dataset_z2)):
                for y in range(4):
                    dataset_z2[x][y] = float(dataset_z2[x][y])

            self.classification(k_value, length_new_z1, dataset_z1, dataset_z2)
