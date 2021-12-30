import numpy as np
from math import sin, cos, pi
import sys

importFile = sys.stdin

q = list(map(int, input().split()))

rot_axes = ['z', 'y', 'y', 'x', 'y', 'x']
const = [25, 400, 560, 35, 515, 80]
trans_axes = ['x', 'z', 'x', 'z', 'x', 'x']
np.set_printoptions(precision=3, suppress=True)


def tr(axis, con):
    a, b, c = 0, 0, 0
    if axis == 'x':
        a = con
    if axis == 'y':
        b = con
    if axis == 'z':
        c = con
    mat = np.array([[1, 0, 0, a], [0, 1, 0, b], [0, 0, 1, c], [0, 0, 0, 1]])
    return mat


def rotationX(ang):
    ang *= pi / 180
    mat = np.array([[1, 0, 0, 0], [0, cos(ang), -sin(-ang), 0], [0, sin(-ang), cos(ang), 0], [0, 0, 0, 1]])
    return mat


def rotationY(ang):
    ang *= pi / 180
    mat = np.array([[cos(ang), 0, sin(ang), 0], [0, 1, 0, 0], [-sin(ang), 0, cos(ang), 0], [0, 0, 0, 1]])
    return mat


def rotationZ(ang):
    ang *= pi / 180
    mat = np.array([[cos(ang), -sin(-ang), 0, 0], [sin(-ang), cos(ang), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    return mat


h = \
    rotationZ(q[0]) @ \
    tr(trans_axes[0], const[0]) @ \
    tr(trans_axes[1], const[1]) @ \
    rotationY(q[1]) @ \
    tr(trans_axes[2], const[2]) @ \
    rotationY(q[2]) @ \
    tr(trans_axes[3], const[3]) @ \
    rotationX(q[3]) @ \
    tr(trans_axes[4], const[4]) @ \
    rotationY(q[4]) @ \
    tr(trans_axes[5], const[5]) @ \
    rotationX(q[5])
x = int(h[0][3])
y = int(h[1][3])
z = int(h[2][3])
s = []
for i in range(int(input())):
    inp = [float(x) for x in input().split()]
    cords = inp[1:]
    number = inp[0]
    cordX = [cords[0], cords[3]]
    cordX.sort()
    cordY = [cords[1], cords[4]]
    cordY.sort()
    cordZ = [cords[2], cords[5]]
    cordZ.sort()
    if cordX[0] < x < cordX[1] and cordY[0] < y < cordY[1] and cordZ[0] < z < cordZ[1]:
        s.append(int(number))
print(len(s))
print(*s)
