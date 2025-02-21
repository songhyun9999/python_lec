class Person2:
    '''
    `앞뒤`로 __(밑줄두개)가 붙은 메서드는 
    파이썬이 자동으로 호출해주는 메소드
    '''
    def __init__(self):
        self.hello = 'hello'
        self.name = 'kim'
        self.age = 27
        self.addr = 'seoul'
        
    def greeting(self):
        print(' '.join([f'{self.hello} i am {self.name}',
                    f'my address is {self.addr}']))
        

kim = Person2()
kim.greeting()
print(kim.name)
print(kim.addr)





