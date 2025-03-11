class CustomRange:
    def __init__(self,stop):
        self.current = 0
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.stop:
            rvalue = self.current
            self.current += 1
            return rvalue
        else:
            raise StopIteration
for i in CustomRange(10):
    print(i,end=' ')
print()
