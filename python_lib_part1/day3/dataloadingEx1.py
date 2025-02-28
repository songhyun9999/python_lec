import pandas as pd

frame1 = pd.read_csv('data/ex1.csv')
print(frame1) # csv의 첫줄은 해당 DataFrame의 column 값으로 설정
print(type(frame1)) # csv 파일은 DataFrame 으로 읽어옴
print()

# 데이터의 첫줄을 column으로 지정 안함
# 첫번째 : header = None
frame2 = pd.read_csv('data/ex2.csv',header=None)
print(frame2)
print()

# 두번째 : 직접 이름 설정하여 column 값 지정
frame3 = pd.read_csv('data/ex2.csv',
                     names=['one','two','three','four','msg'])
print(frame3)
print()

# index로 사용할 데이터 직접 지정
frame3 = pd.read_csv('data/ex2.csv',
                     names=['one','two','three','four','msg'],
                     index_col=['msg'])
print(frame3)
print()

# 첫번째 column의 데이터를 index로 사용
frame3 = pd.read_csv('data/ex2.csv',
                     names=['one','two','three','four','msg'],
                     index_col=0)
print(frame3)
print()

# 주석처럼 필요없는 데이터를 처리하기 위해
# 생략할 행을 지정함
frame4 = pd.read_csv('data/ex4.csv',skiprows=[0,2,3])
print(frame4)
