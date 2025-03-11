class IsMultiple:
    def __init__(self, value):
        self.value = value

    def __call__(self, func):
        def wrapper(a, b):
            revalue = func(a, b)
            if revalue % self.value == 0:
                print("{}'revalue is {} multiple".format(func.__name__, self.value))
            else:
                print("{}'revalue is not {} multiple".format(func.__name__, self.value))
            return revalue
        return wrapper
    
@IsMultiple(4)
def add(n1, n2):
    return n1 + n2

print(add(10,30))
print(add(10,31))