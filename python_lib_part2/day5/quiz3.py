import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 3.final_exam.csv 파일을 이용하여 아래와 같이 막대그래프를 그리시오
# (파일 로딩시 encodingf='cp949' 사용)
plt.rc('font',family='Malgun Gothic')
df = pd.read_csv('final_exam.csv',encoding='cp949',index_col=0)
# print(df)
colors = ['b','g','r','c','m']

plt.bar(x=df.index,height=df['korean'],color=colors)
plt.title('국어 점수',fontsize=14)
plt.xlabel('학생 이름')
plt.ylabel('점수')

for idx in range(len(df.korean)):
    text = f"{df['korean'].iloc[idx]}점"
    plt.text(x=idx, y=df['korean'].iloc[idx]+1,
             s=text, ha='center', fontsize=8)

mean_val = df['korean'].mean(axis=0)
meantext = f'평균: {int(mean_val)}점'
plt.axhline(y=mean_val,color = 'r',linewidth=1,linestyle='--')
plt.text(x=0,y=mean_val+1,
         s=meantext,ha='center',fontsize=11)
plt.show()