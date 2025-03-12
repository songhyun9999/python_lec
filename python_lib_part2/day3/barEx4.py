import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


plt.rc('font',family = 'Malgun Gothic')

data = pd.read_csv('covid_data.csv',index_col='국가')

america = data.loc[['미국']].T
# print(america)

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,6))

america.plot(kind='bar',ax=axes[0],rot=0,alpha=0.7)
america.plot(kind='barh',ax=axes[1],color='m',alpha=0.7)
fig.suptitle('서브 플로팅',fontsize=16)

plt.show()