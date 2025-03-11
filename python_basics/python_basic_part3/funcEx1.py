def add(n1,n2):
    return n1+n2

print(add(10,20))
print()

ndata = [100,300]
print(add(ndata[0],ndata[1]))
print(add(*ndata))
print()

# 가변인자 활용하면 여러 인자를 받을 수 있음
# 가변인자는 일반적으로 하나만 사용가능
# 언패킹되게 인자를 전달 받는다는 의미 -> data는 패킹된 상태 (tuple)
def add2(*data): 
    total = 0
    for d in data:
        total += d
    return total

print(add2(10,20,30))
print(add2(10,20,30,40))

print(add2(*ndata))
