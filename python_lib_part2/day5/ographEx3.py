import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


plt.rc('font',family = 'Malgun Gothic')

import squarify

# sizes = [50,20,17,11]
# squarify.plot(sizes)
# plt.show()

# labels = ['서울', '대구', '인천', '부산']
# colors = ['lightgreen', 'cornflowerblue', 'lightcoral', 'mediumpurple']
# squarify.plot(sizes,10,10,label=labels,color=colors,
#               bar_kwargs=dict(edgecolor='w',linewidth=3))
# plt.axis('off')
# plt.show()

welfare = pd.read_csv('welfareClean.csv',encoding='cp949')
welfare.info()
df = welfare.groupby('지역코드').size().reset_index(name='counts')
print(df)
print()
labels = df.apply(lambda x :f'{x.iloc[0]}\n{x.iloc[1]}',axis=1)
# print(labels)
sizes = df['counts'].values.tolist()
colors = [plt.cm.Spectral(i/float(len(labels)))for i in range(len(labels))]
plt.figure(figsize=(10,6))
squarify.plot(sizes=sizes, label=labels,alpha=0.8,
              bar_kwargs=dict(linewidth=3, edgecolor='w'))
plt.title('Tree map(지역구)',fontsize=20)
plt.axis('off')
plt.show()