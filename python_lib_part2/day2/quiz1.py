import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

tip_frame = pd.read_csv('tips.csv',index_col=0)
# print(tip_frame)
fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
ax2 = ax1.twinx()

ax1.plot(tip_frame['total_bill'],'r-')
ax1.tick_params(axis='y',labelcolor='red')

ax1.set_ylabel('결제 금액',c='r')
ax1.set_title('결제 금액과 Tip(이중 축)')

ax2.plot(tip_frame['tip'],'b-')
ax2.set_ylabel('팁(tips)',c='b',rotation=0)
ax2.tick_params(axis='y',labelcolor='blue')

plt.tight_layout()
plt.show()