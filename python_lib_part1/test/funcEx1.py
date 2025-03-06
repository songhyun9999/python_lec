

def add(n1,n2,n3):
    return n1+n2+n3

print(add(10,20,30))

tdata = (90,80,100)
print(add(*tdata)) # tuple unpacking
print()

def add2(*data): # argument packing
    result = 0
    for d in data:
        result += d
    return result

print(add2(10,20))
print(add2(10,20,30))
print(add2(10,20,30,40))

