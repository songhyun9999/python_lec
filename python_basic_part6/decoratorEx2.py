def trace(funcv):
    def wrapper(n1, n2):
        result = funcv(n1, n2)
        print(f'{funcv.__name__}(n1={n1}, n2={n2}) => {result}')
        return result
    return wrapper

@trace
def add(n1, n2):
    return n1 + n2

print(add(20, 50))


def test(func):
    def wrap(n1,n2):
        result = func(n1, n2)
        print(f'{func.__name__}(n1={n1}, n2={n2}) => {result}')
        return result
    return wrap

@test
def min(n1,n2):
    return n1-n2
print(min(100,20))
print(type())