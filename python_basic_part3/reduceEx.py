from functools import reduce

def rfunc(x,y):
    return x+y

ldata = list(range(11))
print(reduce(rfunc,ldata))
print(reduce(lambda x,y:x+y,ldata))
