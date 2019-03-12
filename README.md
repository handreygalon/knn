# Implementation of the Knn classifier (K nearest neighbors)

Consider samples from a database, each one has a feature vector and true label of the class. Given a file containing a base with N samples, it was build a program to divide this base into three sets:
- _Z1_: training;
- _Z2_: evaluation;
- _Z3_: test.
This sets were recorded in separate files. The number of samples in each set must be defined by program parameters. Use a percentage for each set (e.g., 25% for _Z1_, 25% for _Z2_, and 50% for _Z3_), but ensure that this percentage is also respected for each class.

To classify a test sample _s_ with knn classifier, you must search for the _K_ samples closest to _s_ in Z1 according to the Euclidean distance between the respective feature vectors. The most frequent label among the nearest _K_ samples is the label used to classify _s_. If this is not the true label of _s_, then it is an error.

The purpose of this implementation is to design a classifier using the sets _Z1_ and _Z2_ in order to minimize the number of errors in _Z2_. Once designed, it will be assumed that this classifier will also get a low error in _Z3_. This methodology is interesting for two reasons:
- It demonstrates the learning ability with the errors using the _Z2_ samples;
- Demonstrates the robustness of the classifier in case the errors in _Z3_ are of the same order of magnitude of errors in _Z2_.

Then, a program was written to read the _Z1_ and _Z2_ files, and find out which _K_ value (1, 3, 5, 7, 9, ...) minimizes the errors in _Z2_. Keep _Z1_ fixed and vary only _K_. When you find the optimal value of _K_, you set this value, and sort the _Z2_ samples again, identifying the erroneously sorted samples, writing _Z1_ and storing the number of errors. Samples erroneously classified in _Z2_ are exchanged for samples of the same class in Z1, and the process is repeated by _T_ iterations (_T_ can be a parameter of the program together with the names of the _Z1_ and _Z2_ files). At the end of iterations, you must identify which instance of _Z1_ generated the least number of errors in _Z2_. This file with the best _Z1_ instance should then be used to test your _Z3_ classifier.

