class Person2:
    def __init__(self,name='kim',age=27,addr='seoul',weight=80):
        self.hello = 'hello'
        self.name = name
        self.age = age
        self.addr = addr
        # __ (2개) 붙으면 private , _ (1개) 붙으면 protected
        self.__weight = weight
        
    def print_info(self):
        print(' '.join([f'name:{self.hello} age:{self.name}',
                    f'addr:{self.addr} weight:{self.__weight}']))
        
kim = Person2()
kim.print_info()
# print(kim.__weight) # private 속성이므로 접근 불가 error

# 외부에 새로운 변수처럼 할당하여 접근 가능해짐
# 실제 __weight 값은 변하지 않음
kim.__weight = 120
print(kim.__weight) # 120
kim.print_info()    # 80 실제 값은 변하지 않음