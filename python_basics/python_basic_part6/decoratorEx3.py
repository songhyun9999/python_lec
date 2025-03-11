def trace(funcv):
    def wrapper(*args, **kwargs):
        revalue = funcv(*args, **kwargs)
        if len(args) == 0:
            print(f'{funcv.__name__}, kwargs={kwargs} => {revalue}')
        elif len(kwargs) == 0:
            print(f'{funcv.__name__}, args={args} => {revalue}')
        return revalue
    return wrapper

@trace
def getmax(*args):
    return max(args)

print(getmax(40,10,80,20))
print()

@trace
def get_min(**kwargs):
    return min(kwargs.values())
print(get_min(x=20, y=10, z=100))
