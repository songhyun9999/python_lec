import numpy as np

ch = 'y'
scores = []
while ch =='y':
    score = list(map(int,input('국어 영어 수학 점수를 입력하세요 : ').split(' ')))
    scores.append(score)
    ch = input('입력을 계속 진행하시겠습니까?(y/n) ')

print(scores)
print()
scores = np.array(scores)

print(f'국어 점수: {scores[:,0]}')
print(f'영어 점수: {scores[:,1]}')
print(f'수학 점수: {scores[:,2]}')