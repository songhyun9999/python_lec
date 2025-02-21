class Person7:
    def greeting(self):
        print('hello')
        
class Student(Person7):
    def greeting(self):
        print('good morning')
        

james = Student()
james.greeting()

class Point2D:
    def __init__(self):
        self.x_point = 100
        self.y_point = 200
        
    def print_point(self):
        print(f'x : {self.x_point}')
        print(f'y : {self.y_point}')

class Point3D(Point2D):
    def __init__(self):
        super().__init__()
        self.z_point = 300
        
    def print_point(self):
        super().print_point()
        print(f'z : {self.z_point}')

p3 = Point3D()
p3.print_point()