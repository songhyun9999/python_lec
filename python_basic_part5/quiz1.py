class MultiIterator:
    def __init__(self,stop,mul):
        self.__count = 1
        self.__stop = stop
        self.__mul = mul
    
    @property
    def stop(self):
        return self.__stop
    @stop.setter
    def stop(self,stop):
        self.__stop = stop
        
    @property
    def mul(self):
        return self.__mul
    @mul.setter
    def mul(self,mul):
        self.__mul = mul
            
    def __iter__(self):
        return self
    
    def __next__(self):
        rt_val = self.__count*self.mul
        if rt_val < self.stop:
            self.__count += 1
            return rt_val
        else:
            raise StopIteration

for i in MultiIterator(20,3):
    print(i,end=' ')
print()        