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

with open('output1.csv', mode='w', newline='') as csv_file_obj:
    writer = csv.writer(csv_file_obj)
    go = True
    iter_count = 0
    last_coef = None
    while go:
        iter_count += 1
        clf = Perceptron(max_iter=iter_count)
        clf.fit(X, Y)
        # print('Perceptron coefficients', clf.coef_)
        # print('Intercept', clf.intercept_)
        # print('Actual # of iterations', clf.n_iter_)
        writer.writerow([
            int(clf.coef_[0][0]), int(clf.coef_[0][1]), int(clf.intercept_[0])
        ])
        if last_coef is not None:
            if clf.coef_[0][0] == last_coef[0][0]:
                if clf.coef_[0][1] == last_coef[0][1]:
                    go = False
        last_coef = clf.coef_
    print('Iteration count', iter_count)
