# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:49:00 2024

@author: jagla
"""

import cv2
import numpy as np

img = cv2.imread('img1.png')
original = img.copy()
xp = [0,64,128,192,255]
fp = [0,16,128,240,255]
x = np.arange(256)
table = np.interp(x, xp, fp).astype('unit8')
img = cv2.LUT(img,table)
cv2.imshow("original",original)
cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.destroyAllWindows() 