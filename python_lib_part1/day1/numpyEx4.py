import numpy as np

arr1 = np.array([9,2,3,4,1,5,6,7,8])
print(arr1[0])
print(arr1[-1])
print(arr1[2:5])
print()

arr2 = np.array([[2,3,6,8],
                 [3,5,9,7],
                 [0,10,20,30]])
print(arr2)
print()
print(arr2[1,0])
print(arr2[1][0])
print()

print(arr2[1:,2:])
print(arr2[1:][2:])
