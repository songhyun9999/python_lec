import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


plt.rc('font',family='Malgun Gothic')

data = pd.read_csv('covid_data.csv',index_col=0)

COUNTRY = ['독일','프랑스','중국','영국']
when = ['4월06일','4월07일','4월08일']
data = data.loc[COUNTRY]
filtered_data = data[when]

pieData = filtered_data.sum(axis=1)
barData = filtered_data.loc['독일'].values
barData = barData / sum(barData)
# print(barData)

fig = plt.figure(figsize=(9,5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.pie(pieData,autopct='%1.1f%%',startangle=90,labels=COUNTRY,
        explode=[0.05,0,0,0],counterclock=False)

xpos = 0
bottom = 0
width = 0.2
colors = ['r','g','b']

for j in range(len(barData)):
    height = barData[j]
    ax2.bar(xpos,height,width,bottom=bottom,color=colors[j])
    ypos = bottom + ax2.patches[j].get_height()/2
    ax2.text(xpos,ypos,f'{ax2.patches[j].get_height()*100:.2f}',
             ha='center',fontsize=10,color='w')
    bottom += height

ax2.set_title(f'{COUNTRY[0]}의 일자별 비율')
ax2.legend(when,loc='best')
ax2.set_xlim(-2.5*width,2.5*width)
ax2.axis('off')

# print(ax1.patches[0])
theta1,theta2 = ax1.patches[0].theta1,ax1.patches[0].theta2
center,r = ax1.patches[0].center, ax1.patches[0].r
bar_height = sum([item.get_height() for item in ax2.patches])

x = r * np.cos(np.pi/180 * theta2) + center[0]
y = r * np.sin(np.pi/180 * theta2) + center[1]
print(x,y)

from matplotlib.patches import ConnectionPatch

conn = ConnectionPatch(xyA=(-0.1,bar_height-0.005),coordsA=ax2.transData,
                       xyB=(x,y),coordsB=ax1.transData)
conn.set_color((0.3, 0.3, 0.3))
conn.set_linewidth(1)
ax2.add_artist(conn)

x2 = r * np.cos(np.pi/180 * theta1) + center[0]
y2 = r * np.sin(np.pi/180 * theta1) + center[0]
print(x2,y2)

conn2 = ConnectionPatch(xyA=(-0.1,0.005),coordsA=ax2.transData,
                        xyB=(x2,y2),coordsB=ax1.transData)
conn2.set_color((0.1,0.1,0.1))
conn2.set_linewidth(1.5)
ax2.add_artist(conn2)

plt.show()