class MultiClass:
    def __init__(self, convar):
        self.convar = convar
    
    def multiply(self,number):
        return number * self.convar
    
# obj = MultiClass(5)
# print(obj.multiply(20))

# f = open('classData.p','wb')

import pickle
# pickle.dump(obj,f)
# f.close()

f2 = open('classData.p','rb')
obj2 = pickle.load(f2)
print(obj2.multiply(40))