import numpy as np
from cv2 import cv2

if __name__ == '__main__':
    def nothing(*arg):
        pass

hsvMinRed = np.array((0, 110, 0), np.uint8)
hsvMaxRed = np.array((50, 255, 255), np.uint8)
hsvMinBlue = np.array((65, 20, 0), np.uint8)
hsvMaxBlue = np.array((140, 255, 255), np.uint8)

dst = cv2.imread("assignments.jpg", cv2.IMREAD_COLOR)
img = cv2.GaussianBlur(dst, (5, 5), cv2.BORDER_DEFAULT)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsvRedFilter = cv2.inRange(hsv, hsvMinRed, hsvMaxRed)
contourRed, img4 = cv2.findContours(hsvRedFilter, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
redContourDraw = img.copy()
cv2.drawContours(image=redContourDraw, contours=contourRed, contourIdx=-1, color=(0, 255, 0), thickness=2,
                 lineType=cv2.LINE_AA)
print(len(contourRed))

hsvBlueFilter = cv2.inRange(hsv, hsvMinBlue, hsvMaxBlue)
contourBlue, img6 = cv2.findContours(hsvBlueFilter, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
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
