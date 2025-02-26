import numpy as np
from numpy.ma.core import zeros

arr1 = np.arange(0,10,1)
print(arr1)
print(type(arr1))

arr2 = np.arange(0,10)
print(arr2)
arr3 = np.arange(10)
print(arr3)
print()

arr4 = np.linspace(-3,3,5)
print(arr4)
print()

arr5 = np.ones([3,4])
print(arr5)
print()

arr6 = np.zeros([3,4])
print(arr6)
print()

arr7 = np.empty([3,4])
print(arr7)
print()

arr8 = np.full([2,3],100)
print(arr8)
print()

arr9 = np.full_like(arr8,50)
print(arr9)
print()
