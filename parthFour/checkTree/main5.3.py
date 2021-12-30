import numpy as np
from math import cos, atan2, pi, asin
from sys import stdin as ImportFile


def ang(rm):
    if rm[2][0] != -1 and rm[2][0] != 1:
        y = [asin(rm[2][0]), -pi - asin(rm[2][0])]
        x = [-atan2(rm[2][1] / cos(y[0]), rm[2][2] / cos(y[0])), atan2(rm[2][1] / cos(y[1]), rm[2][2] / cos(y[1]))]
        z = [-atan2((rm[1][0] / cos(y[0])), (rm[0][0] / cos(y[0]))),
             atan2((rm[1][0] / cos(y[1])), (rm[0][0]) / cos(y[1]))]
    else:
        z = 0
        if rm[2][0] == -1:
            y = pi / 2
            x = z + atan2(rm[0][1], rm[0][2])
        else:
            y = -pi / 2
            x = -z + atan2(-rm[0][1], -rm[0][2])
    return [x, y, z]


tr = list(map(float, ImportFile.readline().split()))
tf = list(map(float, ImportFile.readline().split()))
tr = np.reshape(tr, (4, 4))
tf = np.reshape(tf, (4, 4))
tt = np.linalg.inv(tr) @ tf
print(round(tt[0][3], 3), round(tt[1][3], 3), round(tt[2][3], 3), end=' ')
rm = tt[0:3, 0:3]
angles = ang(rm.transpose())
print(round(angles[0][0], 3), round(angles[1][0], 3), round(angles[2][0], 3))
