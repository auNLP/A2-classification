"""
includes a class for logistic regression
"""

from torch import nn


class Logistic(nn.Module):
    def __init__(self):
        super(Logistic, self).__init__()
        pass
        #your code

    def fit(self, X, y):
        pass

    def predict(self, X):
        pass