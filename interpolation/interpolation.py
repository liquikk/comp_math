from slau import slau_gj
from copy import deepcopy

def find_coeff(mat):
    new_mat = deepcopy(mat)
    k = []
    for i in range(len(new_mat)):
        k += [new_mat[i][1]]
        new_mat[i][1] = 1
    return slau_gj(new_mat, k)

def int_point(mat, x):
    coefficients = find_coeff(mat)
    if type(x) in (float, int):
        return [x, coefficients[0] * x + coefficients[-1]]
    elif type(x) == list:
        xy = []
        for point_x in x:
            xy += [[point_x, coefficients[0] * point_x + coefficients[-1]]]
        return xy
    else:
        raise TypeError("x must be int, float or list type")

def int_piece(mat, x):
    coeffs = []
    pieces = []
    for j in range(len(mat) - 1):
        coeffs += [find_coeff([mat[j], mat[j+1]])]
        pieces += [[mat[j][0], mat[j+1][0]]]
    points_arr = []
    for i in x:
        if i <= pieces[0][0]:
            points_arr += [[i, i * coeffs[0][0] + coeffs[0][1]]]
        elif i >= pieces[-1][0]:
            points_arr += [[i, i * coeffs[-1][0] + coeffs[-1][1]]]
        else:
            for j in range(len(pieces)):
                if i >= pieces[j][0] and i <= pieces[j][1]:
                    points_arr += [[i, i * coeffs[j][0] + coeffs[j][1]]]
    return points_arr

def get_basis(data, i, x):
    l = 1
    for j in range(len(data)):
        if j != i:
            l *= (x - data[j][0]) / (data[i][0] - data[j][0])
    return l


def lagranje_polimom(data, x):
    L = 0
    for j in range(len(data)):
        L += data[j][1] * get_basis(data, j, x)
    return [x, L]


