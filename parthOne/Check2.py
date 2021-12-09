import sys
import math


def sign(n):
    if n > 0:
        return 1.0
    elif n < 0:
        return -1.0
    return 0.0


q = [math.radians(-0), math.radians(0), math.radians(-90), 0, 0, 0]#[math.radians(int(x)) for x in sys.stdin.readline().split()]
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
# start Pos сделано до оси A4 ( это вращение)
Z += fromTableToFirstAngle
Z -= fromFirstAngleToSecond * math.sin(q[1])
Z -= fromSecondToThird * math.sin(q[1] + q[2])
Z += instrumentOffset * math.cos(q[1] + q[2])
Z += toEndInstrument * 0
X += moveFromCenter
X += fromFirstAngleToSecond * math.cos(q[1]) * math.cos(q[0])
X += fromSecondToThird * math.cos(q[0]) * math.cos(q[1] + q[2])
X += instrumentOffset * math.cos(q[0]) * math.sin(q[1] + q[2])
X += toEndInstrument * 0
Y += fromFirstAngleToSecond * math.cos(q[1]) * math.sin(q[0])
Y += fromSecondToThird * math.sin(q[0]) * math.cos(q[1] + q[2])
Y += instrumentOffset * math.sin(q[0]) * math.sin(q[1] + q[2])
Y += toEndInstrument * 0
print(q)
print(round(X), round(Y), round(Z), XX, YY, ZZ)
