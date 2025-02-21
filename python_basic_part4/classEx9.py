class Person5:
    def greeting(self):
        print('hello~~')
        
class Student(Person5):
    def study(self):
        print('studing')
        
james = Student()
james.study()
james.greeting()
