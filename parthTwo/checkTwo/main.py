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

p = open("1")
d = []
for i in p.readlines():
    c = [int(a) for a in i.split()]
    hls = colorsys.rgb_to_hls(c[3] / 255.0, c[4] / 255.0, c[5] / 255.0)
    if 5 < hls[1] * 100 < 95 and hls[2] * 100 > 5 and 100 * abs(math.cos(hls[1] * 2 * math.pi)) < hls[2] * 100:
        if hsvMinRed[0] < hls[0] * 360 < hsvMaxRed[0] or hsvMinRed2[0] < hls[0] * 360 < hsvMaxRed2[0]:
            d.append([c[0], c[1]])
c = np.array(d, dtype=np.int32)
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
