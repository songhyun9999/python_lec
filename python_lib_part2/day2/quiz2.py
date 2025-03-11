import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

# covid_frame = pd.read_csv('covid_data.csv',index_col=0)['4월06일']
# # print(covid_frame)
#
# YTICK_INTERVAL = 50000
# maxlim = (int(covid_frame.max() / YTICK_INTERVAL) + 1) * YTICK_INTERVAL
# # print(covid_frame.max(),maxlim)
# values = np.arange(0,maxlim+1,YTICK_INTERVAL)
# # print(values)
# plt.plot(covid_frame,'bo-')
# plt.yticks(values,[format(val,',')for val in values])
# plt.title('4월6일 코로나 발생 건수')
# plt.grid(True)
# plt.xlabel('국가별')
# plt.ylabel('발생 건수')
# plt.show()

covid_frame = pd.read_csv('covid_data.csv',index_col=0)

COUNTRY = ['스페인','프랑스','독일','중국','영국','이란']
chartdata = covid_frame.loc[COUNTRY,'4월06일':'4월10일']
print(chartdata.T)
chartdata.T.plot(title='일자& 국가별 코로나 발생 수',
                 figsize=(10,6),legend=True,marker='o')
plt.grid(True)
plt.show()