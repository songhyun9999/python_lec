class TraceC:
    def __init__(self, func):
        self.func = func
    
    def __call__(self):
        print(self.func.__name__, 'function start')
        self.func()
        print(self.func.__name__, 'function end')

@TraceC
def hello():
    print('hello!!!!!!')

#obj1 = TraceC(hello)
#obj1.__call__()
#obj1()

# hello = TraceC(hello)
# hello()
hello()