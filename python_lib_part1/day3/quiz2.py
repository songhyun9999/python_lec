import pandas as pd
import numpy as np

df = pd.read_csv('data/quiz_data.csv',
                 index_col='name')
print(df)
print()
max_score = df.max()
min_score = df.min()
total_score = df.sum()
avg_score = df.mean()

answer = pd.DataFrame([max_score,min_score,total_score,avg_score],
                      index = ['최고값','최소값','총합','평균'])
answer = answer.map(lambda x:f'{x:.1f}')
print(answer)