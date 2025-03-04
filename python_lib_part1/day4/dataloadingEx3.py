import numpy as np
import pandas as pd

df = pd.read_excel('data/monthly_sales.xlsx',header=1,index_col=0)
print(df)
print()

df2 = pd.read_excel('data/class_info.xlsx',sheet_name='2학년')
print(df2)
print()

df2 = pd.read_excel('data/class_info.xlsx',sheet_name=0)
print(df2)
print()

# sheet를 전부 dictionary type으로 가져옴, key값은 해당 sheet 의 이름
data = pd.read_excel('data/class_info.xlsx',sheet_name=None)
print(data)
print(type(data))
print()

# sheet name 지정해서 가져오기
data2 = pd.read_excel('data/class_info.xlsx',sheet_name=['1학년','2학년'])
print(data2)
print()

frame3 = pd.DataFrame(np.random.randn(100,4),
                      columns=['seoul','busan','incheon','suwon'])
frame3.to_csv('sfile.csv')
frame3.to_csv('sfile2.csv',index=False) # 인덱스를 저장X

