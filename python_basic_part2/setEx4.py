# 1~100 의 숫자 중 3과 5의 공배수를 출력
x = {i*3 if i*3 <= 100 else 0 for i in range(50)}
y = {i*5 if i*5 <= 100 else 0 for i in range(50)}
x.discard(0)
y.discard(0)

ans = x.intersection(y)
ans = list(ans)
ans.sort()

print(ans)