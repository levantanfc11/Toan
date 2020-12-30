import numpy as np
import random
def matran(n):
    while True:
        A = np.random.randint(10, size=(n,n))
        det=np.linalg.det(A)
        if det!=0:
            break
    print(A)
n = int(input("Nhap A : "))
matran(n)