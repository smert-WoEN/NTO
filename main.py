import sys
import time

import cv2
import numpy as np

s = time.time()
dst = np.array([list(map(lambda x: [int(x[:2], 16), int(x[2:4], 16), int(x[4:], 16)], i.replace("\n", '').split()))
                for i in np.array(sys.stdin.readlines(), dtype=np.str_)], dtype=np.uint8)

hsvMinRed = np.array((0, 110, 0), np.uint8)
hsvMaxRed = np.array((50, 255, 255), np.uint8)
hsvMinBlue = np.array((85, 20, 0), np.uint8)
hsvMaxBlue = np.array((140, 255, 255), np.uint8)

img = cv2.GaussianBlur(dst, (65, 65), cv2.BORDER_DEFAULT)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsvRedFilter = cv2.inRange(hsv, hsvMinRed, hsvMaxRed)
_, contourRed, _ = cv2.findContours(hsvRedFilter, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

hsvBlueFilter = cv2.inRange(hsv, hsvMinBlue, hsvMaxBlue)
_, contourBlue, _ = cv2.findContours(hsvBlueFilter, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

if len(contourBlue) > len(contourRed):
    print("B " + str(len(contourBlue)))
elif len(contourRed) > len(contourBlue):
    print("R " + str(len(contourRed)))
else:
    print("S " + str(len(contourRed)))
print(time.time()-s)



#inputMat = np.genfromtxt("0", delimiter=" ", dtype=str)

#print(len(inputMat))
#print(inputMat)
