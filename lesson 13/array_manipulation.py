from array import array

import numpy as np

array2d = np.array([
                    [1,2,3,4,5],
                   [6,7,8,9,10]
                        ])
print(array2d)
elemnti = array2d[0,2]
print(elemnti)
dimenzioni =  array2d.ndim
print(dimenzioni)
arryShape = array2d.shape
print(arryShape)

arraySize = array2d.size
print(arraySize)

ndaje = array2d[:2,:2]

print(ndaje)

shuma=np.sum(array2d)
print(shuma)

sum_column = np.sum(array2d,axis=0)
print(sum_column)