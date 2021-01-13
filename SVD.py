import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageOps
A = np.random.randint(10, size=(3,4))
print(A)
U, S, V = np.linalg.svd(A)
print(U)
print("-"*50)
print(S)
print("-"*50)
print(V)