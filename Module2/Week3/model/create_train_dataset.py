import numpy as np


def create_train_dataset():
    data = [['Sunny', 'Hot', 'High', 'Weak', 'no'], ['Sunny', 'Hot', 'High', 'Strong', 'no'],
            ['Overcast', 'Hot', 'High', 'Weak', 'yes'], ['Rain', 'Mild', 'High', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Weak', 'yes'], ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
            ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'], ['Overcast', 'Mild', 'High', 'Weak', 'no'],
            ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'], ['Rain', 'Mild', 'Normal', 'Weak', 'yes']]
    return np.array(data)
