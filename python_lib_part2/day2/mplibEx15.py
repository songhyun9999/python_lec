import matplotlib.pyplot as plt
import pandas as pd

# df = pd.DataFrame({'day1':[7,1,5,6,3,9,5,8],
#                    'day2':[1,2,8,4,6,5,3,1]})
# plt.plot(df)
# lg = plt.legend(['day1','day2'],loc=1,title='t_legend',title_fontsize=12)
# lg._legend_box.sep = 20
# plt.show()

# plt.plot([2,3,5,9],label='values')
# plt.legend(loc=(0,0))
# plt.legend(loc=(0,1))
# plt.legend(loc=(1,0))
# plt.legend(loc=(1,1))
# plt.legend(loc=(0.2,0.5))
# plt.show()

plt.plot([2,3,1,3],label='value1')
plt.plot([8,6,5,8],label='value2')
plt.plot([5,1,2,7],label='value3')
plt.plot([4,9,3,1],label='value4')
plt.legend(loc=2,ncol=2)
plt.show()
