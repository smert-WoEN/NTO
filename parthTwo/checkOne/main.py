import numpy as np
import colorsys


def convertor(x):
    return [int(x[:2], 16), int(x[2:4], 16), int(x[4:], 16)]


maxZ = 10000
maxY = -float('inf')
color = ""
a = np.genfromtxt("1", delimiter=" ", dtype=np.str_)
Y = 0
for i in range(len(a)):
    b = a[i]
    if Y - int(b[1]) != 0:
        Y = int(b[1])
    if -int(b[2]) < maxZ:
        maxY = int(b[1])
        maxZ = -int(b[2])
        color = b[3]
c = convertor(color)
h = colorsys.rgb_to_hsv(c[0], c[1], c[2])
hsvMinRed = np.array((0, 0, 0), np.uint8)
hsvMaxRed = np.array((60, 255, 255), np.uint8)
hsvMinBlue = np.array((60, 0, 0), np.uint8)
hsvMaxBlue = np.array((255, 255, 255), np.uint8)
colorS = ""
if hsvMinRed[0] < h[0] * 255 < hsvMaxRed[0]:
    colorS = 'RED'
elif hsvMinBlue[0] < h[0] * 255 < hsvMaxBlue[0]:
    colorS = 'BLUE'
print(maxZ, colorS)

