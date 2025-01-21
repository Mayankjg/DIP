# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:22:36 2024

@author: jagla
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread(r"C:\Users\jagla\OneDrive\Desktop\img1.png", cv2.IMREAD_GRAYSCALE)


equ = cv2.equalizeHist(img)


res = np.hstack((img, equ))


cv2.imshow(r"C:\Users\jagla\OneDrive\Desktop\img1.png", res)


hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_equ = cv2.calcHist([equ], [0], None, [256], [0, 256])


plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
plt.plot(hist_img, color='black')
plt.title('Histogram of Original Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')


plt.subplot(1, 2, 2)
plt.plot(hist_equ, color='black')
plt.title('Histogram of Equalized Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()