# -*- coding: utf-8 -*-
import create_bases
import best_k
from change_sample import SwapSamples
import best_z1
import classify_z3
# from csv_file import CSV_file

# csvfile = CSV_file("iris.csv")
# csvfile.add_key("k")
# csvfile.add_key("acerto_Z2")
# csvfile.add_key("melhor_Z1")
# csvfile.add_key("acerto_Z3")
# csvfile.write_header()

if __name__ == '__main__':
    finish = 0
    while finish == 0:
        create = input("Create bases? (Y|N): ")
        if create.lower() == 'y':
            data = {}
            create_bases.createIrisBase()

        k_value = input("Define best k value? (Y|N) ")
        if k_value.lower() == 'y':
            k, percentage = best_k.bestK()
            data['k'] = k
            data['acerto_Z2'] = percentage
            print("Best K value: ", k)

        swap = input("Swap samples erroneously classified in Z2 by sampling from Z1? (Y|N) ")
        if swap.lower() == 'y':
            ss = SwapSamples()
            swap_samples = ss.classify(k)
            print("Samples were exchanged")

        choose_z1 = input("Choose best instance of Z1 (Y|N) ")
        if choose_z1.lower() == 'y':
            instance_z1 = "z1n{0}.txt".format(best_z1.bestZ1(k))
            data['melhor_Z1'] = instance_z1
            print("{0} is the best instance of Z1".format(instance_z1))

        classify = input("Classify using Z3? (Y|N) ")
        if classify.lower() == 'y':
            m = classify_z3.classifyZ3(k, instance_z1)
            data['acerto_Z3'] = m
            # csvfile.add_values(data)
            # finish = 1
            print("Finish")

        again = input("Repeat the process? (Y|N) ")
        if again.lower() == 'y':
            # data.clear()
            # csvfile.add_values(data)
            finish = 0
        else:
            # csvfile.add_values(data)
            finish = 1
