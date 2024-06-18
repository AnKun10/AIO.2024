import math
from random import uniform


def is_numeric(n):
    try:
        int(n)
    except ValueError:
        return False
    return True


def generate_sample():
    predict, target = uniform(0, 10), uniform(0, 10)
    return predict, target


def ae(predict, target):
    return abs(target - predict)


def se(predict, target):
    return (target - predict) ** 2


def loss_function(num_samples, name):
    print(f"Input number of samples (integer number) which are generated: {num_samples}")
    if not is_numeric(num_samples):
        print('number of samples must be an integer number')
        return
    loss = 0
    print(f"Input loss name: {name}")
    for i in range(num_samples):
        predict, target = generate_sample()
        error = 0
        if name == "MAE":
            error = ae(predict, target)
        else:
            error = se(predict, target)
        print(f"loss name: {name}, sample: {i}, pred:{predict}, target:{target}, loss: {error}")
        loss += error
    loss /= num_samples
    if name == "RMSE":
        loss = math.sqrt(loss)
    print(f"final {name}: {loss}")


loss_function(5, "RMSE")
loss_function('aa', "MAE")
