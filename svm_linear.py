import csv

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

feature_list = []
label_list = []
with open('input3.csv', newline='') as csv_file_obj:
    reader = csv.reader(csv_file_obj)
    for row in reader:
        if row == ['A', 'B', 'label']:
            continue

        feature_1 = float(row[0])
        feature_2 = float(row[1])
        feature_list.append([feature_1, feature_2])

        label = int(row[2])
        label_list.append(label)

        # print(', '.join(row))

X = np.array(feature_list)
Y = np.array(label_list)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.4
)

# classifier = LinearSVC()
#
# classifier.fit(X_train, Y_train)
#
# prediction = classifier.predict(X_train)
# score = accuracy_score(Y_train, prediction)
# print('Linear SVM training score', score)
#
# prediction = classifier.predict(X_test)
# score = accuracy_score(Y_test, prediction)
# print('Linear SVM actual score', score)

max_score = -1.0
c_with_max_score = None
for c in [0.1, 0.5, 1, 5, 10, 50, 100]:
    classifier = LinearSVC(C=c)

    classifier.fit(X_train, Y_train)

    prediction = classifier.predict(X_train)
    score = accuracy_score(Y_train, prediction)
    print('Linear SVM training score for C =', c, score)
    if score >= max_score:
        max_score = score
        c_with_max_score = c

print('Max score', max_score)
print('C with max score', c_with_max_score)

classifier = LinearSVC(C=c_with_max_score)

classifier.fit(X_train, Y_train)

prediction = classifier.predict(X_test)
score = accuracy_score(Y_test, prediction)
print('Linear SVM actual score', score)
