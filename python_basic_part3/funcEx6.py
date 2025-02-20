def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

def calc(cf,n1,n2):
    result = cf(n1,n2)
    return result

print(calc(mul,10,20))
print(calc(div,10,20))
print()

ldata = [4,1,2,8,3]
ldata.sort()
print(ldata)
ldata.sort(reverse=True)
print(ldata)
print()

ldata2 = [('lee',90),('kim',30),('choi',1000),('hyp',200)]

def mfunc(x):
    return x[1]

ldata2.sort(key=mfunc)
print(ldata2)
print()

ldata3 = ['democratic','squoia','equals','brrr','break','two']

ldata3.sort(key=lambda x:x[-1],reverse=True)
print(ldata3)

