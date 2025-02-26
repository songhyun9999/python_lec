import numpy as np

arr1 = np.arange(8)

print(arr1)
print()

print(arr1.reshape((4,2)))
print()
print(arr1.reshape(2,2,2))
print()

arr2 = np.array([[10,20],
                 [30,40],
                 [50,60]])
print(arr2)
print()

print(arr2.transpose())