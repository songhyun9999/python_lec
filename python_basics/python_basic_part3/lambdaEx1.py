def plus_ten(n):
    return n+10

print(plus_ten(100))

lf = lambda n : n+10
print(lf(100))

ladd = lambda n1,n2 : n1+n2
print(ladd(100,20))

ldata2 = [('lee',90),('kim',50),('choi',70)]
ldata2.sort(key=lambda x:x[1])
print(ldata2)
print()

ldata3 = ['20','70','100','120']
print(list(map(int,ldata3)))

ldata4 = [90,77,22,55]
ldata5 = list(map(plus_ten,ldata4))
print(ldata5)

print(list(map(lambda x:x+10, ldata4)))

a=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:str(x) if x==1 else float(x) if x==2 else x+10,a)))

a = [1,2,3,4,5]
b = [2,4,6,8,10]
print(list(map(lambda x,y: x*y,a,b)))
print(list(map(lambda x,y: (x,y),a,b))) # zip 처럼 동작
print(list(zip(a,b)))