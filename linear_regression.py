import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

classifier = LinearRegression()

classifier.fit(X, Y)

prediction = classifier.predict([[-0.8, -1]])
print('Linear regression prediction', prediction)

prediction = classifier.predict([[-0.8, -1], [0.5, 1.5]])
print('Linear regression predictions', prediction)
