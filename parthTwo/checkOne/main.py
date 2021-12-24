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
    d = [int(c[0]), int(c[2]), int(c[2])]
    d.extend(convertor(c[3]))
    b.append(d)
a = (np.array(b, dtype=np.int32))
maxZ = (np.max(a, axis=0))[2]
counterR = 0
counterB = 0
for i in a:
    if i[2] > maxZ - 2:
        hls = colorsys.rgb_to_hls(i[3] / 255.0, i[4] / 255.0, i[5] / 255.0)
        if (10 < hls[1] * 100 < 90 and hls[2] * 100 > 10 and 100 * abs(math.cos(hls[1] * 2 * math.pi)) < hls[2] * 100):
            if (hsvMinRed[0] <= hls[0] * 360 < hsvMaxRed[0] or hsvMinRed2[0] <= hls[0] * 360 < hsvMaxRed2[0]):
                counterR += 1
            elif hsvMinBlue[0] <= hls[0] * 360 < hsvMaxBlue[0]:
                counterB += 1
colorS = ""
if counterR > counterB:
    colorS = 'RED'
else:
    colorS = 'BLUE'
print(-maxZ, colorS)

