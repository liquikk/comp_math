import vect as v
from copy import deepcopy

def add(m1, m2):
    add_m = []
    if are_matrices(m1, m2):
        check_size(m1, m2)
        for row in range(len(m1)):
            add_m+=[v.sum_vect(m1[row], m2[row])]
    else:
        m, num = mat_num(m1, m2)
        for row in m:
            add_m+=[v.sum_vect(row, num)]
    return add_m

def mlt(m1, m2):
    mlt_m = []
    if are_matrices(m1, m2):
        mlt_check_size(m1, m2)
        zip_b = zip(*m2)
        zip_b = list(zip_b)
        mlt_m = [[sum(a*b for a, b in zip(row_a, col_b)) for col_b in zip_b] for row_a in m1]
    else:
        m, num = mat_num(m1, m2)
        for row in m:
            mlt_m += [v.mlt(row, num)]
    return mlt_m

def sub(m1, m2):
    if are_matrices(m1, m2):
        check_size(m1, m2)
        return add(m1, mlt(m2, -1))
    else:
        m, num = mat_num(m1, m2)
        return add(m, 0 - num)

def transposition(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def get_row(m, row_num):
	return m[row_num]

def get_coll(m, coll_num):
	return get_row(transposition(m), coll_num)

def change_rows(m, row1, row2, do_copy=False):
    if do_copy:
        m = deepcopy(m)
    tmp = get_row(m, row2)
    m[row2] = m[row1]
    m[row1] = tmp
    return m

def mlt_row(m, row, scal=1):
    is_matrix(m)
    ch_m = deepcopy(m)
    for i in range(len(ch_m[row - 1])):
        ch_m[row][i] *= scal
    return ch_m

def add_rows(a, row1, row2, scal=1):
    is_matrix(a)
    ch_m = deepcopy(a)
    ch_m[row1] = v.sum_vect(ch_m[row1], v.mlt(get_row(ch_m, row2), scal))
    return ch_m

def sub_rows(m, row1, row2, scal=1):
    is_matrix(m)
    ch_m = deepcopy(m)
    ch_m[row1] = v.subtraction(ch_m[row1], v.mlt(get_row(ch_m, row2), scal))
    return ch_m



def are_matrices(m1, m2):
    return is_matrix(m1) and is_matrix(m2)
    
def is_matrix(m):
    if type(m) != list:
        return False
    elif type(m) == list and type_cells(m):
        return True
    else:
        raise TypeError(type(m))

def type_cells(m):
    for row in m:
        if type(row) == list:
            for cell in row:
                if not(type(cell) in (int, float)):
                    mess = cell
                    raise TypeError(mess)
    return True

def check_size(m1, m2):
    if len(m1) == len(m2):
        for i in range(len(m1)):
            if len(m1[i]) != len(m2[i]):
                raise ValueError("Size error")
    else:
        raise ValueError("Size error")

def mlt_check_size(m1, m2):
    for row in m1:
        if len(row) != len(m2):
            raise ValueError("Size error")

def mat_num(m, num):
    if type(m) == list:
        if is_matrix(m) and type_cells(m) and type(num) in (int, float):
            return m, num
    elif type(num) == list:
        if is_matrix(num) and type_cells(num) and type(m) in (int, float):
            return num, m
    else:
        raise TypeError("must be only list or num")
