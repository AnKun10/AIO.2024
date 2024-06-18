def is_positive(name, val):
    if val <= 0:
        print(f"{name} must be greater than zero")
        return False
    return True


def factorial(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans


def sin(x, n):
    ans = 0
    for i in range(n + 1):
        cur = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        ans += cur
    return ans


def cos(x, n):
    ans = 0
    for i in range(n + 1):
        cur = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        ans += cur
    return ans


def sinh(x, n):
    ans = 0
    for i in range(n + 1):
        cur = (x ** (2 * i + 1)) / factorial(2 * i + 1)
        ans += cur
    return ans


def cosh(x, n):
    ans = 0
    for i in range(n + 1):
        cur = (x ** (2 * i)) / factorial(2 * i)
        ans += cur
    return ans
