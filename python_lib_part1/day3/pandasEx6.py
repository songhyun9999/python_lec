import pandas as pd
import numpy as np

sdl = pd.Series(np.arange(5),index=list('abcde'))
print(sdl)
print()

print(sdl.drop(['c','e'])) # 원본 변경 X
print(sdl)
print()

sdl.drop(['c','e'],inplace=True) # 원본 변경
print(sdl)
print()

frame = pd.DataFrame(np.arange(16).reshape(4,4),
                     index = list('abcd'),
                     columns=['one','two','three','four'])

print(frame)
print()
print(frame.drop('a'))
print(frame.drop('one',axis=1))
print()
print(frame.drop(index='a',columns='one'))