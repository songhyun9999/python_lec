import numpy as np

np.random.seed(12345)

values = np.array([5,0,1,3,2])
indexer = values.argsort()
print(indexer)

arr = np.random.randn(3,5)
arr[0] = values
print(arr)
print(arr[:,arr[0].argsort()])
print()

data = np.arange(30).reshape(5,6)
np.random.shuffle(data)
print(data)
print()
# print(data[data[:,0].argsort(),:])
print(data[np.argsort(data[:,0]),:])