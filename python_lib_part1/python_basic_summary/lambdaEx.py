def calc(fval,n1,n2):
    rvalue = fval(n1,n2)
    return rvalue

print(calc(lambda x,y: x+y+10, 100, 200))

ldata = [('lee',50),('kim',60),('oh',30)]

ldata.sort(key=lambda x:x[1])
print(ldata)