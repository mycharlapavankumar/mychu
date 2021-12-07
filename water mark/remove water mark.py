import cv2
import numpy as np
from matplotlib import pyplot as plt
k=150
img=cv2.imread("8.jpg",0)
img2=cv2.imread("8.jpg")
cv2.imshow('im',img)
hist=cv2.calcHist([img],[0],None,[256],[0,256])
target3=255*np.ones((img2.shape),dtype="uint8")
#plt.subplot(211)
plt.plot(hist)
target=255*np.ones((img.shape),dtype="uint8")
target2=255*np.ones((img.shape),dtype="uint8")
index=(img<k*np.ones(target.shape))
index2=(img>=k*np.ones(target.shape))
target[index]=img[index]
target2[index]=img[index]
cv2.imshow('f',target)
cv2.imshow('ff',target2)
target3[index]=img2[index]
cv2.imshow('gr',target3)
plt.show()


