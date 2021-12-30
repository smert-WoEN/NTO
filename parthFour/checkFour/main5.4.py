from math import cos, sin, radians, atan2


angle1 = [-132, 132]
angle2 = [-145, 145]
axis3 = [-200, 0]
angle3 = [-355, 355]
const = [225, 275, 200]
x = 0
y = 0
z = 0
inp = [int(x) for x in input().split()]
angle = []
for i in range(-132, 132 + 1):
    for j in range(-145, 145 + 1):
        a1 = radians(i)
        a2 = radians(j)
        if round(const[0] * cos(a1) + const[1] * cos(a1 + a2)) == inp[0] \
                and round(const[0] * sin(a1) + const[1] * sin(a1 + a2)) == inp[1]:
            angle = [i, j, axis3[0] + inp[2]]
if angle[0] + angle[1] == 0:
    angle.append(0)
else:
    for i in range(-355, 355 + 1):
        if -90 < angle[1] < 90 and angle[0] + i == 90:
            angle.append(i - 188)
        elif angle[0] + i == 180 and not (-90 < angle[1] < 90):
            angle.append(i + 7)
print(*angle)
