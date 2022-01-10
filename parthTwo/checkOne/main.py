import math
import time
import ftplib

import numpy as np
import colorsys

s = time.time()


def convertor(x):
    return [int(x[:2], 16), int(x[2:4], 16), int(x[4:], 16)]


hsvMinRed = np.array((0, 0, 0), np.uint16)
hsvMaxRed = np.array((20, 255, 255), np.uint16)
hsvMinRed2 = np.array((340, 0, 0), np.uint16)
hsvMaxRed2 = np.array((361, 255, 255), np.uint16)
hsvMinBlue = np.array((190, 0, 0), np.uint16)
hsvMaxBlue = np.array((265, 255, 255), np.uint16)
b = []
e = []
f = open("input.txt")
for i in f.readlines():
    c = [x for x in i.split()]
    d = [int(c[0]), int(c[1]), int(c[2])]
    d.extend(convertor(c[3]))
    if d[0] < -200:
        e.append([d[3], d[4], d[5]])
    b.append(d)
a = (np.array(b, dtype=np.float64))

b = np.array(e, dtype=np.float64)
mean = np.mean(b, axis=0)
greyCor = sum(mean) / 3
greyCorNorm = [mean[0] / greyCor, mean[1] / greyCor, mean[2] / greyCor]

maxZ = -1000

h = []
for b in a:
    if b[2] > maxZ:
        hsv = colorsys.rgb_to_hsv(min(b[3] * greyCorNorm[0], 256.0) / 256.0, min(256.0, b[4] * greyCorNorm[1]) / 256.0, min(256.0, b[5] * greyCorNorm[2]) / 256.0)
        if (hsv[2] * 100 >= 1600 / (hsv[1] * 100)) and hsv[1] * 100 > 25 and hsv[2] * 100 > 25\
            and (hsvMinRed[0] < hsv[0] * 360 < hsvMaxRed[0] or hsvMinRed2[0] < hsv[0] * 360 < hsvMaxRed2[0]
                 or hsvMinBlue[0] < hsv[0] * 360 < hsvMaxBlue[0]):
            h = hsv
            maxZ = b[2]
c = np.array(b, dtype=np.float64)
d = (np.mean(c))
colorS = ""
if hsvMinRed[0] < h[0] * 360 < hsvMaxRed[0] or hsvMinRed2[0] < h[0] * 360 < hsvMaxRed2[0]:
    colorS = 'RED'
elif hsvMinBlue[0] < h[0] * 360 < hsvMaxBlue[0]:
    colorS = 'BLUE'
print(int(-maxZ), colorS)
