import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 와인 품질 데이터셋을 이용한다.
#  a. 데이터 셋을 DataFrame으로 읽어온다.
#  b. 위의 데이터프레임의 요약 통계를 표시한다.(최소, 최대, 사분위, 평균, 분산)
#  c. 와인 품질(quality)의 유일 값을 찾아 출력한다.
#  d. 와인 품질(quality)의 빈도를 계산하여 출력한다.
#  e. 와인 종류에 따라 기술 통계(최소, 최대, 사분위, 평균, 분산)를 출력한다.
#  f.  와인 종류에 따른 품질(quality)의 분포를 확인하기 위해 레드와인과 화이트 와인의 막대 그래프를 출력한다.
#     (이때 범례도 같이 출력한다. )
#  g. 와인 종류에 따라 품질의 차이를 검정(분산, 평균)하여 각 각을 출력한다.

# 1-a
df = pd.read_csv('winequality-both.csv')
# df.info()
# print(df.head())

# 1-b
print('--------1-b----------')
print(df.describe())
print()

# 1-c
print('--------1-c----------')
print(df['quality'].unique())
print()

# 1-d
print('--------1-d----------')
print(df['quality'].value_counts())
print()

# 1-e
print('--------1-e----------')
print(df.groupby('type').describe())
print()

# 1-f
print('--------1-f----------')
by_quality = df.groupby(['quality','type']).size().unstack()
print(by_quality)
by_quality.plot(kind='bar')
plt.show()

# import seaborn
# seaborn.histplot(data=df,x='quality',hue='type')
# plt.show()
# print()

# 1-g
print('--------1-g----------')
varience = df.groupby('type')['quality'].var()
mean = df.groupby('type')['quality'].mean()
print(f'분산\n{varience}')
print(f'평균\n{mean}')
print()