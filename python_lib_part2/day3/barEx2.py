import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def make_bar(x,y,color,xlabel,ylabel,title):
    plt.bar(x,y,color=color,alpha=0.7)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title,fontsize=14)

    YTHICK_INTERVAL = 50000

    maxlim = (int(y.max()/YTHICK_INTERVAL)+1)*YTHICK_INTERVAL
    values = np.arange(0,maxlim+1,YTHICK_INTERVAL)
    plt.yticks(values,[format(value,',')for value in values])

    ratio = 100*y / y.sum()

    for idx in range(y.size):
        value = format(y.iloc[idx],',') + '건'
        ratioval = f'{ratio.iloc[idx]:.1f}%'
        plt.text(x=idx,y=y.iloc[idx]+2000,s=value,ha='center',fontsize=9)
        plt.text(x=idx,y=y.iloc[idx]/2,s=ratioval,ha='center',fontsize=9)

    mean_val = y.mean()
    meantext = f'평균:{mean_val}건'
    plt.axhline(y=mean_val,color = 'r',linewidth=1,linestyle='--')
    plt.text(x=y.size-1,y=mean_val+3000,
             s=meantext,ha='center',fontsize=11)

plt.rc('font',family='Malgun Gothic')
covid_frame = pd.read_csv('covid_data.csv',index_col=0)
# print(covid_frame)
covid_46 = covid_frame['4월06일']
color_list = ['b','g','r','c','m','y','k']
make_bar(covid_46.index,covid_46,color_list,'국가별','발생건수',
         '국가별 코로나 발생 건수')
plt.show()
