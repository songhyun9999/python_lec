ch = ''
ans = dict()
while True:
    name = input('이름을 입력하세요:')
    score = list(map(int,input('영어 수학 국어 점수를 넣어주세요:').split(' ')))
    
    ans[name] = score
    ch = input('계속 진행하시겠습니까?(y/n)')
    if ch =='y':
        continue
    else:
        break
    
keys = ans.keys()
for i in keys:
    eng ,math ,kor = ans[i]
    total_score = eng + math + kor
    print(''.join([f'이름 : {i:^4} 영어: {eng:>4}',
          f' 수학: {math:>4} 국어 : {kor:>4}',
          f' 총점: {total_score:>4}',
          f' 평균: {(total_score/3):<5.2f}']))
    
    
    

