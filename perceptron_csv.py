import csv

import numpy as np
from sklearn.linear_model import Perceptron


feature_list = []
label_list = []
with open('input1.csv', newline='') as csv_file_obj:
    reader = csv.reader(csv_file_obj)
    for row in reader:
        feature_1 = row[0]
        feature_2 = row[1]
        feature_list.append([feature_1, feature_2])

        label = row[2]
        label_list.append(label)

        # print(', '.join(row))

X = np.array(feature_list)
Y = np.array(label_list)

clf = Perceptron(max_iter=1)

clf.fit(X, Y)

print('Perceptron coefficients', clf.coef_)
print('Intercept', clf.intercept_)
print('Actual # of iterations', clf.n_iter_)

prediction = clf.predict([[10, 10], [5, 15]])
print('Perceptron predictions', prediction)
