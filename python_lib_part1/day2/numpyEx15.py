import numpy as np

np.random.seed(12345)

# loc : 평균(mean), scale : 표준편차(std), size : 만들어지는 ndarray size
data = np.random.normal(loc=10,scale=5,size=[100,3])
print(data)
print(data.mean())
print(data.std())
print()

data2 = np.random.randn(100,3)
print(data2)
print(data2.mean())
print(data2.std())
print()

data3 = np.random.randint(low=1,high=10,size=[10,3])
print(data3)
print()

data4 = np.arange(10)
print(data4)
np.random.shuffle(data4) # 원본을 변경
print(data4)
print()

data5 = np.arange(10)
print(data5)
print(np.random.permutation(data5)) # 원본은 변경 X
print(data5)