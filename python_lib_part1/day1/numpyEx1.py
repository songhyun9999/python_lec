import numpy as np

ldata1 = [10,20,30,40]
print(ldata1)
print(type(ldata1))
print()

arr1 = np.array(ldata1)
print(arr1)
print(type(arr1))

ldata2 = [[1,2,3,4],[5,6,7,8]]
print(ldata2)
arr2 = np.array(ldata2)
print(arr2)
print(arr2.shape)
print(arr2.dtype)
print()

ldata3 = [10.4,23,666.43,11]
print(ldata3)
arr3 = np.array(ldata3)
print(arr3)
arr4 = np.array(ldata3,np.int32)
print(arr4)
print(arr4.dtype)

arr5 = arr4.astype(np.float64)
print(arr5)

ldata4 = ['1.23','333.33',411]
arr6 = np.array(ldata4,np.float64)
print(arr6)