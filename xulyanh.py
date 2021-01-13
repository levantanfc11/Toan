#Cài đặt numpy: pip install numpy
import numpy as np
#Cài đặt Pillow: pip install pillow
from matplotlib import pyplot as plt
#Cần cài đặt matplotlib: pip install matplotlib
from PIL import Image, ImageOps
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
plt.xlim([0,300])
#plt.ylim([500,3000])
plt.xlabel('Số thành phần')
plt.ylabel('Giá trị suy biến')
plt.show()