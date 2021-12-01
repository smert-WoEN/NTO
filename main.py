import numpy

f = open("0")
a1 = numpy.array([f.readline().split()], dtype=str)
for i in range(1023):
    a1 = numpy.append(a1, [f.readline().split()], axis=0)

print(len(a1))


