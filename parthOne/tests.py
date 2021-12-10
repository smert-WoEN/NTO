import sys
import time

import numpy as np

if __name__ == '__main__':
    def nothing(*arg):
        pass
s = time.time()
a = np.genfromtxt("0", delimiter=" ", dtype=str)

print(a)
print(time.time()-s)

f = open('0')

s = time.time()
b = np.asmatrix(f.readlines(), dtype=np.str_, delimiter=' ')
print(b)
print(time.time()-s)
