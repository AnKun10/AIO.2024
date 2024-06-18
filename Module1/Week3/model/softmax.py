import torch
from torch import tensor
from torch.nn import Module


class Softmax(Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, inp):
        return tensor([torch.exp(x) / torch.sum(torch.exp(inp)) for x in inp])


class SoftmaxStable(Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, inp):
        c = torch.max(inp)
        return tensor([torch.exp(x - c) / torch.sum(torch.exp(inp - c)) for x in inp])
