class Person6:
    def __init__(self):
        print('Person.__init__')
        self.name = 'kim'
        

class Student(Person6):
    def __init__(self):
        # super() 는 부모를 나타냄
        super().__init__() # 파이썬에서 부모의 생성자는 자동 호출 X
        print('Student.__init__')
        self.message = 'hello~~~~~~~'
        
    def print_message(self):
        print(f'{self.name} 이/가 {self.message}라고 말합니다')
        
obj1 = Student()
obj1.print_message()