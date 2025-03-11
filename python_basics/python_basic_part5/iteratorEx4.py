class Counter:
    def __init__(self, stop):
        self.stop = stop
        
    def __getitem__(self,index):
        if index < self.stop:
            return index
        else:
            raise IndexError
        
print(Counter(3)[0])
print(Counter(3)[1])
print(Counter(3)[2])
# print(Counter(3)[3]) # indexError 발생

