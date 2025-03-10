import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

frame = pd.read_excel('fine_dust.xlsx',index_col=0)
# print(frame)

plt.figure(figsize=(13,4))
plt.plot(frame[2016],'bs-',label='2016')
plt.plot(frame[2017],'s-',c='orange',label='2017')
plt.plot(frame[2018],'gs-',label='2018')
plt.plot(frame[2019],'rs-',label='2019')
plt.legend(loc=1)
plt.grid(True)
plt.xlabel('area')
plt.ylabel('micrometer')
plt.title('2018 Fine dust line graph')
plt.tight_layout()
# plt.savefig('finedust_plot_quiz.png',dpi=400,bbox_inches='tight')
plt.show()