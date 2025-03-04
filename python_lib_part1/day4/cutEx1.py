import numpy as np
import pandas as pd

ages = [20,22,25,27,21,23,37,31,61,45,41,32]
bins = [18,25,35,60,100]
cdata = pd.cut(ages,bins) # bins 의 범위에 대해 ages 의 각 값이 속하는 범위를 표현
# 데이터를 그룹별로 labeling
print(cdata)
print()

cdata2 = pd.cut(ages,bins,right=False)
print(cdata2)
# print(pd.value_counts(cdata2)) # 각 value 값의 수
print(pd.Series(cdata2).value_counts()) # 각 value 값의 수
print()

rdata = pd.cut(ages,bins,labels=['Youth','YoungAdult','MiddledAged','Senior'])
print(rdata)
print(pd.Series(rdata).value_counts())