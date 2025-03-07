class Person:
    def __init__(self):
        print('Person.__init__call')
        self.hello = 'hihihi'


class Student(Person):
    def __init__(self):
        print('Student.__init__call')
        super().__init__() # 호출 시점을 지정할 수 있음
        self.school = '학교'


james = Student()
print(james.school)
print(james.hello)