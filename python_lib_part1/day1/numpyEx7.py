import numpy as np

arr = np.arange(10)
print(arr)
print(np.exp(arr))
print(np.square(arr))
print(np.sqrt(arr))
print()

print(np.cos(arr))
print(np.sin(arr))
print()

x = np.array([5,2,8,6,11,6,99])
y = np.array([1,2,3,4,5,66,77])
print(np.maximum(x,y))
print(np.minimum(x,y))
print()

arr2 = np.array([32.23, 5.22, 0.321, 491.93])
print(np.modf(arr2))