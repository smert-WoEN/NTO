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
b = []
f = open("input.txt")
for i in f.readlines():
    c = [x for x in i.split()]
    d = [int(c[0]), int(c[1]), int(c[2])]
    d.extend(convertor(c[3]))
    b.append(d)
a = (np.array(b, dtype=np.int32))
a = np.array(sorted(a, key=lambda x: (-x[1], x[0])))
maxZ = a[0]
for i in range(1, len(a)):
    if a[i][2] > maxZ[2]:
        maxZ = a[i]
b = []
for i in a:
    if i[2] > maxZ[2] - 6 and maxZ[0] - 10 < i[0] < maxZ[0] + 10 and maxZ[1] - 10 < i[1] < maxZ[1] + 10:
        hls = colorsys.rgb_to_hsv(i[3] / 255.0, i[4] / 255.0, i[5] / 255.0)
        if 10 < hls[1] * 100 < 90 and hls[2] * 100 > 10 and 100 * abs(math.cos(hls[1] * 2 * math.pi)) < hls[2] * 100:
            x = float(hls[0]) * 360
            if x < 60:
                x += 360
            b.append(x)
c = np.array(b, dtype=np.float64)
d = (np.mean(c))
colorS = ""
if d > 300:
    colorS = 'RED'
else:
    colorS = 'BLUE'
print(-maxZ[2], colorS)
