ldata = [10,20,30]
ldata.insert(1,[500,600])
print(ldata) # 출력 : [1,[500,600],20,30]

####################################
'''
list에 여러 원소를 특정 index에 한번에 삽입할 수 있다는 장점이 있음
list를 확장시킬 수 있음 (insert는 원소 하나를 추가하게 됨)
'''
ldata[1:1] = [1000,2000] 
print(ldata) # 출력 : [10,1000,2000,....,30]
print()
#############################

ldata.remove(20)
print(ldata)

del ldata[2]
print(ldata)

data = ldata.pop()
print(data)
print(ldata)
print()

data = ldata.pop(1)
print(data)
print(ldata)
print()

ldata3 = ['lim','kim','lee','lim']
print(ldata3)
ldata3.remove('lim') # remove는 가장 작은 index의 해당 값 하나를 삭제함
print(ldata3)
print()

# 전부 지우기
# 아래 방식으로 하거나 
# 찾는 원소의 수를 구해 해당 수만큼 반복문을 통해 remove
ldata3.insert(0,'lim')
count = 0
for i in range(len(ldata3)):
    if ldata3[i] == 'lim':
        ldata3.remove('lim')
        ldata3.append(0)
        count += 1
ldata3 = ldata3[:-count]
print(ldata3)