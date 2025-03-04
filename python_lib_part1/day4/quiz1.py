import pandas as pd

ch ='y'
df = pd.DataFrame(index=['수학','영어','국어'])
while ch=='y':
    name = input('이름을 입력하세요: ')
    score = list(map(int,input('수학 영어 국어 점수를 순서대로 입력하세요: ').split(' ')))
    df[name] = score
    ch = input('계속 진행하시겠습니까?(y/n) ')

print(df)
print()
# print(df.stack().unstack(level=0).stack())
print(df.T.stack())

total_score = df.sum(axis=1)
mean_score = df.mean(axis=1)
df['총점'] = total_score
df['평균'] = mean_score.map(lambda x: round(x,2))
print(df)
