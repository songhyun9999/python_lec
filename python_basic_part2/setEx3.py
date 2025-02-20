# 집합 연산 후 저장
sdata = {1,2,3,4}
sdata.update({5,6})
print(sdata)
sdata |= {5,6,7}
print(sdata)

# 원소 삽입
sdata.add(10)
print(sdata)

# 원소 삭제
sdata.remove(3)
print(sdata)

sdata.discard(5)
print(sdata)

# discard : 없는 원소를 삭제할 때 에러X
# remove  : 없는 원소를 삭제할 때 에러O
sdata.discard(1000) 
# sdata.remove(1000)
print()

# 1~100 의 숫자 중 3과 5의 공배수를 출력
x = {i*3 if i*3 <= 100 else 0 for i in range(50)}
y = {i*5 if i*5 <= 100 else 0 for i in range(50)}
x.discard(0)
y.discard(0)

ans = x.intersection(y)
ans = list(ans)
ans.sort()

print(ans)

