import numpy as np
from sklearn.svm import LinearSVC

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array(['A class', 'A class', 'A class', 'B class', 'B class', 'B class'])

classifier = LinearSVC()

classifier.fit(X, Y)

prediction = classifier.predict([[-0.8, -1]])
print('Linear SVM prediction', prediction)

prediction = classifier.predict([[-0.8, -1], [0.5, 1.5]])
print('Linear SVM predictions', prediction)
