import numpy as np
from cv2 import cv2
import sys
if __name__ == '__main__':
    def nothing(*arg):
        pass

hsvMinRed = np.array((0, 110, 0), np.uint8)
hsvMaxRed = np.array((50, 255, 255), np.uint8)
hsvMinBlue = np.array((65, 20, 0), np.uint8)
hsvMaxBlue = np.array((140, 255, 255), np.uint8)

dst = np.array([list(map(lambda x: [int(x[:2], 16), int(x[2:4], 16), int(x[4:], 16)], i.replace("\n", '').split()))
                for i in np.array(sys.stdin.readlines(), dtype=np.str_)], dtype=np.uint8)
img = cv2.GaussianBlur(dst, (165, 165), cv2.BORDER_DEFAULT)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsvRedFilter = cv2.inRange(hsv, hsvMinRed, hsvMaxRed)
_, contourRed, _ = cv2.findContours(hsvRedFilter, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
redContourDraw = img.copy()
cv2.drawContours(image=redContourDraw, contours=contourRed, contourIdx=-1, color=(0, 255, 0), thickness=2,
                 lineType=cv2.LINE_AA)
print(len(contourRed))

hsvBlueFilter = cv2.inRange(hsv, hsvMinBlue, hsvMaxBlue)
_, contourBlue, _ = cv2.findContours(hsvBlueFilter, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
blueContourDraw = img.copy()
cv2.drawContours(image=blueContourDraw, contours=contourBlue, contourIdx=-1, color=(0, 255, 0), thickness=2,
                 lineType=cv2.LINE_AA)

print(len(contourBlue))
if len(contourBlue) > len(contourRed):
    print("B " + str(len(contourBlue)))
elif len(contourRed) > len(contourBlue):
    print("R " + str(len(contourRed)))
else:
    print("S " + str(len(contourRed)))

while True:
    cv2.imshow("HSV", hsv)
    cv2.imshow("dst", dst)
    cv2.imshow("img", img)
    cv2.imshow("hsvRedFilter", hsvRedFilter)
    cv2.imshow("hsvBlueFilter", hsvBlueFilter)
    cv2.imshow("redContourDraw", redContourDraw)
    cv2.imshow("blueContourDraw", blueContourDraw)
    ch = cv2.waitKey(5)
    if ch == 27:
        break
