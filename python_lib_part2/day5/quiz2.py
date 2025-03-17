import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 2.unemployment_rate.csv 파일을 이용하여 아래와 그림과
# 같이 선그래프를 그리시오(파일 로딩시 encoding='cp949' 사용)
plt.rc('font',family='Malgun Gothic')
df = pd.read_csv('unemployment_rate.csv',encoding='cp949',index_col=0)
# print(df)
index = df.index
dfT = df.T
dfT[index[range(5)]].plot(marker='o',figsize=(7,4))
plt.xlabel('연령대')
plt.ylabel('연도명')
plt.title('연령대별 연도명 꺾은 선 그래프')
plt.show()