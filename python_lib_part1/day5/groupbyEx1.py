import pandas as pd
import numpy as np

df = pd.DataFrame({'key1':['a','a','b','b','a'],
                   'key2':['one','two','one','two','one'],
                   'data1':np.random.randn(5),
                   'data2':np.random.randn(5)})
print(df)
print()

grouped1 = df.groupby('key1')
print(grouped1)
print()

for name, gd in grouped1:
    print(name)
    print(gd, end='\n\n')

print()
print(grouped1[['data1', 'data2']].mean())
print()
print(grouped1[['data2']].mean())
print()

print(list(grouped1))
print()
ldata = list(grouped1)
print(ldata[1][1])
print()

print(dict(ldata)['b'])
print()

grouped2 = df.groupby(['key1','key2'])
for gd in grouped2:
    print(gd, end='\n\n')
print()

print(grouped2[['data1','data2']].sum())
