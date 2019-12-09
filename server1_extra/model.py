import numpy as np

import AIwaffle.MLsource.LogisticRegressionModel.functional as mmodel


class Model:
    def __init__(self, data):
        self.data = data
        self.X = self.data.T[0:2, :]
        self.Y = self.data.T[2, :]
        self.Y = self.Y.reshape((1, -1))
        self.n = self.X.shape[0]
        self.m = self.X.shape[1]
        self.W = np.random.randn(1, self.n + 1)
        self.X = np.vstack((np.ones((1, self.m)), self.X))
        self.A = None

    def forward(self):
        self.A = mmodel.forward(self.X, self.W)
        return self.A

    def backward(self):
        self.W, _ = mmodel.backward(self.W, self.A, self.Y, 0.01)
        return self.W

    def loss(self):
        return mmodel.compute_loss(self.A, self.Y)

    def evaluate(self):
        return mmodel.evaluate(self.X, self.W, self.Y)
