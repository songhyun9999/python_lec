'''
static method 와 class method
둘 다 클래스 선언과 동시에 
클래스에 할당된 메모리 영역에 저장되어
객체 생성 없이 클래스 이름으로 접근 가능
'''
class Calc:
    # static method 는 self를 일반적으로 인자로 받지 않음
    # 따라서 클래스 내부 인자와 상관없이 동작하는 함수를 만들때 사용
    @staticmethod
    def add(self,a,b):
        return a+b
    
    @staticmethod
    def mul(a,b):
        return a*b
    
    # class method 는 cls를 첫번째 인자로 지정해야함
    # cls 는 self 처럼 클래스의 주소를 의미하며 클래스 내부 인자에 접근 가능
    @classmethod
    def print_info(cls,name,age):
        print(name,age)

print(Calc.add(10,20))
print(Calc.mul(10,20))
Calc.print_info('kim',40)

