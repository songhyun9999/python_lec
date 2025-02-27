import pandas as pd
import numpy as np

myindex = ['김구','이봉창','안중근','윤봉길']
mycolumns = ['강남구','은평구','마포구','용산구']
mylist = list(10* i for i in range(1,17)) # 10 ~ 160
mylist = np.array(mylist).reshape(4,4)

df = pd.DataFrame(mylist,index=myindex,columns=mycolumns)
# print(df)

# ㄱ 1번째 행 데이터를 조회
print(df.iloc[1],'\n')

# ㄴ 1번째와 3번째 행 데이터를 조회
print(df.iloc[[1,3]],'\n')

# ㄷ '윤봉길' 행만 조회
print(df.loc['윤봉길'],'\n')

# ㄹ '이봉창' 과 '윤봉길' 행을 조회
print(df.loc[['윤봉길','이봉창']],'\n')

# ㅁ '윤봉길' 행의 '은평구' 데이터만 조회
print(df.loc[['윤봉길'],['은평구']],'\n')

# ㅂ '김구'와 '이봉창' 의 '용산구'와 '은평구' 데이터 조회
print(df.loc[['김구','이봉창']][['용산구','은평구']],'\n')

# ㅅ '은평구'의 값이 100 이하인 행들을 조회
print(df.loc[df['은평구']<=100],'\n') # loc 필터링 -> 좀더 직관적이고 명확함

# ㅇ '은평구'의 값이 100인 행들을 조회
print(df[df['은평구']==100],'\n') # boolean 인덱싱

# ㅈ '김구'부터 '안중근' 까지 '용산구' 데이터를 80으로 변경
df.loc['김구':'안중근',['용산구']] = 80
# df.loc['김구':'안중근','용산구'] = 80 # 같은 표현이지만 여러 column 지정시 []필요
print(df,'\n')




