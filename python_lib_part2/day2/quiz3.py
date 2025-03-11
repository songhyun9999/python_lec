import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


plt.rc('font',family='Malgun Gothic')
kbo = pd.read_csv('kbo.csv',encoding='cp949',index_col=0)
print(kbo)

xdata,ydata = kbo['AVG'],kbo['HR']

plt.figure(figsize=(8,4))
# plt.scatter(xdata,ydata,color='b',marker='o')
plt.plot(xdata,ydata,marker='o',linestyle='None')
plt.title('산점도 그래프')
plt.xlabel('타율')
plt.ylabel('홈런')
plt.grid(True,color='w',lw=1)
plt.gca().patch.set_facecolor('0.9')
plt.show()
