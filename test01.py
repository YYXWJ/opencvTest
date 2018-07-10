#!/usr/bin/env python
# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('test.jpg')
print img.shape
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.imshow(img2)
plt.xticks([]),plt.yticks([])
plt.show()
