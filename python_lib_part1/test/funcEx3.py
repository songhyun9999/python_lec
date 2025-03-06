def insa():
    print('hello')

print(insa)

insa()

fvalue = insa
fvalue()

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def calc(fval, n1, n2):
    rvalue = fval(n1 , n2)
    return rvalue

print(calc(mul, 100, 20))
print(calc(subtract, 100, 20))

ldata = [('lee', 50), ('choi', 10), ('oh', 30)]
def sfunc(x):
    return x[1]
ldata.sort(key=sfunc)
print(ldata)