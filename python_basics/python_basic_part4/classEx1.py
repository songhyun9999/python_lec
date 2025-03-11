class Person:
    def greeting(self):
        print('Hello')

# 힙영역에 객체의 정보를 저장
# 정보에는 variable, function 을 포함한 해당 클래스 객체의 정보들        
obj = Person()
obj.greeting()

# 저장된 객체는 각자의 영역에 저장된 함수를 호출하도록 함
obj2 = Person()
obj2.greeting()

print(type(obj))
print()

# 파이썬은 대부분은 함수와 자료구조가 객체화 되어 있음
n1 = 10 # n1 = int(10)
print(type(n1)) # class int
ldata = [10,20,30] # ldata = list([10,20,30])
print(type(ldata)) # class list

def hf():
    print('hello')
print(type(hf)) # class function
print(type())

