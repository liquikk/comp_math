import matrix as m
import vect as v
from copy import deepcopy

def slau_gj(matrix, keys):
    check_slau(matrix, keys) 

    new_mat = deepcopy(matrix)
    new_keys = deepcopy(keys)
    ch_mat_rows(new_mat, new_keys)
    new_mat, new_keys = direct_sub(new_mat, new_keys)
    new_mat, new_keys = reverse_sub(new_mat, new_keys)
    return new_keys

# def slau_inv_mat(mat, keys):
#     return m.mlt(inverse_mat(mat), keys)

# def inverse_mat(matrix):    
#     diag_mat = diagonal_mat(len(matrix))
#     return slau_gj(matrix, diag_mat)

# def diagonal_mat(size):
#     mat = []
#     for i in range(size):
#         tmp = []
#         for j in range(size):
#             if i == j:
#                 tmp += [1]
#             else:
#                 tmp += [0]
#         mat += [tmp]
#         tmp = []
#     return mat

def direct_sub(matrix, keys):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j > i:
                break
            if i != j:
                if matrix[i][j] != 0:
                    if matrix[j][j] == 0:
                        m.change_rows(matrix, i, j)
                        buf = keys[j]
                        keys[j] = keys[i]
                        keys[i] = buf
                    keys[i] -= keys[j] * matrix[i][j]
                    matrix = m.sub_rows(matrix, i, j, matrix[i][j])
            else:
                if matrix[i][i] == 0:
                    continue
                elif matrix[i][i] != 1:
                    keys[i] /= matrix[i][i]
                    matrix = m.mlt_row(matrix, i, 1 / matrix[i][i])
    return matrix, keys

def reverse_sub(matrix, keys):
     for i in range(len(matrix) - 1, -1, -1):
         for j in range(len(matrix) - 1, -1, -1):
             if i != j:
                 if matrix[i][j] != 0:
                     keys[i] -= keys[j] * matrix[i][j]
                     matrix = m.sub_rows(matrix, i, j, matrix[i][j])
             else:
                 if matrix[i][i] == 0:
                     raise ValueError("invalid matrix")
                 if matrix[i][i] != 1:
                     keys[i] /= matrix[i][i]
                     matrix = m.mlt_row(matrix, i, 1 / matrix[i][i])
     return matrix, keys

def ch_mat_rows(matrix, keys):
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            change = False
            for j in range(len(matrix)):
                if matrix[j][i] != 0 and matrix[i][j] != 0:
                    m.change_rows(matrix, i, j)
                    tmp = keys[i]
                    keys[j] = keys[i]
                    keys[i] = tmp
                    change = True
                    break
            if not(change):
                raise ValueError("invalid matrix")

def check_slau(matrix, keys):
    if type(matrix) != list:
        raise TypeError("Matrix with coefficients must be list type")
    for row in matrix:
        if type(row) != list:
            raise TypeError(f"Matrix with coefficients must consist lists not {type(row)}")
        if len(row) != len(matrix):
            raise ValueError(f"Matrix must be square, row's len ({len(row)}) is not equael matrix's len ({len(matrix)})")
        for cell in row:
            if not(type(cell) in (int, float)):
                raise TypeError(f"Coefficients must be int or float, {cell} is not {type(cell)}")
    if type(keys) != list:
        raise TypeError("Matrix with scalars must be list type")
    for cell in keys:
        if not (type(cell) in (int, float)):
            raise TypeError(f"Keys must be int or float, {cell} is not {type(cell)}")
    if len(matrix) != len(keys):
        raise ValueError(f"sizes matrix with coefficients and matrix with scalars must be similar")


def check_keys(matrix, keys):
    if type(keys) != list:
        raise TypeError("Matrix with scalars must be list type")
    for cell in keys:
        if not (type(cell) in (int, float)):
            raise TypeError(f"Keys must be int or float, {cell} is not {type(cell)}")
    if len(matrix) != len(keys):
        raise ValueError("sizes matrix with coefficients and matrix with scalars must be similar")
