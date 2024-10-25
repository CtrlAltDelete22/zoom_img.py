# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:19:29 2024

@author: ACER
"""
#import our libraries
import numpy as np
import cv2 as cv

 
#get a value from user to scale up
scale = int(input('enter a value for scaleUP img: '))
#read our image
img = cv.imread('wood.jpg')
#multiply our heigth and width shape of our image with scale that user enter
heigth = img.shape[0] * scale
width = img.shape[1] * scale
#store our new zoom image
zoomed_img = np.zeros((heigth,width,3),dtype = np.uint8)
#loop over our image and divide every point with scale we want
for i in range(heigth):
    for j in range(width):
        zoomed_img[i,j] = img[int(i/scale),int(j/scale)]
#show our original and zoomed img        
cv.imshow('orig img', img)
cv.imshow('zoomed img', zoomed_img)
cv.waitKey(0)