import math

def length(vector):
    """длина вектора"""
    vv = 0
    for i in range(len(vector)):    
        vv += ((vector[i]**2))
    return math.sqrt(vv)

def angle(vec1,vec2):
    """угол между векторами"""
    if are_vectors(vec1, vec2):
        c=cos(vec1,vec2)
        return math.degrees(math.acos(c))

def sum_vect(vec1, vec2):
    """сложение векторов"""
    if are_vectors(vec1, vec2):
        vec=[]
        for i in range(len(vec1)):    
            vec.append(vec1[i] + vec2[i])
        return vec  
    else:
        vec, num = check_type(vec1, vec2)
        return [vec[i] + num for i in range(len(vec))]

def subtraction(vec1,vec2):
    """вычитание векторов"""
    if are_vectors(vec1, vec2):
        vec=[]
        for i in range(len(vec1)):    
            vec.append(vec1[i] - vec2[i])
        return vec 
    else:
        vec, num = check_type(vec1, vec2)
        return [vec[i] - num for i in range(len(vec))]
    
def scal_pr(vec1, vec2):
    """скалярное произведение векторов"""
    if are_vectors(vec1, vec2):
        vec=0
        for i in range(len(vec1)):    
            vec += (vec1[i] * vec2[i])
        return vec

def mlt(vec1, vec2):
    """произведение векторов"""
    if are_vectors(vec1, vec2):
        return [(vec1[i] * vec2[i]) for i in range(len(vec1))]
    else:
        vec, num = check_type(vec1, vec2)
        return [vec[i] * num for i in range(len(vec))]

def div(vec1, vec2):
    """деление векторов"""
    if are_vectors(vec1, vec2):
        vec = []
        for i in range(len(vec1)):
            vec.append(vec1[i]/vec2[i])
        return vec
    else:
        vec, num = check_type(vec1, vec2)
        return [vec[i] / num for i in range(len(vec))]

def div_scal(vector, scal):
    """деление на скаляр"""
    vec = []
    for i in range(len(vector)):    
        vec.append(vector[i] / scal)
    return vec

def mlt_scal(vector, scal):
    """умножение на скаляр"""
    vec = []
    for i in range(len(vector)):    
        vec.append(vector[i] * scal)
    return vec

def collinear(vec1, vec2):
    """коллинеарность"""
    if are_vectors(vec1, vec2):
        if co_directionality(vec1,vec2) or opposite(vec1,vec2):
            return True
        else:
            return False

def co_directionality(vec1,vec2):
    """сонаправленность"""
    if are_vectors(vec1, vec2):
        c = cos(vec1,vec2)
        if (c == 1):
            return True
        else:
            return False

def opposite(vec1,vec2):
    """противоположность"""
    if are_vectors(vec1, vec2):
        c = cos(vec1,vec2)
        if (c == -1):
            return True
        else:
            return False

def equality(vec1, vec2):
    """равенство"""
    if are_vectors(vec1, vec2):
        n=0
        for i in range(len(vec1)):
            if (vec1[i] == vec2[i]):
                n += 1
        if n == len(vec1):
            return True
        else:
            return False

def equality_with_precision(vec1,vec2,eps):
    """равентсво с зад. точностью"""
    if are_vectors(vec1, vec2):
        n = 0
        for i in range(len(vec1)):
            if (abs(vec1[i] - vec2[i]) < eps):
                n = n + 1
        if n == len(vec1):
            return True
        else:
            return False

def orthogonality(vec1,vec2):
    """ортогональность"""
    if are_vectors(vec1, vec2):
        c = cos(vec1,vec2)
        if c == 0:
            return True
        else:
            return False

def cos(vec1, vec2):
    """косинус"""
    if are_vectors(vec1, vec2):
        return scal_pr(vec1,vec2)/(length(vec1)*length(vec2))

def normaliz(vector):
    """нормировка"""
    vec = []
    leng = length(vector)
    for i in range(len(vector)):
        vec.append(vector[i]/leng)
    return vec

def change_dir(vector):
    """изменение направления вектора"""
    vec = []
    for i in range(len(vector)):
        vec.append(vector[i]*(-1))
    return vec

def projection(vec1, vec2):
    """проекция вектора на вектор"""
    if are_vectors(vec1, vec2):
        c = cos(vec1, vec2)
        proj1 = length(vec1) * c
        proj2 = length(vec2) * c
        return(proj1, proj2)

def are_vectors(v1, v2):
    if type(v1) != list or type(v2) != list:
        return False
    if is_vector(v1) and is_vector(v2):
        check_size(v1, v2)
    return True


def check_size(v1, v2):
    if len(v1) != len(v2):
        raise ValueError(f"first vector len - {len(v1)}, second vector len - {len(v2)}, len's are not similar")
    return True


def check_type(vec, num):
    if type(vec) == list:
        if is_vector(vec) and type(num) in (int, float):
            return vec, num
        else:
            mess = f"{num} must be list, int or float type, not {type(num)}"
            raise TypeError(mess)
    elif type(num) == list:
        if is_vector(num) and type(vec) in (int, float):
            return num, vec
        else:
            mess = f"{vec} must be list, int or float type, not {type(vec)}"
            raise TypeError(mess)
    else:
        raise TypeError("Arguments don't contain vector, vector must be list type")




def is_vector(vec):
	if type(vec) != list:
		raise TypeError(f"{vec} is not vector. Vector must be list, not {type(vec)}")
	for item in vec:
		if type(item) not in (int, float):
			raise TypeError(f"Vector must contanin only int or float coordinates, {item} is {type(item)}")
	return True

    