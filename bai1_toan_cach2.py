import numpy as np


n = int(input("Nhập n :"))


def matran(n):
    M = np.random.randint(10, size=(n,n))
    det1=np.linalg.det(M)
    rank=np.linalg.matrix_rank(M)
    P = M * 2 
    T = M ^ 3
    return M , det1 , rank , P , T
matrixA=matran(n)
print(matrixA)    
