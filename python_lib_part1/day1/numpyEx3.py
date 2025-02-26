import numpy as np

ldata1 = [10,20,30,40]
ldata2 = [100,200,300,400]
ldata3 = ldata1 + ldata2
print(ldata3)

arr1 = np.array(ldata1)
arr2 = np.array(ldata2)
arr3 = arr1 + arr2
print(arr3)
print()

arr4 = np.array([[1,2,3,4],
                 [5,6,7,8]])
arr5 = np.array([[1,1,1,1],
                 [1,1,1,1]])
print(arr4+arr5)
print()
print(arr4 - arr5)
print()

print(arr4 + 10)
print()

print(1/arr4)
print()

arr5 = np.array([100,200,300,400])
print(arr4+arr5) # broadcast 연산 : 열크기는 달라도 행크기가 같으면 연산가능
print()

arr6 = np.array([[3,2,8],
                [8,3,7]])
arr7 = np.array([[9,1,7],
                 [2,2,9]])

print(arr6>arr7)
