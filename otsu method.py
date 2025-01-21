# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:42:54 2024

@author: jagla
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread(r"\Users\jagla\OneDrive\Desktop/img1.jpeg", cv2.IMREAD_GRAYSCALE)

_, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.figure(figsize=(30, 15))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Binarized Image (Otsu)')
plt.imshow(binary_image, cmap='gray')
plt.axis('off')

plt.show()