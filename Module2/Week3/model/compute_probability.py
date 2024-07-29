from Module2.Week3.model.get_index_from_value import get_index_from_value
import numpy as np


def compute_prior_probability(data):
    y_unique = ['no', 'yes']
    sample_len = len(data)
    target = data[:, -1]
    prior_probability = np.array([np.count_nonzero(target == val) for val in y_unique]) / sample_len
    return prior_probability


def compute_conditional_probability(data):
    y_unique = ['no', 'yes']
    prior_probability = compute_prior_probability(data)
    sample_len = len(data)
    conditional_probability = []
    list_x_name = []
    for i in range(0, data.shape[1] - 1):
        cur_column = data[:, i]
        x_unique = np.unique(cur_column)
        list_x_name.append(x_unique)
        x_conditional_probability = np.zeros((len(y_unique), len(x_unique)))
        for j in range(0, len(y_unique)):
            for k in range(0, len(x_unique)):
                x_conditional_probability[j, k] = (len(np.where(
                    (cur_column == x_unique[k]) & (data[:, -1] == y_unique[j]))[0]) / sample_len) / prior_probability[j]
        conditional_probability.append(x_conditional_probability)
    return conditional_probability, list_x_name


def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    y_unique = ['no', 'yes']
    prior_probability = compute_prior_probability(train_data)
    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(train_data)
    return prior_probability, conditional_probability, list_x_name


def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(X[0], list_x_name[0])
    x2 = get_index_from_value(X[1], list_x_name[1])
    x3 = get_index_from_value(X[2], list_x_name[2])
    x4 = get_index_from_value(X[3], list_x_name[3])
    p0 = prior_probability[0] * conditional_probability[0][0, x1] * conditional_probability[1][0, x2] * \
         conditional_probability[2][0, x3] * conditional_probability[3][0, x4]
    p1 = prior_probability[1] * conditional_probability[0][1, x1] * conditional_probability[1][1, x2] * \
         conditional_probability[2][1, x3] * conditional_probability[3][1, x4]
    if p0 > p1:
        y_pred = 0
    else:
        y_pred = 1
    return y_pred
