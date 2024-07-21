from Module2.Week2.model.cosine_similarity import cs
import numpy as np

x = np.arange(1, 5)
y = np.array([1, 0, 3, 0])
print(cs(x, y))

