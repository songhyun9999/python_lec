import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

plt.rc('font',family='Malgun Gothic')

df = pd.read_csv('medical.csv')
df.info()
# print(df.head(5))

# print(df.describe())
df = df[df.Age >= 0]
# print(df.describe())
# print(df['No-show'].unique())
df['No-show'] = df['No-show'].map({'Yes':1,'No':0})
# print(df.head(5))
# print(df['No-show'].value_counts())

# print(df[['ScheduledDay','AppointmentDay']])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
# df.info()
# print(df[['ScheduledDay','AppointmentDay']])

df['waiting_day'] = df['AppointmentDay'].dt.dayofyear - df['ScheduledDay'].dt.dayofyear
# print(df.describe()['waiting_day'])
df = df[df.waiting_day>=0]

df = df[df.Age<=105]

import seaborn as sns
# plt.figure(figsize=(14,2))
# sns.boxplot(x=df.Age)
# plt.show()

wtotal = df[df.waiting_day==0]['waiting_day'].value_counts()
ntotal = df[(df.waiting_day==0) & (df['No-show']==1)]['waiting_day'].value_counts()

# print(ntotal, wtotal)
# print(ntotal/wtotal)

no_show = df[df['No-show']==1]
show = df[df['No-show']==0]

# plt.hist(no_show[no_show['waiting_day']<=10]['waiting_day'],
#          bins=10,label='no_show',rwidth=0.9,alpha=0.7)
# plt.hist(show[show['waiting_day']<=10]['waiting_day'],
#          bins=10,label='show',rwidth=0.9,alpha=0.3)
# plt.legend(loc='best')
# plt.show()

# no_show['ScheduledDay'].hist(alpha=0.7,label='no-show')
# show['ScheduledDay'].hist(alpha=0.7,label='show')
# plt.legend(loc='best')
# plt.show()

# sns.barplot(data=df,x='SMS_received',y='waiting_day',hue='No-show')
# plt.show()

# sns.countplot(x='Gender',hue='No-show',data=df)
# plt.show()

woman_noshow = df[(df['Gender']=='F') & (df['No-show']==1)]['Gender'].value_counts()
man_noshow = df[(df['Gender']=='M') & (df['No-show']==1)]['Gender'].value_counts()
woman_total = df[df['Gender']=='F']['Gender'].value_counts()
man_total = df[df['Gender']=='M']['Gender'].value_counts()

print(f'노쇼 여성 비율: {woman_noshow/woman_total}')
print(f'노쇼 남성 비율: {man_noshow/man_total}')
