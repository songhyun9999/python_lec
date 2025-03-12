import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


plt.rc('font',family='Malgun Gothic')

data = pd.read_csv('covid_data.csv',index_col=0)
chartdata = data.loc[['독일','영국','중국','프랑스','이탈리아'],['4월06일','4월07일']]
chartdata = chartdata.values
# print(chartdata)

COLOR_NUM = 5
cmap = plt.get_cmap('tab20c')
outer_colors = cmap(np.arange(COLOR_NUM)*4)
inner_colors = cmap(np.arange(COLOR_NUM*2))

INNER_VACANT_CIRCLESIZE = 0.3
OUTER_PCTDISTANCE = 0.85
INNER_PCTDISTANCE = 0.75

cum_sum = chartdata.sum(axis=1)
fig,ax = plt.subplots(figsize=(6,6))
ax.pie(cum_sum,radius=1,colors=outer_colors,
       labels=['독일','영국','중국','프랑스','이탈리아'],
       autopct='%.2f%%',
       pctdistance=OUTER_PCTDISTANCE,
       wedgeprops=dict(width=INNER_VACANT_CIRCLESIZE,edgecolor='w'))

ax.pie(chartdata.flatten(),radius=1-INNER_VACANT_CIRCLESIZE,colors=inner_colors,
       wedgeprops=dict(width=INNER_VACANT_CIRCLESIZE,edgecolor='w'),
       autopct='%.2f%%',
       pctdistance=INNER_PCTDISTANCE)
ax.set_title('주요 국가별 중첩 파이 그래프')

plt.show()