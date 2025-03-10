import matplotlib.pyplot as plt
import numpy as np

# plt.plot([10,20,30,40],[4,2,9,12],color='orange',
#          lw=5,ls='--',marker='o',ms=12,mec='green',mew=5,mfc='red')
# plt.show()
#
# plt.plot([10,20,30,40],[4,2,9,12],color='orange',
#          lw=5,ls='-.',marker='^',ms=5,mec='blue',mew=2,mfc='red')
# plt.show()

# x = range(5)
# y = [2,5,7,8,1]
# plt.plot(x,y,'o-')
#
# x2 = [2]
# y2 = [7]
# plt.plot(x2,y2,'rs')
#
# plt.show()

plt.plot([10,20,30,40],[4,2,9,12],color='k',lw=5,ls='--',
         marker='^',ms=12,mec='blue',mew=2,mfc='red')
plt.xlim(0,50)
plt.ylim(-10,30)
plt.show()
