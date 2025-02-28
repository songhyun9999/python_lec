import pandas as pd
import numpy as np
# 많은 양의 데이터를 나누어 처리
# chunker = pd.read_csv('data/ex6.csv',chunksize=1000)
# print(chunker) # TextFileReader 객체 -> iteraotr 객체임
# print()
#
# for piece in chunker:
#     print(piece,end='\n\n')

sdata1 = pd.Series(['a','b','a','c','d','a','c'])
print(sdata1)
print()
# series 내의 value 값의 개수를 가져와
# value 값을 index로, 개수를 value 로 만들어 series 객체를 반환함
print(sdata1.value_counts())

chunker = pd.read_csv('data/ex6.csv',chunksize=1000)
print(chunker) # TextFileReader 객체 -> iteraotr 객체임
print()

total = pd.Series([],dtype=np.float64)

for piece in chunker:
    total = total.add(piece['key'].value_counts(),fill_value=0)
print(total.sort_values(axis=0,ascending=False)[:10])