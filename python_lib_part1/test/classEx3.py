class Calc:
    age = 10
    name = 'kim'

    @staticmethod
    def add(n1,n2):
        return n1+n2

    @staticmethod
    def mul(n1,n2):
        return n1*n2

    @classmethod
    def print_info(cls):
        print(cls.name, cls.age)




print(Calc.mul(10,20))
print(Calc.add(11,11))
Calc.print_info()