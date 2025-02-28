import pandas as pd
import numpy as np


data = pd.Series([1, np.nan, 3.5, np.nan, 7])
print(data)
print(data.dropna()) # NaN 제외
print()
print(data.notnull()) # null 값 있는지 확인
print(data[data.notnull()]) # dropna 처럼 역할
print()

np.random.seed(12345)
frame = pd.DataFrame(np.random.randn(7,3),
                     columns=['seoul','busan','incheon'])
frame.iloc[:4,1] = np.nan
frame.iloc[:2,2] = np.nan
print(frame)
print()

print(frame.fillna(0)) # NaN 값을 해당 값으로 초기화
print()
# 각 column에 넣을 값 지정 2가지 방식
print(frame.fillna({'busan':-5,'incheon':0})) # 딕셔너리(dataframe)
print()
print(frame.fillna(pd.Series([-5,0],index=['busan','incheon']))) # series
print()

print(frame.mean(axis=0))
print()
print(frame.fillna(frame.mean(axis=0)))
print()
# 보간 메소드 사용
# print(frame.fillna(method='bfill')) # deprecated 아래 메소드 사용
print(frame.bfill())

data = {'one':np.arange(7),
        'two':np.arange(7,0,-1),
        'three':[1,1,1,2,2,2,2],
        'four':[0,1,2,0,1,2,3]}

# 데이터의 값으로 인덱스 설정 방법 및 다중 인덱스 설정 방법
frame2 = pd.DataFrame(data)
print(frame2)
frame3 = frame2.set_index('three')
print(frame3)
print()
print(frame2.set_index(['two','four']))

