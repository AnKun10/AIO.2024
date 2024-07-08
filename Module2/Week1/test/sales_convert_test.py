from Module2.Week1.model.sales_convert import sales_convert
import numpy as np
import pandas as pd

df = pd.read_csv('../dataset/advertising.csv')
data = df.to_numpy()

# Ex20
sales_avg = np.average(data[:, -1])
scores = np.vectorize(sales_convert)(data[:, -1], sales_avg)
print(scores[7:10])

# Ex21
A = data[(abs(data[:, -1] - sales_avg) == np.min(abs(data[:, -1] - sales_avg))), -1][0]
scores = np.vectorize(sales_convert)(data[:, -1], A)
print(scores[7:10])
