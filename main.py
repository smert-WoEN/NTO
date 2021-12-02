import cv2
import numpy
import numpy as np

if __name__ == '__main__':
    def nothing(*arg):
        pass

a1 = (np.zeros((1024,1280,3), dtype=np.uint8))
f = open("2")
for i in range(1024):
    x = f.readline().split()
    for j in range(1280):
        a = [x[j][:2], x[j][2:4], x[j][4:]]
        b = [int(a[0], 16), int(a[1], 16), int(a[2], 16)]
        a1[i][j] = b
        #a1 = np.append(a1, [[b]], axis=1)
        #print(a1)
        #print([b]+ [b])
        #a1 = np.append(a1, [[b] + [b]], axis=0)
print(a1)
while True:
    cv2.imshow("HSV", a1)
    ch = cv2.waitKey(5)
    if ch == 27:
        break

#inputMat = np.genfromtxt("0", delimiter=" ", dtype=str)

#print(len(inputMat))
#print(inputMat)
