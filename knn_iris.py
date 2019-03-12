from sklearn.neighbors import KNeighborsClassifier


arquivo = './bases/iris.txt'

with open(arquivo) as f:
    samples = f.readlines()

# classes separation
setosa = samples[:50]
versicolor = samples[50:100]
virginica = samples[100:]

# create samples sets
separate_samples = []
for i in range(0, 50):
    separate_samples.append(setosa[i])
    separate_samples.append(versicolor[i])
    separate_samples.append(virginica[i])

# features and classes separation
features = []
classes = []
for sample in separate_samples:
    aux = sample.split(",")
    c1 = float(aux[0])
    c2 = float(aux[1])
    c3 = float(aux[2])
    c4 = float(aux[3])
    classe = aux[4]
    classe = aux[4].strip()
    features.append([c1, c2, c3, c4])
    classes.append(classe)

# trainning and test separation
training_ratio = 0.7
feature_training = features[:int(training_ratio * len(samples))]
feature_test = features[int(training_ratio * len(samples)):]
classes_training = classes[:int(training_ratio * len(samples))]
classes_test = classes[int(training_ratio * len(samples)):]

# trainning
k = 2
neigh = KNeighborsClassifier(n_neighbors=k)
neigh.fit(feature_training, classes_training)
classes_predicted = neigh.predict(feature_test)


hit_percentage = 0
for i in range(0, len(classes_test)):
    if classes_test[i] == classes_predicted[i]:
        hit_percentage += 1
hit_percentage /= float(len(classes_test))
print(hit_percentage * 100)
