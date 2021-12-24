from sympy import *

def sign(x):
    if x > 0:
        return 1.0
    if x < 0:
        return -1.0
    return 0.0



l1, l2, l3 = [float(x) for x in input().split()]
angleL1 = [float(x) for x in input().split()]
angleL2 = [float(x) for x in input().split()]
angleL3 = [float(x) for x in input().split()]
x, y = [float(x) for x in input().split()]

a, b, c = symbols('a b c')
d = (solve([l1 * cos(a) + l2 * cos(a + b) + l3 * cos(a + b + c) - x,
            l1 * sin(a) + l2 * sin(a + b) + l3 * sin(a + b + c) - y,
            cos(a + b + c) - 1,
            sin(a + b + c)]))
for i in d:
    if angleL1[0] < i[a] < angleL1[1] and angleL2[0] < i[b] < angleL2[1] and angleL3[0] < i[c] < angleL3[1]:
        print(round(i[a], 5), round(i[b], 5), round(i[c], 5))
        break
else:
    print('None')
