from torch import tensor
from Module1.Week3.model.softmax import Softmax, SoftmaxStable

data = tensor([1, 2, 3])
softmax = Softmax()
softmax_stable = SoftmaxStable()
output = softmax.forward(data)
print(output)
output = softmax_stable.forward(data)
print(output)
