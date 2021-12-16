import math as m
import sys
import numpy as n

h = 400
L1 = 560
L2 = 515
L3 = 80
a = 25
b = 35

class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def coords_conv(l3, L1, a, b):

    mt3 = n.matrix([[1,0,0],
                    [0,m.cos(q3),-m.sin(q3)],
                    [0,m.sin(q3),m.cos(q3)]])
    m3 = n.matrix([l3.x, l3.y, l3.z]) 
    l2 = Vector(mt3*m3)

    l2.y = l2.y + L1
    l2.z = l2.z + b

    mt2 = n.matrix([[m.cos(q1), m.cos(q1)*m.cos(q2),-m.cos(q1)*m.cos(q2),m.sin(q1)], 
                    [-m.sin(q1), m.cos(q1)*m.cos(q2),-m.cos(q1)*m.cos(q2),m.cos(q1)],
                    [0, m.sin(q2), m.cos(q2), 0]])
    m2 = n.matrix(l2.x, l2.y, l2.z, a)
    l1 = Vector(mt2*m2)

    return l1

def angle(a, b):
    angle = a.x*b.x + a.y*b.y + a.z*b.z
    return angle

q1, q2, q3, q4, q5, q6 = sys.stdin

l3 = Vector(L3*m.sin(q5)*m.sin(q4), L3*m.cos(q5) + L2, L3*m.sin(q5)*m.cos(q4))
l1 = coords_conv(l3, L1, a, b)

i4 = Vector(m.cos(q4), m.sin(q4)*m.sin(q5), m.sin(q4)*m.cos(q5))
j4 = Vector(m.cos(q4)*m.sin(q5), m.cos(q5), m.sin(q4)*m.sin(q5))
k4 = Vector(m.sin(q4)*m.cos(q5), m.sin(q5), m.cos(q4)*m.cos(q5))

i4 = coords_conv(i4, 0, 0, 0)
j4 = coords_conv(j4, 0, 0, 0)
k4 = coords_conv(k4, 0, 0, 0)

i1 = Vector(1, 0, 0)
j1 = Vector(0, 1, 0)
k1 = Vector(0, 0, 1)

xx = angle(i1, i4)
yy = angle(j1, j4)
zz = angle(k1, k4)
sys.stdout(l1.y, l1.x, l1.z, xx, yy, zz)
                                                    
