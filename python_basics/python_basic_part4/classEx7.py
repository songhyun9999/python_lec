class Person4:
    count = 0
    
    def __init__(self):
        Person4.count += 1
        
    @classmethod
    def print_make_count(cls):
        print(f'{cls.count}개의 객체가 생성되었습니다.')
        
obj1 = Person4()
obj2 = Person4()
obj3 = Person4()

Person4.print_make_count()