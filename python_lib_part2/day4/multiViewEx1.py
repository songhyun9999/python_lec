import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import xticks

plt.rc('font',family='Malgun Gothic')

mpg = pd.read_csv('mpg.csv')
fig = plt.figure(figsize=(10,7))
grid = plt.GridSpec(4,4,hspace=0.7,wspace=0.4)
ax_main = fig.add_subplot(grid[:-1,:-1])
ax_right = fig.add_subplot(grid[:-1,-1],xticklabels=[],yticklabels=[])
ax_bottom = fig.add_subplot(grid[-1,:-1],xticklabels=[],yticklabels=[])


ax_main.scatter('displ','hwy',data=mpg,edgecolor='k')

ax_bottom.hist(mpg.displ,bins=40,color='orange')
ax_bottom.invert_yaxis()

ax_right.hist(mpg.hwy,bins=40,color='darkblue',orientation='horizontal')
ax_main.yaxis.tick_right()
ax_main.yaxis.set_label_position('right')
ax_main.set_xlabel('엔진의 크기')
ax_main.set_ylabel('마일 수',rotation=0)
ax_main.set_title('grid spec',fontsize=16)

plt.show()