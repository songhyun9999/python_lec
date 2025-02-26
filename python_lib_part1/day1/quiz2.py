import numpy as np

ch = 'y'
scores = []
names = []
while ch =='y':
    names.append(input('이름을 입력하세요 : '))
    score = list(map(int,input('국어 영어 수학 점수를 입력하세요 : ').split(' ')))
    scores.append(score)
    ch = input('입력을 계속 진행하시겠습니까?(y/n) ')

print(scores)
print()
scores = np.array(scores)
names = np.array(names)
print(scores)
print()

name = input('출력할 학생의 이름을 입력하세요 : ')
print(scores[names==name,:])
