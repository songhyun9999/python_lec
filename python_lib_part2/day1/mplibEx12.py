import matplotlib.pyplot as plt
import numpy as np

np.random.seed(777)
plot_data1 = np.random.randn(50).cumsum()
plot_data2 = np.random.randn(50).cumsum()
plot_data3 = np.random.randn(50).cumsum()
plot_data4 = np.random.randn(50).cumsum()

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(plot_data1,'bo-',label='Blue Solid')
ax1.plot(plot_data2,'r*--',label='Red Dashed')
ax1.plot(plot_data3,'g*-.',label='Green Dash Dot')
ax1.plot(plot_data4,c='orange',ls=':',marker='s',
         label='orange Dotted')

ax1.xaxis.set_ticks_position('top')
ax1.yaxis.set_ticks_position('right')

ax1.set_title('Line Plots: Markers, Colors, and LineStyles',fontsize=16)
plt.xlabel('Draw')
plt.ylabel('Random Number')
plt.legend(loc=1)

# 생성된 figure 저장
plt.savefig('line_plot_quiz.png',dpi=400,bbox_inches='tight')
plt.show()