import math

def mclaurin_rows_cheker(n, x):
    if n < 0:
        raise ValueError("n must be > 0")
    if type(n) != int:
        raise TypeError("n must be int type")
    if type(x) not in (int, float):
        raise TypeError("x must be int or float type")

def factorial(n):
    if n < 0:
        return 1
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def mclaurin_exp(n, x = 1):
    mclaurin_rows_cheker(n, x)
    if n == 0:
        return 1
    else:
        return x ** n / factorial(n) + mclaurin_exp(n - 1, x)

def mclaurin_sin(n, x):
    mclaurin_rows_cheker(n, x)
    if n == 0:
        return x
    else:
        return ((-1) ** n * x ** (2 * n + 1)) / factorial(2 * n + 1) + mclaurin_sin(n - 1, x)

def mclaurin_cos(n, x):
    mclaurin_rows_cheker(n, x)
    if n == 0:
        return 1
    else:
        return ((-1) ** n  * x ** (2 * n)) / factorial(2 * n) + mclaurin_cos(n - 1, x)

def mclaurin_arcsin(n, x):
    mclaurin_rows_cheker(n, x)
    if n == 0:
        return x
    else:
        return (factorial(2 * n) * x ** (2 * n + 1)) / ((4 ** n) * (factorial(n) ** 2) * (2 * n + 1)) + mclaurin_arcsin(n - 1, x)

def mclaurin_arccos(n, x):
    mclaurin_rows_cheker(n, x)
    if n == 0:
        return x
    else:
        return math.pi / 2 - mclaurin_arcsin(n, x)
