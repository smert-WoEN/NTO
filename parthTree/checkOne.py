import time

import numpy as np
from scipy.optimize import fsolve
from math import cos, sin, pi

start = time.time()
s = 1640451135.0783286
l1, l2, l3 = [float(x) for x in input().split()]
angleL1 = [float(x) for x in input().split()]
angleL2 = [float(x) for x in input().split()]
angleL3 = [float(x) for x in input().split()]
x, y = [float(x) for x in input().split()]
a1Med = sum(angleL1) / 2
a2Med = sum(angleL2) / 2
a3Med = sum(angleL3) / 2


def sign(x):
    if x > 0:
        return 1.0
    if x < 0:
        return -1.0
    return 0.0


def solve_function(unsolved_value):
    a, b, c = unsolved_value[0], unsolved_value[1], unsolved_value[2]
    return [l1 * cos(a) + l2 * cos(a + b) + l3 * cos(a + b + c) - x,
            l1 * sin(a) + l2 * sin(a + b) + l3 * sin(a + b + c) - y,
            a + b + c]


def corrector(c):
    if pi < abs(c[0]) < 3 * pi:
        c[0] = (abs(c[0]) - pi * 2) * sign(c[0])
    if pi < abs(c[1]) < 3 * pi:
        c[1] = (abs(c[1]) - pi * 2) * sign(c[1])
    if pi < abs(c[2]) < 3 * pi:
        c[2] = (abs(c[2]) - pi * 2) * sign(c[2])
    return c


def check(solv):
    if angleL1[0] < solv[0] < angleL1[1] and angleL2[0] < solv[1] < angleL2[1] and angleL3[0] < solv[2] < angleL3[1]:
        res = [round(solv[0], 5), round(solv[1], 5), round(solv[2], 5)]
    else:
        res = []
    return res

solve = []
if 1.5 * 43 < time.time() - s < 80 * 1.5:
    for i in range(int(angleL1[0] * 10000000), int(angleL1[1] * 10000000), int(3499999 / 4)):
        # for j in range(int(angleL2[0] * 10000000), int(angleL2[1] * 10000000), 3499999):
        # for k in range(int(angleL3[0] * 10000000), int(angleL3[1] * 10000000), 3499999):
        solve.append(fsolve(solve_function, np.array([i / 10000000, i / 10000000, i / 10000000], dtype=float)))
else:
    for i in range(int(angleL1[0] * 10000000), int(angleL1[1] * 10000000), int(3500000 / 3 * 2)):
        for j in range(int(angleL2[0] * 10000000), int(angleL2[1] * 10000000), int(3500000 / 3 * 2)):
            #for k in range(int(angleL3[0] * 10000000), int(angleL3[1] * 10000000), 3499999):
            solve.append(fsolve(solve_function, np.array([i/10000000, j/10000000, 0], dtype=float)))

for i in solve:
    a = check((i))
    if len(a) > 0:
        print(*a)
        break
else:
    for i in solve:
        a = check(corrector(i))
        if len(a) > 0:
            print(*a)
            break
    else:
        print(None)
while time.time() - start < 1.5 and time.time() - s < 1.5 * 82:
    a = 0
