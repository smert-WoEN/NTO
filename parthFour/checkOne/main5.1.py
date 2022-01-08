import math
import time

import numpy as np
import colorsys

s = time.time()

hsvMinRed = np.array((0, 0, 0), np.uint16)
hsvMaxRed = np.array((25, 255, 255), np.uint16)
hsvMinRed2 = np.array((335, 0, 0), np.uint16)
hsvMaxRed2 = np.array((361, 255, 255), np.uint16)
hsvMinBlue = np.array((195, 0, 0), np.uint16)
hsvMaxBlue = np.array((285, 255, 255), np.uint16)
f = open("input.txt")
b = []
for i in f.readlines():
    c = [int(x) for x in i.split()]
    hsv = colorsys.rgb_to_hsv(c[3] / 255.0, c[4] / 255.0, c[5] / 255.0)
    if ((hsv[1] * 100.0 - 100.0) ** 2 + (hsv[2] * 100.0 - 64.0 - 100.0) ** 2) ** 0.5 + \
            ((hsv[1] * 100.0 - 100.0) ** 2 + (hsv[2] * 100.0 + 64.0 - 100.0) ** 2) ** 0.5 < 99 * 2:
        if hsvMinRed[0] < hsv[0] * 360 < hsvMaxRed[0] or hsvMinRed2[0] < hsv[0] * 360 < hsvMaxRed2[0]:
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
    if len(i) > count:
        count = len(i)
        a = i

a = (sorted(a, key=lambda x: (-x[1], x[0])))


mean = np.mean(a, axis=0)
maxMat = np.max(a, axis=0)
maxYCords = []
for i in a:
    if maxMat[1] == i[1]:
        maxYCords = i
        break
a = (sorted(a, key=lambda x: (x[0], -x[1])))
b = []
yPrev = [-1000, 1000]
yPrev2 = [-1000, -1000]
c = []
for i in a:
    if i[0] >= maxYCords[0] and i[0] > yPrev[0]:
        b.append(i)
        yPrev = i
a = (sorted(a, key=lambda x: (x[1], x[0])))
for i in a:
    if i[1] < maxYCords[1] and i[1] > yPrev2[1]:
        c.append(i)
        yPrev2 = i
b = np.array(b, dtype=np.float64)
c = np.array(c, dtype=np.float64)
flag = False
if len(c) > len(b):
    flag = True
    b = []
    for i in range(len(c) // 3 * 2):
        b.append(c[i])
    b = np.array(b, dtype=np.float64)
apr = (np.zeros((len(b), 2), dtype=np.float64))
yRes = np.zeros(len(b), dtype=np.float64)


for i in range(len(b)):
    apr[i] = np.array([b[i][0], 1.], dtype=np.float64)
    yRes[i] = b[i][1]
m, d = np.linalg.lstsq(apr, yRes, rcond=None)[0]

if flag:
    print(round(math.degrees(math.atan2(d, 1))) + 90)
else:
    print(-(round(math.degrees(math.atan2(-1 * m, -1))) - 89))

f1 = open("out.txt", 'w')
for i in a:
    f1.write(str(i[0]) + " " + str(i[1]) + '\n')
f1.close()

