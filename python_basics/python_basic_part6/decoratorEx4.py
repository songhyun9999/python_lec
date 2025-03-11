def is_multiple(x):
    def real_decorator(funcv):
        def wrapper(n1, n2):
            revalue = funcv(n1, n2)
            if revalue % x == 0:
                print('{} revalue  is {} mutiple'.format(funcv.__name__, x))
            else:
                print('{} revalue  is not {} mutiple'.format(funcv.__name__, x))
            return revalue
        return wrapper
    return real_decorator


@is_multiple(3)
def add(n1, n2):
    return n1 + n2

print(add(10, 20))
print(add(10, 21))