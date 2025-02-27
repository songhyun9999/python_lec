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

kor,eng,math = scores.sum(axis=0)
print(f'국어 총점:{kor}, 영어 총점:{eng}, 수학 총점:{math}')
print()

name = input('출력할 학생의 이름을 입력하세요 : ')
score = scores[names==name,:].flatten()

print(f'{name} 과목 점수 : {score}, 평균 : {np.average(score):.2f}, '
      f'표준편차 : {np.std(score):.2f}, 분산 : {np.var(score):.2f}')
print()
print(f'수학 점수로 정렬 후\n{scores[scores[:,2].argsort()]}')

