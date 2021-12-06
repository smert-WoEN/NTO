import sys

import cv2
import numpy as np

dst = (np.zeros((1024, 1280, 3), dtype=np.uint8))
for i in range(1024):
    x = sys.stdin.readline().split()
    for j in range(1280):
        a = [x[j][:2], x[j][2:4], x[j][4:]]
        b = [int(a[0], 16), int(a[1], 16), int(a[2], 16)]
        dst[i][j] = b

hsvMinRed = np.array((0, 110, 0), np.uint8)
hsvMaxRed = np.array((50, 255, 255), np.uint8)
hsvMinBlue = np.array((65, 20, 0), np.uint8)
hsvMaxBlue = np.array((140, 255, 255), np.uint8)

img = cv2.GaussianBlur(dst, (5, 5), cv2.BORDER_DEFAULT)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsvRedFilter = cv2.inRange(hsv, hsvMinRed, hsvMaxRed)
contourRed, img4 = cv2.findContours(hsvRedFilter, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

hsvBlueFilter = cv2.inRange(hsv, hsvMinBlue, hsvMaxBlue)
contourBlue, img6 = cv2.findContours(hsvBlueFilter, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

if len(contourBlue) > len(contourRed):
    print("B " + str(len(contourBlue)))
elif len(contourRed) > len(contourBlue):
    print("R " + str(len(contourRed)))
else:
    print("S " + str(len(contourRed)))




#inputMat = np.genfromtxt("0", delimiter=" ", dtype=str)

#print(len(inputMat))
#print(inputMat)
