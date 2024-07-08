import numpy as np
import pandas as pd

df = pd.read_csv('../dataset/advertising.csv')
data = df.to_numpy()

# Ex15
sales_max_values = np.max(data[:, -1])
sales_max_idx = np.where(data[:, -1] == sales_max_values)[0][0]
print(f"Max: {sales_max_values} - Index: {sales_max_idx}")

# Ex16
print(np.average(data[:, 0]))

# Ex17
print(len(np.where(data[:, -1] >= 20)[0]))

# Ex18
print(np.average(data[(data[:, -1] >= 15), 1]))

# Ex19
newspaper_avg = np.average(data[:, 2])
print(np.sum(data[(data[:, 2] > newspaper_avg), -1]))
