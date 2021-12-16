import numpy as np
import colorsys

maxZ = [-10000]*6
c = ""
a = np.genfromtxt("input.txt", delimiter=" ", dtype=np.int32)
a = np.array(sorted(a, key=lambda x: (-x[2])))
for i in range(len(a)):
    b = a[i]
    if b[2] > maxZ[2]:
        maxZ = b
b = []
for i in range(len(a)):
    c = a[i]
    if c[2] > maxZ[2] - 6:
        b.append(c)
c = np.array(b, dtype=np.int32)
d = np.mean(c, axis=0)
print(round(d[0]), round(d[1]), round(d[2]))

