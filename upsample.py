import numpy as np

def upsample(x):
     y = np.array(x)
     new_list = []
     new_list.append(np.repeat(y,3,axis=1))
     newer_list = new_list[0].tolist()
     really_new_list = [] #Probably not the best variable names
     for i in newer_list:
         for h in range(2):
             really_new_list.append(i)
     return really_new_list

test = upsample([[1, 2, 6], [3, 4, 3], [5, 6, 5]]) #Put any 2d array in here
for i in test:
    print(i)
