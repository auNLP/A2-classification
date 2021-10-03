from sklearn import datasets
from sklearn.model_selection import train_test_split

import numpy as np

from logistic import Logistic
from neural_network import NeuralNet

# make data
X, y = datasets.make_classification(n_samples=1000, n_features=10, random_state=7)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)


def test_Logistic():
    # train
    mdl = Logistic(input_feature=10)
    mdl.fit(X_train, y_train)

    # apply to test
    y_hat = mdl.predict(X_test)

    # calculate accuracy
    acc = sum(y_hat == y_test) / len(y_test)

    assert acc > 0.80


def test_NeuralNetwork():
    # train
    mdl = NeuralNet()
    mdl.fit(X_train, y_train)

    # apply to test
    y_hat = mdl.predict(X_test)

    # calculate accuracy
    acc = sum(y_hat == y_test) / len(y_test)

    assert acc > 0.80
