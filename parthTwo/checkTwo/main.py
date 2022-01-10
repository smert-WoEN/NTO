import colorsys
import time
import math
import numpy as np

s = time.time()
hsvMinRed = np.array((0, 0, 0), np.uint16)
hsvMaxRed = np.array((20, 255, 255), np.uint16)
hsvMinRed2 = np.array((340, 0, 0), np.uint16)
hsvMaxRed2 = np.array((361, 255, 255), np.uint16)
hsvMinBlue = np.array((195, 0, 0), np.uint16)
hsvMaxBlue = np.array((285, 255, 255), np.uint16)

d = []
e = []
for i in open("1").readlines():
    c = [int(a) for a in i.split()]
    if c[0] < -200:
        e.append([c[3], c[4], c[5]])
    d.append(c)
b = np.array(e, dtype=np.float64)
mean = np.mean(b, axis=0)
greyCor = sum(mean) / 3
greyCorNorm = [mean[0] / greyCor, mean[1] / greyCor, mean[2] / greyCor]

c = np.array(d, dtype=np.int32)
d = []
for b in c:
    hsv = colorsys.rgb_to_hsv(min(b[3] * greyCorNorm[0], 256.0) / 256.0, min(256.0, b[4] * greyCorNorm[1]) / 256.0,
                              min(256.0, b[5] * greyCorNorm[2]) / 256.0)
    if (hsv[2] * 100 >= 1600 / (hsv[1] * 100)) and hsv[1] * 100 > 25 and hsv[2] * 100 > 25 \
            and (hsvMinRed[0] < hsv[0] * 360 < hsvMaxRed[0] or hsvMinRed2[0] < hsv[0] * 360 < hsvMaxRed2[0]
                 or hsvMinBlue[0] < hsv[0] * 360 < hsvMaxBlue[0]):
        d.append([b[0], b[1]])
c = np.array(d, dtype=np.int64)
c = np.unique(c, axis=0)
c = (sorted(c, key=lambda x: (-x[1], x[0])))
b = [[c[0]]]
kPrev = [c[0]]
for i in range(1, len(c)):
    d = c[i]
    f = False
    for j in range(len(kPrev)):
        if abs(d[0] - kPrev[j][0]) <= 1 and abs(d[1] - kPrev[j][1]) <= 0:
            kPrev[j] = d
            b[j].append(d)
            break
    else:
        for j in range(len(b)):
            e = b[j]
            for k in e:
                if abs(d[0] - k[0]) <= 9 and abs(d[1] - k[1]) <= 5:
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
    print(len(i))
    if len(i) >= med:
        count += 1
print(count)
print(med)
