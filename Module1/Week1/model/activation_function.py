import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    if x > 0:
        return x
    return 0


def elu(x, alpha=0.01):
    if x > 0:
        return x
    return alpha * (math.exp(x) - 1)


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def activation_function(x, name):
    print(f"Input x = {x}")
    if not is_number(x):
        print('x must be a number')
        return
    x = float(x)

    print(f"Input activation function (sigmoid|relu|elu): {name}")
    if name == 'sigmoid':
        print(f"sigmoid: f({x}) = {sigmoid(x)}")
    elif name == 'relu':
        print(f"relu: f(x) = {relu(x)}")
    elif name == 'elu':
        print(f"elu: f(x) = {elu(x)}")
    else:
        print(f"{name} is not supported")
