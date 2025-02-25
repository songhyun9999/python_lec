class TraceC:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwds):
        revalue = self.func(*args, **kwds)
        print(f'{self.func.__name__}, args={args}, kwargs={kwds} => {revalue}')
        return revalue
    

@TraceC
def add(a, b):
    return a + b

print(add(10, 20))
print()
print(add(a=20, b=30))