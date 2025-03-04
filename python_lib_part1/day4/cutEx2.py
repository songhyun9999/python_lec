import pandas as pd

scores = pd.Series([70,88,92,54,34,76,59,91,83,78,61,55],
                   index=['홍길동','이순신','임꺽졍','정난정','이이','이황',
                          '정도전','이성계','김유신','김철수','정약용','정약전'])

print(scores)
print()
bins = [0,60,70,80,90,101]

answer = pd.cut(scores,bins,labels=['F','D','C','B','A'],right=False)
counts = answer.value_counts(sort=False)[::-1]

print(pd.concat([answer,counts],axis=0))
print()

print(pd.concat([scores,answer],axis=1,keys=['점수','학점']))