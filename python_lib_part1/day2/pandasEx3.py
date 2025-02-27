import pandas as pd
import numpy as np

obj1 = pd.Series([4,2,6,9], index=list('abcd'))
print(obj1)
print(obj1['b'])
print(obj1.iloc[1])
print(obj1.iloc[1:3])
print(obj1['b':'d']) # 문자열의 경우 끝문자가 포함됨 (다음문자 없음)

frame = pd.DataFrame(np.arange(16).reshape(4,4),
                     index=['서울','부산','인천','대전'],
                     columns=['one','two','three','four'])
print(frame)
print(frame.loc['부산']['one'])
print(frame.iloc[1,0])
print(frame.iloc[2:,2:])
print(frame.loc['인천':'대전','three':'four'])
print(frame.loc[['인천','대전'],['three','four']])
print()

print(frame.iloc[:,:3][frame.three>5])
