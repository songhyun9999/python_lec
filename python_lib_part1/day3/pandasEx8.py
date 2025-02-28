import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.arange(12).reshape(3,4),
                   columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20).reshape(4,5),
                   columns=list('abcde'))

print(df1)
print()
print(df2)
print()

print(df1+df2) # 크기가 다를때 부족한 빈 부분은 NAN이 됨
print()
print(df1.add(df2,fill_value=0)) # 크기가 다를때 부족한 빈 부분은 0으로 초기화
print()

frame = pd.DataFrame(np.arange(12).reshape(4,3),
                     columns=list('bde'),
                     index=['one','two','three','four'])
print(frame)
print()
sdata = frame.iloc[0]
print(sdata)
print()
print(frame-sdata) # broadcast 연산 적용됨 -> frame 의 모든 행에 sdata를 뺌

