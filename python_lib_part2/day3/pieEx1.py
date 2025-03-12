import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


plt.rc('font',family='Malgun Gothic')
# data = [5,25,50,20]
# plt.pie(data)
# plt.show()

data = pd.read_csv('covid_data.csv',index_col=0)
chartdata = data.loc[['독일','영국','중국','프랑스'],'4월06일']
mylabel = chartdata.index
# mycolor = ['blue','#61ff00','yellow','#ff113c']
#
# plt.figure(figsize=(5,5))
# plt.pie(chartdata, labels=mylabel, startangle=90,
#         colors=mycolor,
#         autopct='%.2f%%',
#         counterclock=False,
#         explode=(0,0.1,0,0),
#         shadow=True) # 2차원 데이터 사용불가
#
# plt.legend(loc='best')
# plt.xlabel('국가명')
# plt.title('주요 국가 코로나 발생 비율(4월6일)')

fig,axes = plt.subplots(figsize=(8,4))

def getLabelFormat(pct, values):
    absolute = int(pct/100 * np.sum(values))
    return f'{pct:.2f}%\n{absolute}명'

wedges,text,autoexts = axes.pie(chartdata,
         autopct = lambda pct:getLabelFormat(pct,chartdata),
         textprops=dict(color='grey'),
         labels=mylabel)

plt.setp(autoexts,size=10,weight='bold')
plt.legend(title='국가명',loc='best')

plt.show()