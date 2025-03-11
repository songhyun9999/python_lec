it1 = iter(range(4))
print(it1)
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

ld = [100,600,400,200]
it2 = iter(ld)
print(it2.__next__())
print(it2.__next__())
print(it2.__next__())
print(it2.__next__())
print(next(it2,0)) # 더이상 가져올게 없을 때 가져올 default값 지정


