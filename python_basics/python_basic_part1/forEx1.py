# 전부 같은 동작을 하는 반복문
for i in range(0,5,1):
    print(i,end=' ')
print()

for i in range(0,5):
    print(i,end=' ')
print()

for i in range(5):
    print(i,end=' ')
print()

# iterator 객체 만들어서 사용
a = [1,2,3,4,5,6]
b = iter(a)
print(b)

for j in b:
    print(j,end=' ')
print()
print()
