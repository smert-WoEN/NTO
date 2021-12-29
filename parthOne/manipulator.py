h = 400
L1 = 560
L2 = 515
L3 = 80
a = 25
b = 35


q1 = float(input())
q2 = float(input())
q3 = float(input())
q4 = float(input())
q5 = float(input())
q6 = float(input())

l3 = n.matrix([[L3*m.sin(q5)*m.sin(q4)],
             [L3*m.cos(q5) + L2],
             [L3*m.sin(q5)*m.cos(q4)]])

mt3 = n.matrix([[1, 0, 0],
                [0, m.cos(q3), -m.sin(q3)],
                [0, m.sin(q3), m.cos(q3)]])

l2 = n.matrix(n.dot(mt3, l3))

mt2 = n.matrix([[m.cos(q1), m.cos(q1) * m.cos(q2), -m.cos(q1) * m.cos(q2), m.sin(q1)],
                [-m.sin(q1), m.cos(q1) * m.cos(q2), -m.cos(q1) * m.cos(q2), m.cos(q1)],
                [0, m.sin(q2), m.cos(q2), 0]])
m2 = n.matrix([[l2[0][0]], [l2[1][0]], [l2[2][0]], [a]])
l1 = n.matrix(n.dot(mt2, m2))

print(l1)
