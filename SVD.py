#Cài đặt numpy: pip install numpy
import numpy as np
#Cài đặt Pillow: pip install pillow
from matplotlib import pyplot as plt
#Cần cài đặt matplotlib: pip install matplotlib
from PIL import Image, ImageOps
np.set_printoptions(suppress=True)
#Tạp ma trận random cáp 3x4:
A = np.random.randint(10, size=(3,4))
print(A)
#Phân tích giá trị suy biến với numpy:
U, S, V = np.linalg.svd(A)
print(U)
print("-"*50)
print(S)
print("-"*50)
print(V)

#Tạo ma trận đường chéo với phần tử S:
Sigma = np.zeros(((3, 4)))
print(Sigma)
#Sigma[0, 2] =10 Để thay đổi giá trị trong ma trận zeros
print(Sigma)
for i, x in enumerate(S):
    Sigma[i, i] = x
print(Sigma)
#Khôi phục lại ma trận A
B = U@Sigma@V
print(B)
print(A-B)

#Ung dung svd vao giam chieu cua anh:
#Đọc file ảnh từ đĩa cứng:
pic = Image.open('bam.jpg')
plt.imshow(pic)

#Chuyển anh sang gray:
pic = ImageOps.grayscale(pic)
pic = np.array(pic)
#plt.show()

plt.imshow(pic, cmap='gray')
#plt.show()
U, S, V = np.linalg.svd(pic)

plt.plot(S, 's-')
plt.xlim([0,160])
plt.ylim([160,0])
plt.xlabel('Số thành phần')
plt.ylabel('Giá trị suy biến')
plt.show()

comps = np.arange(0, 10)
rec_pic = U[:,comps]@np.diag(S[comps])@V[comps, :]

plt.figure(figsize=(10,20))
plt.subplot(1,2,1)
plt.imshow(pic, cmap='gray')
plt.title('Lê Văn Tân')
plt.axis

plt.subplot(1,2,2)
plt.imshow(rec_pic, cmap='gray')
plt.title(f'Reconstructed pic from {comps[0]} to {comps[-1]}')
plt.axis

plt.show()