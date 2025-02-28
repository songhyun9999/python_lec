import numpy as np
import pandas as pd


np.random.seed(12345)

frame = pd.DataFrame(np.random.randn(4,3),
                     columns=['서울','부산','인천'],
                     index=['김가','이가','최가','오가'])
print(frame)
print()

f1 = lambda x: x.max() - x.min()
f2 = lambda x: x.sum()
result = frame.apply(f1,axis=0)
print(result)
print()
print(frame.apply(f1,axis=1))
print()

def f3(x):
    return pd.Series([x.mean(),x.std()],index=['mean','std'])
result2 = frame.apply(f3,axis=0)
print(result2)
print()

f4 = lambda x: f'{x:.2f}'
# result3 = frame.applymap(f4) # deprecated
result3 = frame.map(f4)
print(result3)
print()

print(frame['인천'].map(f4))
print(frame['인천'].apply(f4))
print()

