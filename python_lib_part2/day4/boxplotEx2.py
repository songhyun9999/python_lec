import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

frame = pd.read_csv('tips.csv',index_col=0)
# print(frame.head())

frame1 = frame.loc[frame['time']=='Dinner','total_bill']
frame1.index.name = 'Dinner'
frame2 = frame.loc[frame['time']=='Lunch','total_bill']
frame2.index.name = 'Lunch'

chartdata = [np.array(frame1),np.array(frame2)]
tick_label = ['Dinner','Lumch']

fig,(ax1,ax2) = plt.subplots(1,2,figsize=(9,4))
ax1.boxplot(chartdata,labels = tick_label,vert=True)
ax1.set_title('vertical boxplot(tip)')
ax2.boxplot(chartdata,labels=tick_label,vert=False)
ax2.set_title('horizontal boxplot(tip)')
plt.show()
