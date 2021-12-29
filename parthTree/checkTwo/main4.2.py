import math
import numpy as np


def perp( a ) :
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b


def seg_intersect(a1,a2, b1,b2):
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = perp(da)
    denom = np.dot( dap, db)
    num = np.dot( dap, dp )
    return (num / denom.astype(float))*db + b1


n = int(input())
cord = [float(x) for x in input().split()]
x = math.cos(cord[1]) * cord[0]
y = math.sin(cord[1]) * cord[0]
cords = [[0, 0], [x, y]]
angle = cord[1]
for i in range(1, n):
    cord = [float(x) for x in input().split()]
    angle += cord[1]
    x += (math.cos(angle) * cord[0])
    y += (math.sin(angle) * cord[0])
    cords.append([x, y])
per = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        point1 = cords[i]
        point2 = cords[i - 1]
        point3 = cords[j]
        point4 = cords[j - 1]
        p = seg_intersect(np.array(cords[i]), np.array(cords[i - 1]), np.array(cords[j]), np.array(cords[j - 1]))
        p = [round(p[0], 6), round(p[1], 6)]
        if not math.isnan(p[0]):
            x0 = round(min(point1[0], point2[0]), 6)
            x1 = round(max(point1[0], point2[0]), 6)
            y0 = round(min(point1[1], point2[1]), 6)
            y1 = round(max(point1[1], point2[1]), 6)
            x2 = round(min(point3[0], point4[0]), 6)
            x3 = round(max(point3[0], point4[0]), 6)
            y2 = round(min(point3[1], point4[1]), 6)
            y3 = round(max(point3[1], point4[1]), 6)
            if x0 < p[0] < x1 and y0 < p[1] < y1 and x2 < p[0] < x3 and y2 < p[1] < y3:
                for k in per:
                    if p[0] == k[0] and p[1] == k[1]:
                        break
                else:
                    per.append(p)
print(len(per))
for i in per:
    print(*i)
