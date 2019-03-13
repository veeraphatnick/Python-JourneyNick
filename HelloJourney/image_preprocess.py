import cv2
import numpy as np
import glob

path = glob.glob("D:\\Object_Detection\\Data Set\\Traffic Signs\\Dataset\\Regulatory Signs\\R-52\\Original\\*.png")
count = 1
size = 40
for img in path:
    image = cv2.imread(img)

    h, w = image.shape[:2]
    hh = int(h/2)
    ww = int(w/2)
    hhh = h/size
    www = w/size

    if(h>w):
        roi = image[hh-ww:hh+ww,ww-ww:ww+ww]
        roi = cv2.resize(roi,(int(w/www), int(h/hhh)), interpolation = cv2.INTER_CUBIC)
    else:
        roi = image[hh-hh:hh+hh,ww-hh:ww+hh]
        roi = cv2.resize(roi,(int(w/www), int(h/hhh)), interpolation = cv2.INTER_CUBIC)
    
    cv2.imwrite('D:\\Object_Detection\\Data Set\\Traffic Signs\\Dataset\\Regulatory Signs\\R-52\\40x40\\'+'R-52_40x40_'+str(count)+'.png',roi)
    
    cv2.imshow('roi',roi)
    count += 1
    k = cv2.waitKey(1)
    cv2.destroyAllWindows
    
  