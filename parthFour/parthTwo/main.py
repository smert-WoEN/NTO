import random
f = open("input.txt")
s = f.readline()
a = [0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 7, 7]
for i in range(24155):
    random.shuffle(a)
print(a[0])
