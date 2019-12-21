import torch
import numpy as np

import AIwaffle.MLsource.SimpleClassificationModel.SimpleClassificationNetwork as SCN


class Model:
    def __init__(self, size_list, learning_rate=0.01):
        self.obj = SCN.SimpleClassificationNetwork(size_list, learning_rate)

    def forward(self, x: list) -> list:
        res = self.obj.forward(torch.tensor(x))
        return list(map(lambda a: a.tolist(), res))

    def backward(self, y: list) -> dict:
        self.obj.compute_loss(torch.tensor(y))
        self.obj.backward()
        return self.get_data()

    def optimize(self) -> dict:
        self.obj.optimize()
        return self.get_data()

    def loss(self, y: list) -> float:
        return self.obj.compute_loss(torch.tensor(y))

    def get_data(self) -> dict:
        params = self.obj.get_params()
        params = list(map(lambda a: a.tolist(), params))
        grads = self.obj.get_grads()
        grads = list(map(lambda a: a.tolist(), grads))
        return {
            "params": params,
            "grads": grads,
        }

    def iter_(self, x: list, y: list) -> dict:
        output = self.forward(x)
        self.backward(y)
        res = self.get_data()
        res.update({"output": output})
        return res
