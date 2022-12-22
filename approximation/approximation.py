from slau import slau_gj
from matrix import mlt, transposition

def least_squares_method(mat):
    coeffs = []
    a = []
    b = []
    for i in range(len(mat)):
        coeffs_line = []
        for j in range(len(mat[i])):
            coeffs_line += [mat[i][j]]
        coeffs += [coeffs_line]
    for j in range(len(coeffs) - 1):
        b += [0]
        for i in range(len(coeffs)):
            b[-1] += coeffs[i][j] * coeffs[i][-1]
    for j in range(len(coeffs) - 1):
        a_line = [0 for i in range(len(coeffs) - 1)]
        for c in range(len(a_line)):
            for i in range(len(coeffs)):
                a_line[c] += coeffs[i][c] * coeffs[i][j]
        a += [a_line]
    return slau_gj(a, b)


def linear_approximation(mat, x):
    a = [[mat[i][0], 1] for i in range(len(mat))]
    b = [[mat[i][-1]] for i in range(len(mat))]

    a_data = mlt(transposition(a), a)
    b_data = [value[0] for value in mlt(transposition(a), b)]

    coeffs = slau_gj(a_data, b_data)
    return [[item, coeffs[0] * item + coeffs[1]] for item in x]


def polinomial_approximation(coeffs, x):
    mat = []
    a = [[i] for i in coeffs]
    for i in range(len(x)):
        mat_line = []
        for j in range(len(coeffs)):
            mat_line = [x[i]**j] + mat_line
        mat += [mat_line]
    y = mlt(mat, a)
    return  [[x[i], y[i][0]] for i in range(len(y))]
