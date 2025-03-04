import pandas as pd
import numpy as np

# data = pd.Series([1,-999,2,-999,-1000,3])
# print(data)
# print()
# # print(data.replace([-999,-1000],np.nan))
# print(data.replace({-999:np.nan,-1000:0}))

np.random.seed(12345)
data = pd.DataFrame(np.random.randn(1000,4))
print(data.head(10))
print()
print(data.describe())

# 1
# data = data.map(lambda x: x if x>-3 else -3).map(lambda x: x if x<3 else 3)

# 2
# data[data>3] = 3
# data[data<-3]=-3

# 3
data[np.abs(data>3)] = np.sign(data)*3
# np.sign() : 음수 = -1, 0 = 0, 양수 = 1 return 하는 함수

print(data.describe())