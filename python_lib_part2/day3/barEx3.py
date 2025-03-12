import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


plt.rc('font',family = 'Malgun Gothic')

data = pd.read_csv('covid_data.csv',index_col='국가')
datachart = data.loc[['프랑스','중국','영국','이란'],'4월06일':'4월08일']
# print(datachart)

def make_bar2(chartdata,rotation,title,ylim=None,stacked=False,ytick_interval=10000):
    # plt.figure(figsize=(8,6))
    chartdata.plot(kind='bar',rot=rotation,legend=True,stacked=stacked)

    if stacked is False:
        maxlim = (int(max(chartdata.max())/ytick_interval)+1)*ytick_interval
    else:
        maxlim = (int(chartdata.sum(axis=1)/ytick_interval)+1)*ytick_interval

    values = np.arange(0,maxlim+1,ytick_interval)
    plt.yticks(values,[format(val,',')for val in values])

    if ylim is not None:
        plt.ylim(ylim)
    plt.show()


make_bar2(datachart,rotation=0,title='국가별 일별 발생 수')
