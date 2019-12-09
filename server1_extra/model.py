import numpy as np

import AIwaffle.MLsource.LogisticRegressionModel.functional as m_model


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

    def forward(self) -> list:
        self.A = m_model.forward(self.X, self.W)
        return self.A.tolist()

    def backward(self) -> list:
        self.W, _ = m_model.backward(self.W, self.A, self.Y, self.X, 0.01)
        return self.W.tolist()

    def loss(self) -> int:
        return m_model.compute_loss(self.A, self.Y)

    def evaluate(self) -> int:
        return m_model.evaluate(self.X, self.W, self.Y)

    def get_data(self) -> dict:
        attrs = ["data", "X", "Y", "n", "m", "W", "A"]
        res = dict()
        for attr in attrs:
            val = self.__getattribute__(attr)
            if isinstance(val, np.ndarray):
                val = val.tolist()
            res.update({attr: val})
        return res
