import numpy as np
import pandas as pd

np.random.seed(12345)

frame = pd.DataFrame(np.random.randn(5,5),
                     index=['joe','steve','wes','jim','travis'],
                     columns=list('abcde'))
print(frame)
print()

mapping = {'a':'red', 'b':'red', 'c':'blue', 'd':'blue', 'e':'red'}
grouped1 = frame.groupby(mapping, axis=1)
print()
print(grouped1.sum())
print()

labeling = ['one', 'one', 'one', 'two', 'two']
grouped2 = frame.groupby(labeling)
print(grouped2.mean())
print()

grouped3 = frame.groupby(len)
print(grouped3.sum())
print()

print(frame.groupby(lambda x : x[-1]).mean())
print()

print(frame.groupby([len, labeling]).min())