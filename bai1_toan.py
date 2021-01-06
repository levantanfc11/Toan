import numpy as np

n =int(input("Nhập n: "))
def matran(n):
        A = np.random.randint(10, size=(n,n))
        return A
def det_matran(A):
        det=np.linalg.det(A)
        return det
def rank_matran(A):
        rank=np.linalg.matrix_rank(A)
        return rank
def luythuabac2_matran(A):
        P=A*A
        return P
def luythuabac3_matran(A):
        T=A*A*A
        return T
matrixA=matran(n)
print(matrixA)
print("Định thức bằng : ",det_matran(matrixA))
print("Rank của ma trận là : ",rank_matran(matrixA))
print("Lũy thừa bậc 2 : \n",luythuabac2_matran(matrixA))
print("Lũy thừa bậc 3 : \n",luythuabac3_matran(matrixA))
