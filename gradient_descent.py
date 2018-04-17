import csv

import numpy as np
from sklearn.linear_model import SGDRegressor


feature_list = []
label_list = []
with open('input2.csv', newline='') as csv_file_obj:
    reader = csv.reader(csv_file_obj)
    for row in reader:
        row = row[0].split(',')

        feature_1 = row[0]
        feature_2 = row[1]
        feature_list.append([feature_1, feature_2])

        label = row[2]
        label_list.append(label)

        # print(', '.join(row))

X = np.array(feature_list)
Y = np.array(label_list)

with open('output2.csv', mode='w', newline='') as csv_file_obj:
    writer = csv.writer(csv_file_obj)
    iter_count = 100
    my_alpha = 11
    for alpha in [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, my_alpha]:
        clf = SGDRegressor(alpha=alpha, max_iter=iter_count)
        clf.fit(X, Y)
        print('Gradient descent coefficients', clf.coef_)
        print('Intercept', clf.intercept_)
        writer.writerow([
            alpha, iter_count, clf.intercept_[0], clf.coef_[0], clf.coef_[1]
        ])
