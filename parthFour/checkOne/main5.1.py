import math
import time

import numpy as np
import colorsys

s = time.time()

hsvMinRed = np.array((0, 0, 0), np.uint16)
hsvMaxRed = np.array((20, 255, 255), np.uint16)
hsvMinRed2 = np.array((340, 0, 0), np.uint16)
hsvMaxRed2 = np.array((361, 255, 255), np.uint16)
hsvMinBlue = np.array((195, 0, 0), np.uint16)
hsvMaxBlue = np.array((285, 255, 255), np.uint16)
b = []
f = open("1")
f1 = open("out.txt", "w")
b = []
for i in f.readlines():
    c = [int(x) for x in i.split()]
    hls = colorsys.rgb_to_hls(c[3] / 255.0, c[4] / 255.0, c[5] / 255.0)
    if 15 < hls[1] * 100 < 85 and hls[2] * 100 > 15 and 100 * abs(math.cos(hls[1] * 2 * math.pi)) < hls[2] * 100:
        if hsvMinRed[0] < hls[0] * 360 < hsvMaxRed[0] or hsvMinRed2[0] < hls[0] * 360 < hsvMaxRed2[0]:
            b.append([c[0], c[1]])

c = np.array(b)
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
a = []
for i in b:
    print(len(i))
    if len(i) > count:
        count = len(i)
        a = i
print()
print(len(a))
print(len(c))
print(time.time() - s)
a = (sorted(a, key=lambda x: (-x[1], x[0])))



minA = [10000, 10000]
for i in a:
    f1.write(str(i[0]) + ' ' + str(i[1]) + '\n')
    if i[0] < minA[0]:
        minA = i
    elif i[0] == minA[0] and i[1] < minA[1]:
        minA = i
print(minA)
f1.write(str(0) + ' ' + str(0) + '\n')
f1.close()
