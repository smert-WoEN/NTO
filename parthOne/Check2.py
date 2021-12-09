import sys
import math
q = [math.radians(int(x)) for x in sys.stdin.readline().split()]
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
# start Pos
Z += fromTableToFirstAngle
Z += fromFirstAngleToSecond * 0
Z += fromSecondToThird * 0
Z += toEndInstrument * 0
Z += instrumentOffset * 1
X += moveFromCenter
X += fromFirstAngleToSecond * 1
X += fromSecondToThird * 1
X += toEndInstrument * 1
X += instrumentOffset * 0
Y += fromFirstAngleToSecond * 0
Y += fromSecondToThird * 0
Y += toEndInstrument * 0
Y += instrumentOffset * 0
print(q)
print(X, Y, Z, XX, YY, ZZ)
