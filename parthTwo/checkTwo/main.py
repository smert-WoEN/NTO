import colorsys
import time

import numpy as np

s = time.time()
hsvMinRed = np.array((0, 0, 0), np.uint16)
hsvMaxRed = np.array((60, 255, 255), np.uint16)
hsvMinRed2 = np.array((300, 0, 0), np.uint16)
hsvMaxRed2 = np.array((360, 255, 255), np.uint16)
hsvMinBlue = np.array((180, 0, 0), np.uint16)
hsvMaxBlue = np.array((300, 255, 255), np.uint16)

p = open("input.txt")
d = []
for i in p.readlines():
    x = [int(a) for a in i.split()]
    h = colorsys.rgb_to_hsv(x[3] / 255.0, x[4] / 255.0, x[5] / 255.0)
    if x[2] > -400 and ((h[1] * 100.0 - 100.0) ** 2 + (h[2] * 100.0 - 64.0 - 100.0) ** 2) ** 0.5 + \
            ((h[1] * 100.0 - 100.0) ** 2 + (h[2] * 100.0 + 64.0 - 100.0) ** 2) ** 0.5 < 99 * 2 and \
            (hsvMinRed[0] < h[0] * 360 < hsvMaxRed[0] or hsvMinRed2[0] < h[0] * 360 < hsvMaxRed2[0]):
        d.append([x[0], x[1]])
c = np.array(d, dtype=np.int32)
c = np.unique(c, axis=0)
c = (sorted(c, key=lambda x: (-x[1], x[0])))
b = [[c[0]]]
kPrev = [c[0]]
for i in range(1, len(c)):
    d = c[i]
    f = False
    for j in range(len(kPrev)):
        if abs(d[0] - kPrev[j][0]) <= 2 and abs(d[1] - kPrev[j][1]) <= 0:
            kPrev[j] = d
            b[j].append(d)
            break
    else:
        for j in range(len(b)):
            e = b[j]
            for k in e:
                if abs(d[0] - k[0]) <= 7 and abs(d[1] - k[1]) <= 7:
                    kPrev[j] = d
                    b[j].append(d)
                    f = True
                    break
            if f:
                break
        if not f:
            b.append([d])
            kPrev.append(d)

count = 0
med = 0
for i in b:
    med += len(i)
med = med / len(b) / 2
for i in b:
    if len(i) >= 75:
        count += 1
print(count)
