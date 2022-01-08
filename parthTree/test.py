import numpy as np
import colorsys


a = (colorsys.rgb_to_hsv(100, 110, 190))
print(a, a[0] * 360, a[1] * 255, a[2])
a = (colorsys.rgb_to_hsv(100 / 255, 110 / 250, 190 / 250))
print(a, a[0] * 360, a[1] * 255, a[2] * 255)


'''
def perp( a ) :
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

# line segment a given by endpoints a1, a2
# line segment b given by endpoints b1, b2
# return
def seg_intersect(a1,a2, b1,b2) :
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = perp(da)
    denom = np.dot( dap, db)
    num = np.dot( dap, dp )
    return (num / denom.astype(float))*db + b1

p1 = np.array( [0.0, 0.0] )
p2 = np.array( [1.0, 0.0] )

p3 = np.array( [4.0, -5.0] )
p4 = np.array( [4.0, 2.0] )

print(seg_intersect(p1, p2, p3, p4))

p1 = np.array( [2.0, 2.0] )
p2 = np.array( [4.0, 3.0] )

p3 = np.array( [6.0, 0.0] )
p4 = np.array( [6.0, 3.0] )

print(seg_intersect(p1, p2, p3, p4))'''
