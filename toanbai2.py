import numpy as np
from sympy import Matrix


def matran(m,n):
    a = np.random.randint(10, size=(m,n))
    return a



def rank_matran(a):
    ranka=np.linalg.matrix_rank(a)
    return ranka


def bacthang(a):
    a = Matrix(a)
    b = Matrix.rref(a)
    return np.array(b[0])


a = matran(3 , 4)
print("Ma trận a là : \n",a)

r = rank_matran(a)
print("Rank của ma trận a là : ",r)

b = bacthang(a)
print("Ma trận bậc thang của ma trận là : \n",b)


