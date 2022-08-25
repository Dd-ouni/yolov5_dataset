import cv2
import numpy as np
img=cv2.imread('105.png') #读取图像

#由于透明处图像的RGB值是（0,0,0）,所以上下限都设置为0
lower=np.array([0,0,0]) #下限
upper=np.array([0,0,0]) #上限

mask=cv2.inRange(img,lower,upper) #形成掩膜，这个掩膜就符合你的要求，所以不做后面的处理了


cv2.imshow('mask',mask) #显示掩膜
cv2.imwrite("105_done.png",mask) #保存结果




