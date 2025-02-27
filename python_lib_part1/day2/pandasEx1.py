import pandas as pd
import numpy as np

obj = pd.Series([4,7,-5,3])
print(obj)
print(obj.index)
print(obj.values)
print(type(obj.values))
print()

obj2 = pd.Series([4,7,-5,3],index=['a','b','c','d'])
print(obj2)
print()

print(obj2['c'])
print(obj2[['c','b']])
obj2['c'] = 100
print()
print(obj2)
print()

print(obj2 * 2)
print()
print(obj2 > 5)
print(obj2[obj2>5])
print()
print(np.exp(obj2))
print()

data = {'ohio':35000,'texas':72000,'oregon':10000,'utah':5000}
obj3 = pd.Series(data)
print(obj3)