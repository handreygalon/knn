import math
import random


def createIrisBase():
    bases_path = "./bases/"

    with open(bases_path + "iris.txt", "r") as f:
        content = f.readlines()

    # ====================== variables ======================
    total_samples = len(content)
    samples_class1, samples_class2, samples_class3 = 0, 0, 0
    lenght_z1, lenght_z2, lenght_z3 = 0, 0, 0
    class1, class2, class3 = [], [], []
    z1, z2, z3 = [], [], []

    for row in content:
        if row.split(',')[4].startswith('Iris-setosa'):
            samples_class1 = samples_class1 + 1
            class1.append(row)
        elif row.split(',')[4].startswith('Iris-versicolor'):
            samples_class2 = samples_class2 + 1
            class2.append(row)
        elif row.split(',')[4].startswith('Iris-virginica'):
            samples_class3 = samples_class3 + 1
            class3.append(row)

    z1_class1 = math.trunc(0.25 * samples_class1)
    z1_class2 = math.trunc(0.25 * samples_class2)
    z1_class3 = math.trunc(0.25 * samples_class3)

    z2_class1 = math.trunc(0.25 * samples_class1)
    z2_class2 = math.trunc(0.25 * samples_class2)
    z2_class3 = math.trunc(0.25 * samples_class3)

    lenght_z1 = z1_class1 + z1_class2 + z1_class3
    lenght_z2 = z2_class1 + z2_class2 + z2_class3
    lenght_z3 = total_samples - lenght_z1 - lenght_z2

    # Create Z1
    for x in range(0, z1_class1):
        index = random.randrange(0, z1_class1)
        z1.append(class1[index])
        class1.pop(index)

    for x in range(0, z1_class2):
        index = random.randrange(0, z1_class2)
        z1.append(class2[index])
        class2.pop(index)

    for x in range(0, z1_class3):
        index = random.randrange(0, z1_class3)
        z1.append(class3[index])
        class3.pop(index)

    # Create Z2
    for x in range(0, z2_class1):
        index = random.randrange(0, z2_class1)
        z2.append(class1[index])
        class1.pop(index)

    for x in range(0, z2_class2):
        index = random.randrange(0, z2_class2)
        z2.append(class2[index])
        class2.pop(index)

    for x in range(0, z2_class3):
        index = random.randrange(0, z2_class3)
        z2.append(class3[index])
        class3.pop(index)

    # Create Z3
    z3 = class1 + class2 + class3

    # Create base z1
    f = open("z1.txt", "w")
    for x in range(0, lenght_z1):
        f.write(z1[x])
    f.close()

    # Create base z2
    f = open("z2.txt", "w")
    for x in range(0, lenght_z2):
        f.write(z2[x])
    f.close()

    # Create base z3
    f = open("z3.txt", "w")
    for x in range(0, lenght_z3):
        f.write(z3[x])
    f.close()

    print("Bases Z1, Z2 and Z3 successfully created")
