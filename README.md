# Implementação do classificador Knn (K nearest neighbors)

Consider samples from a database, each one has a feature vector and true label of the class. Given a file containing a base with N samples, it was build a program to divide this base into three sets:
- Z1: training;
- Z2: evaluation;
- Z3: test.
This sets were recorded in separate files. The number of samples in each set must be defined by program parameters. Use a percentage for each set (e.g., 25% for Z1, 25% for Z2, and 50% for Z3), but ensure that this percentage is also respected for each class.

To classify a test sample _s_ with knn classifier, you must search for the K samples closest to _s_ in Z1 according to the Euclidean distance between the respective feature vectors. The most frequent label among the nearest K samples is the label used to classify _s_. If this is not the true label of _s_, then it is an error.

The purpose of this implementation is to design a classifier using the sets Z1 and Z2 in order to minimize the number of errors in Z2. Once designed, it will be assumed that this classifier will also get a low error in Z3. This methodology is interesting for two reasons:
- It demonstrates the learning ability with the errors using the Z2 samples;
- Demonstrates the robustness of the classifier in case the errors in Z3 are of the same order of magnitude of errors in Z2.

Then, a program was written to read the Z1 and Z2 files, and find out which K value (1, 3, 5, 7, 9, ...) minimizes the errors in Z2. Keep Z1 fixed and vary only K. When you find the optimal value of K, you set this value, and sort the Z2 samples again, identifying the erroneously sorted samples, writing Z1 and storing the number of errors. Samples erroneously classified in Z2 are exchanged for samples of the same class in Z1, and the process is repeated by T iterations (T can be a parameter of the program together with the names of the Z1 and Z2 files). At the end of iterations, you must identify which instance of Z1 generated the least number of errors in Z2. This file with the best Z1 instance should then be used to test your Z3 classifier.

