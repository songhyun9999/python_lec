'''
클래스 내부에서 전역으로 선언된 변수는 
클래스에 할당된 메모리영역에 저장되어 (각 객체의 힙영역 X)
모든 클래스 객체에서 공유됨
'''
class Person3:
    bag = []
    
    def put_bag(self,stuff):
        self.bag.append(stuff)
    
    def print_bag(self):
        print(self.bag)

# bag는 클래스 메모리 영역에 생성되었으므로 객체없이 접근 가능
Person3.bag.append('remover')
print(Person3.bag)

# 모든 객체에서 bag가 공유되는것을 확인        
obj = Person3()
obj.put_bag('Book')
obj.print_bag() # remover book

obj2 = Person3()
obj2.put_bag('key')
obj2.print_bag() # remover book key
obj.print_bag()  # remover book key
