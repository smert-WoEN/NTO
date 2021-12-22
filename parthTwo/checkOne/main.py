import math
import time

import numpy as np
import colorsys

s = time.time()


def convertor(x):
    return [int(x[:2], 16), int(x[2:4], 16), int(x[4:], 16)]


hsvMinRed = np.array((1, 0, 0), np.uint16)
hsvMaxRed = np.array((45, 255, 255), np.uint16)
hsvMinRed2 = np.array((315, 0, 0), np.uint16)
hsvMaxRed2 = np.array((361, 255, 255), np.uint16)
hsvMinBlue = np.array((195, 0, 0), np.uint16)
hsvMaxBlue = np.array((285, 255, 255), np.uint16)
maxZ = -10000
b = []
f = open("input.txt")
for i in f.readlines():
    c = [x for x in i.split()]
    d = [int(c[0]), int(c[2]), int(c[2])]
    d.extend(convertor(c[3]))
    b.append(d)
a = (np.array(b, dtype=np.int32))
a = np.array(sorted(a, key=lambda x: (-x[2])))
h = []
for i in range(len(a)):
    b = a[i]
    hls = colorsys.rgb_to_hls(b[3] / 255.0, b[4] / 255.0, b[5] / 255.0)
    if b[2] > maxZ and (5 < hls[1] * 100 < 95 and 100 * abs(math.cos(hls[1] * 2 * math.pi)) < hls[2] * 100) and \
            (hsvMinRed[0] <= hls[0] * 360 < hsvMaxRed[0] or
             hsvMinRed2[0] <= hls[0] * 360 < hsvMaxRed2[0] or
             hsvMinBlue[0] <= hls[0] * 360 < hsvMaxBlue[0]):
        maxZ = b[2]
        h = hls

colorS = ""
if hsvMinRed[0] <= h[0] * 360 < hsvMaxRed[0] or hsvMinRed2[0] <= h[0] * 360 < hsvMaxRed2[0]:
    colorS = 'RED'
elif hsvMinBlue[0] <= h[0] * 360 < hsvMaxBlue[0]:
    colorS = 'BLUE'
print(-maxZ, colorS)
