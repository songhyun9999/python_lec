def trace(funcv):
    def wrapper():
        print(funcv.__name__, 'function start')
        funcv()
        print(funcv.__name__, 'function end')
    return wrapper

@trace
def hello():
    print('hello!!!!!!!')

@trace
def world():
    print('world~~~~~~~')

hello()
print()
world()
# print()

# hello = trace(hello)
# hello()
# print()

# world = trace(world)
# world()