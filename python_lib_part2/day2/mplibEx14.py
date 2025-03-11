import matplotlib.pyplot as plt
import numpy as np

# 방법 1
# f = plt.figure()
# # ax1 = plt.gca()
# ax1 = f.add_subplot(1,1,1)
# ax2 = ax1.twinx()
#
# ax1.plot([10,5,3,12,7],'r--',label='y1')
# ax1.set_ylabel('y1')
#
# ax2.plot([100,200,220,170,120],'b:',label='y2')
# ax2.set_ylabel('y2')
#
# f.legend(loc=1)

# 방법 2
ax1 = plt.gca()
ax2 = ax1.twinx()

ln1 = ax1.plot([10,5,3,12,7],'r--',label='y1')
ax1.set_ylabel('y1')

ln2 = ax2.plot([100,200,220,170,120],'b:',label='y2')
ax2.set_ylabel('y2')

lns = ln1 + ln2
labels = [l.get_label()for l in lns]
print(labels)

plt.legend(lns,labels,loc='best')
# plt.legend(lns,['y1','y2'],loc='best')

plt.show()