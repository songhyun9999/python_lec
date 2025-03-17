import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import isnull
from scipy.stats import alpha

plt.rc('font',family='Malgun Gothic')
# 4. drinks.csv 파일을 이용하여 아래의 조건에 맞게 출력하시오
# (아래 그래프 이미지 참조)
#  ㄱ. 파일을 읽어 데이터 프레임으로 구성한 뒤 앞의 10개 행을 출력
#  ㄴ.'beer_servings', 'spirit_servings', 'wine_servings',
#  'total_litres_of_pure_alcohol'들의 상관계수를 계산하여 출력하고
#      heatmap를 이용하여 이를 그래프로 출력
#  ㄷ. 'beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol'들의 상관 관계를 보기 위해 각 특성들의
#      산점도를 그래프로 출력
#  ㄹ. 'continent'의 결측데이터에는 'OT'를 삽입
#  ㅁ. 대륙별('continent')의 데이터 수의 비율을 파이 그래프를 이용하여 출력
#  ㅂ. 'total_litres_of_pure_alcohol' 전체 평균 보다 많은 알코올을 섭취하는 대륙을 구하여 출력
#  ㅅ. 대륙별 spirit_servings의 평균, 최소, 최대, 합계를 막대 그래프로 출력
#  ㅇ. 대륙별 total_litres_of_pure_alcohol를 막대 그래프로 출력

# 4-ㄱ
print('-----------4.ㄱ-------------')
df = pd.read_csv('drinks.csv')
print(df.head(10))
print()

# 4-ㄴ
import seaborn as sns
print('-----------4.ㄴ-------------')
cor_dic = {'beer_servings':'beer','spirit_servings':'spirit',
           'wine_servings':'wine','total_litres_of_pure_alcohol':'alcohol'}
df.rename(columns=cor_dic,inplace=True)
cor_list = ['beer','spirit','wine','alcohol']
cor = df[cor_list].corr()

sns.heatmap(data=cor,annot=True)
plt.xticks(rotation=0)
plt.yticks(rotation=90)
plt.show()

# 4-ㄷ
print('-----------4.ㄷ-------------')
ndf = df.loc[:,cor_list]
sns.pairplot(data=ndf)
plt.show()
print()

# 4-ㄹ
print('-----------4.ㄹ-------------')
# print(df['continent']== 'NaN')
# df.loc[df['continent'].isnull(),'continent']= 'OT'
df['continent'] = df['continent'].fillna('OT')
print(df.iloc[0:10])
print()

# 4-ㅁ
print('-----------4.ㅁ-------------')
cont_num = df.groupby('continent')['continent'].count()
plt.pie(cont_num,labels=cont_num.index,
        autopct= '%.0f%%',
        shadow=True,explode=[0,0,0,0,0.2,0],startangle=0)

plt.legend(loc='best')
plt.show()

# 4-ㅂ
print('-----------4.ㅂ-------------')
mean_val = df['alcohol'].mean()
# 국가
print(df[df['alcohol']>mean_val]['country'])
# 대륙 평균이 더 큰 경우
tmp = pd.DataFrame(df.groupby('continent')['alcohol'].mean()>mean_val).index

print(tmp[df.groupby('continent')['alcohol'].mean()>mean_val])

# 4-ㅅ
print('-----------4.ㅅ-------------')
mean_val = df.groupby('continent')['spirit'].mean()
min_val = df.groupby('continent')['spirit'].min()
max_val = df.groupby('continent')['spirit'].max()
sum_val = df.groupby('continent')['spirit'].sum()

tmp = pd.DataFrame([mean_val,min_val,max_val,sum_val],
                   index=['Mean','Min','Max','Sum'])
# print(tmp)
tmp.T.plot(kind='bar')
plt.xticks(rotation=0)
plt.show()

# 4-ㅇ
print('-----------4.ㅇ-------------')
tmp2 = df.groupby('continent')[['alcohol']].mean()
mean_val = tmp2.T.mean(axis=1)

print(tmp2)
plt.bar(x=tmp2.index,height=tmp2['alcohol'],alpha=0.3)
plt.bar(x='mean',height=mean_val,alpha=0.3,color='r')

plt.axhline(xmin=0.1,xmax=0.9,y=mean_val['alcohol'],color = 'black',linewidth=1,linestyle='--')
plt.title('total_litres_of_pure_alcohol by Continent')
plt.grid(True)
plt.show()