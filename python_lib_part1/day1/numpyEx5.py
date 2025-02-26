import numpy as np

arr1 = np.array([[1,2,7],[6,7,9]])
print(arr1)
print()
barr1 = np.array([[True,False,True],[False,False,True]])
print(barr1)
print()

print(arr1[barr1])
print()

barr2 = np.array([True,False,True])
print(arr1[:,barr2])
print()

barr3 = np.array([True,False])
print(arr1[barr3])
