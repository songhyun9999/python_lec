import numpy as np

np.random.seed(12345)
arr = np.random.randn(100)
print((arr>0).sum())

bools = np.array([[False,False,True,False],
                  [False,False,True,True]])
print(bools.any(0))
print(bools.all(0))
print()

data = np.random.randn(10,4) * 4
print(data)
print()
print(data[(data>3).any(axis=1)])