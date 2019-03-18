import numpy as np

array = np.ones((3, 3))
x = 0

for a in range(3):
    for b in range(3):
            array[a][b] = 20-2*x
            x += 1

print(array)
