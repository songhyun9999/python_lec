def ft_func(x):
    return x>5 and x<10

ldata = [7,4,8,9,2,1,6,10]
print(list(filter(ft_func,ldata)))
print(list(filter(lambda x: x>5 and x<10 ,ldata)))
