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

