from Module2.Week4.model.statistics import *
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Ex 1
X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
print("Mean:", compute_mean(X))

# Ex 2
X = [1, 5, 4, 4, 9, 13]
print("Median:", compute_median(X))

# Ex 3
X = [171, 176, 155, 167, 169, 182]
print("Std:", compute_std(X))

# Ex 4
X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
Y = np.asarray([4, 25, 121, 36, 16, 225, 81])
print("Correlation:", compute_correlation_coefficient(X, Y))

# Ex 5
data = pd.read_csv("../dataset/advertising.csv")
x, y = data['TV'], data['Radio']
corr_xy = compute_correlation_coefficient(x, y)
print(f"Correlation between TV and Radio: {round(corr_xy, 2)}")

# Ex 6
features = ['TV', 'Radio', 'Newspaper']
for feature_1 in features:
    for feature_2 in features:
        correlation_value = compute_correlation_coefficient(data[feature_1], data[feature_2])
        print(f"Correlation between {feature_1} and {feature_2}: {round(correlation_value, 2)}")

# Ex 7
x, y = data['Radio'], data['Newspaper']
print(np.corrcoef(x, y))

# Ex 8
print(data.corr())

# Ex 9
plt.figure(figsize=(10, 8))
data_corr = data.corr()
sns.heatmap(data_corr, annot=True, fmt='.2f', linewidths=.5)
plt.show()


