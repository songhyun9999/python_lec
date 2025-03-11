def calc(num1 = 3,num2 = 5):
    def mul_add(x):
        return num1 * x + num2
    return mul_add

cf = calc()
print(cf(2))

def calc2():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a*x +b
        print(total)
    return mul_add

c = calc2()
c(1)
c(2)
c(3)