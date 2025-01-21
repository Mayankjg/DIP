# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 18:48:32 2024

@author: jagla
"""

import cv2


image = cv2.imread('example.jpg', cv2.IMREAD_GRAYSCALE)
       

if image is None:
    print("Error: Image not found")
    
else:
    
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)


    cv2.imwrite('example1.jpg', blurred_image)

      
    cv2.imshow('Original Image', image)
    cv2.imshow('Blurred Image', blurred_image)

    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    
    