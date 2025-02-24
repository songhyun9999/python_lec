# generator 는 iterator 를 더 편하게 사용할 수 있게 해줌
def num_generator():
    yield 0 # yield 는 generator 를 생성할 때 사용 
    yield 1
    yield 2
    
for i in num_generator():
    print(i)
print()

g = num_generator()
print(g)
# print(g()) # generator 는 직접 호출이 불가능
print(next(g))
print(next(g))
print(next(g))
print(next(g))

