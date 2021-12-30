import sys
from math import *

q1 = [(int(x)) for x in sys.stdin.readline().split()]
q = [radians(x) for x in q1]
A1 = [-170, 170]
moveFromCenter = 25
fromTableToFirstAngle = 400
A2 = [-190, 45]
fromFirstAngleToSecond = 560
A3 = [-120, 156]
fromSecondToThird = 515
A4 = [-185, 185]  # inThirdLever
A5 = [-120, 120]
toEndInstrument = 80
instrumentOffset = 35
A6 = [-350, 350]
X = 0
Y = 0
Z = 0
XX = 0
YY = 0
ZZ = 0
Z += fromTableToFirstAngle
Z -= fromFirstAngleToSecond * sin(q[1])
Z -= fromSecondToThird * sin(q[1] + q[2])
Z += instrumentOffset * cos(q[1] + q[2])
Z -= toEndInstrument * sin(q[1] + q[2] + q[4])
X += moveFromCenter
X += fromFirstAngleToSecond * cos(q[1]) * cos(q[0])
X += fromSecondToThird * cos(q[0]) * cos(q[1] + q[2])
X += instrumentOffset * cos(q[0]) * sin(q[1] + q[2])
X += toEndInstrument * cos(q[1] + q[2] + q[4] * cos(q[3])) * cos(q[0]) * cos(q[3])
Y += fromFirstAngleToSecond * cos(q[1]) * sin(q[0])
Y += fromSecondToThird * sin(q[0]) * cos(q[1] + q[2])
Y += instrumentOffset * sin(q[0]) * sin(q[1] + q[2])
Y += toEndInstrument * cos(q[1] + q[2] + q[4] * cos(q[3])) * sin(q[0]) * cos(q[3])
ZZ -= q1[0]
ZZ -= q1[3] * sin(q[1] + q[2])
ZZ -= q1[4] * sin(q[3]) * cos(q[1] + q[2])
ZZ -= q1[5] * sin(q[1] + q[2] + q[4] * cos(q[3]))
XX -= q1[1] * sin(q[0])
XX -= q1[2] * sin(q[0])
XX -= q1[3] * cos(q[1] + q[2]) * cos(q[0])
XX -= q1[4] * sin(q[0] * cos(q[1] + q[2]) + q[3] * sin(q[1] + q[2])) * \
      cos(q[3] * cos(q[1] + q[2]) + q[0] * sin(q[1] + q[2]))
XX -= q1[5] * cos(q[0]) * cos(q[1] + q[2] + q[4] * cos(q[3]))
YY += q1[1] * cos(q[0])
YY += q1[2] * cos(q[0])
YY += q1[3] * cos(q[1] + q[2]) * sin(q[0])
YY += q1[4] * cos(q[0] * cos(q[1] + q[2]) + q[3] * sin(q[1] + q[2])) * \
      cos(q[3] * cos(q[1] + q[2]) + q[0] * sin(q[1] + q[2]))
YY += q1[5] * sin(q[0]) * cos(q[1] + q[2] + q[4] * cos(q[3]))
X, Y, Z, XX, YY, ZZ = (
int(round(X, 5)), int(round(-Y, 5)), int(round(Z, 5)), int(round(XX, 5)), int(round(YY, 5)), int(round(ZZ, 5)))
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
    print(X, Y, Z, XX, YY, ZZ)
    print(cordX, cordY, cordZ)
    if cordX[0] < X < cordX[1] and cordY[0] < Y < cordY[1] and cordZ[0] < Z < cordZ[1]:
        s.append(int(number))
print(len(s))
print(*s)
