import time

import numpy as np
s = time.time()
a = np.genfromtxt("1", delimiter=" ", dtype=[('X', np.int32),
                                                ('Y', np.int32), ('Z', np.int32),
                                                ('C', '|S6')])

print(a)
c = np.array(sorted(a, reverse=True, key=lambda x: x[1]))
print(*c)
print(a[0][3].decode('UTF-8'))
print(time.time()-s)
