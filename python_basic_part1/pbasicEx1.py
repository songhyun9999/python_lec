var1 = 10
var2 = 'hello world'
var3 = 42.33232
var4 = True

print(var1)
print(type(var1))
print(var2)
print(type(var2))
print(var3)
print(type(var3))
print(var4)
print(type(var4))

if type(var1) == int:
    print('goood')
else:
    print('bad')
print()
    
    
x,y,z = 10,20,30
print(x,y,z)
print()

x2 = y2 = z2 = 200
print(x2,y2,z2)
print()

print(x,y)
x,y = y,x
print(x,y)
print()

x += 100
print(x)
print()

print(10/4)
print(10//4)
print(10*10*10*10)
print(10**4)