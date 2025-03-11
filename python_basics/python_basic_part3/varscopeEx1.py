x = 10
def foo():
    x = 20
    print(x)    
    
foo()
print(x)

def foo2():
    global x
    x = 100
    print(x)

foo2()
print(x)

