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
    
print(ans)

