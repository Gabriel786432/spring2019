import numpy as np

def upsample(x, multiply_x=3, multiply_y=4):
    final = []
    for i in x:
        new_list = [] #Again, not the best variable names
        for a in i:
            new_list.append(a)
            for j in range(multiply_x-1):
                new_list.append(0)
        final.append(new_list)
        for a in range(multiply_y-1):
            final.append([0 for i in range(len(x[0])*(multiply_x))])
    return final


test = upsample([[1, 2, 6], [3, 4, 3], [5, 6, 5]])
for i in test:
    print(i)
