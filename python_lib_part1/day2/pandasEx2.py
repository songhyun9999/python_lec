import pandas as pd
import numpy as np

np.random.seed(12345)

frame1 = pd.DataFrame([[10,20,30],[50,60,70]])
print(frame1)
print()

frame2 = pd.DataFrame([[10,20,30],[50,60,70]],index=['one','two'],
                      columns=['first','second','third'])
print(frame2)
print()
print(frame2.index) # index 객체
print(frame2.columns) # index 객체
# ndarray 는 동일한 데이터타입으로 변경하므로
# 다른 데이터 타입이 섞이면 object 객체로 변경 되는등 벡터 연산이 안될 수 있음
# values를 호출할때는 객체의 값의 데이터 타입에 주의해야함
print(frame2.values)
print()

ldata = [('김가',180,80),('이가',160,60),('최가',170,70),('오가',165,90)]
frame3 = pd.DataFrame(ldata,columns=['이름','키','몸무게'],
                      index=[11,12,21,22])
print(frame3)
print()

data = {'state':['ohio','ohio','nevada','nevada'],
        'year':[2020,2021,2020,2021],
        'pop':[1.5,1.7,3.6,2.4]}
frame4 = pd.DataFrame(data) # 딕셔너리는 key값을 column 으로 지정
print(frame4)
print()

frame5 = pd.DataFrame(data,columns=['year','pop','info']) # 없는 key는 NAN으로 가져옴
print(frame5)
print()
# 지정한 순서대로 데이터 읽어옴
frame6 = pd.DataFrame(data,columns=['year','pop','state'] 
                      ,index=['one','two','three','four'])
print(frame6)
print()

print(frame6['state'])
print(type(frame6['state']))
print()
print(frame6.state)
print()
print(frame6.loc['two']) # index로 데이터를 가져오기
# 보통 다른 시리즈객체의 데이터기 때문에
# 다른 데이터타입이므로 object type의 시리즈객체를 만듬
print(type(frame6.loc['two']))
print()
print(frame6['pop']['two'])
print(type(frame6.loc['two']['pop']))
print()
print(frame6.year.two)
print(frame6.loc['two'].year)
print()

##### 열 추가 ########
# 추가할 때 index 맞춰야함
# frame6['area'] = pd.Series([32.323,32.323,562.43,562.43],
#                            #index=['one','two','three','four']
#                            index=frame6.index)

frame6['area'] = pd.Series([32.323,32.323],index=['one','three'])
print(frame6)
print()

##### 행 추가 #########
frame6.loc['five'] = pd.Series([2020,3.3,'utah',651.326]
                               ,index=frame6.columns)
print(frame6)
print()

frame6.index.name = 'id'
frame6.columns.name = 'info'
print(frame6)

