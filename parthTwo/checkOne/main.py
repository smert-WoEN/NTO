import numpy as np
import colorsys


def convertor(x):
    return [int(x[:2], 16), int(x[2:4], 16), int(x[4:], 16)]


maxZ = -10000
a = np.genfromtxt("input.txt", delimiter=" ", dtype=[('X', np.int32),
                                                ('Y', np.int32), ('Z', np.int32),
                                                ('C', '|S6')])
b = []
for i in range(len(a)):
    c = [a[i][0], a[i][1], a[i][2]]
    c.extend(convertor(a[i][3]))
    b.append(c)
a = (np.array(b, dtype=np.int32))
a = np.array(sorted(a, key=lambda x: (-x[2])))
h = []
for i in range(len(a)):
    b = a[i]
    hsv = colorsys.rgb_to_hsv(b[3]/255.0, b[4]/255.0, b[5]/255.0)
    if b[2] > maxZ and hsv[1] * 100 > 0 and hsv[2] * 100 > (26 ** 2) / (hsv[1] * 100):
        maxZ = b[2]
        h = hsv
hsvMinRed = np.array((0, 0, 0), np.uint16)
hsvMaxRed = np.array((60, 255, 255), np.uint16)
hsvMinRed2 = np.array((300, 0, 0), np.uint16)
hsvMaxRed2 = np.array((360, 255, 255), np.uint16)
hsvMinBlue = np.array((180, 0, 0), np.uint16)
hsvMaxBlue = np.array((300, 255, 255), np.uint16)
colorS = ""
if hsvMinRed[0] < h[0] * 360 < hsvMaxRed[0] or hsvMinRed2[0] < h[0] * 360 < hsvMaxRed2[0]:
    colorS = 'RED'
elif hsvMinBlue[0] < h[0] * 360 < hsvMaxBlue[0]:
    colorS = 'BLUE'
print(-maxZ, colorS)
