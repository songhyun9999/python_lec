import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font',family='Malgun Gothic')

welfare = pd.read_csv('welfare_python.csv',encoding='utf-8')
welfare.info()
# print(welfare.head(5))

welfare['gender']=['남성' if g == 1 else '여성' for g in welfare['gender']]
# print(welfare.head(10))

year = 2000
welfare['age'] = year - welfare['birth']
print(welfare.head())

welfare['marriage'] = welfare['marriage'].map(
    lambda x: '결혼' if x == 1 else '이혼' if x==3 else '무응답')
# print(welfare.head(10))

welfare.loc[welfare['income'].isnull(),['income']] = welfare['income'].mean()
# print(welfare.head(10))
print()

jobFrame = pd.read_csv('welfare_job.csv',encoding = 'cp949')
# jobFrame.info()
print(jobFrame.head(10))

welfare = pd.merge(welfare,jobFrame,on='code_job')
print(welfare.head(10))

welfare['religion'] = welfare['religion'].map(
    lambda x: '있음' if x == 1 else '없음')
# print(welfare.iloc[4])

def setCR(x):
    if int(x) == 1:
        return '서울'
    elif int(x) == 2:
        return '수도권'
    elif int(x) == 3:
        return '부산/경남/울산'
    elif int(x) == 4:
        return '대구/경북'
    elif int(x) == 5:
        return '대전/충남'
    elif int(x) == 6:
        return '강원도/충북'
    elif int(x) == 7:
        return '광주/전남/전북/제주도'


welfare['code_religion'] = welfare['code_religion'].map(setCR)
print(welfare.iloc[4])

welfare['ageg'] = welfare['age'].map(
    lambda x: '청년' if x < 30 else '중년' if x<60 else '노년')
print(welfare.iloc[4])

exchange = {'gender':'성별','birth':'생일','marriage':'결혼유무',
            'religion':'종교유무','code_job':'직업코드','income':'소득',
            'code_religion':'지역코드','age':'나이','job':'직업',
            'ageg':'연령대'}

welfare.rename(columns=exchange,inplace=True)
print(welfare.head(10))

welfare.to_csv('welfareClean.csv',index=False,encoding='cp949')

