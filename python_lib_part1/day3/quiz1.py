import pandas as pd
import numpy as np

data = {
    '번호':[1,2,3,4,5,1,2,3,4,5],
    '반':['A','A','A','A','A','B','B','B','B','B'],
    '영어':[100,90,100,80,70,90,100,70,80,90],
    '국어':[90,80,90,70,100,80,90,100,70,80],
    '수학':[80,100,80,90,80,100,70,80,90,100]
}

df = pd.DataFrame(data)
print(df)
print()

df_fixed = df.drop(columns=['번호','반'])
# avg = (df_fixed['영어']+df_fixed['국어']+df_fixed['수학'])/3
avg = df_fixed.mean(axis=1)
df_fixed['평균'] = avg
print(df_fixed)
print()

# eng = np.average(df_fixed['영어'])
# kor = np.average(df_fixed['국어'])
# math = np.average(df_fixed['수학'])
# total_avg = (eng+kor+math) / 3
# df_fixed.loc['평균'] = list((eng,kor,math,total_avg))

df_fixed.loc['평균'] = df_fixed.mean(axis=0)
print(df_fixed)
print()
