with open('hello.txt','r') as f:
    print(f.read())
print()

class customOpen:
    def __init__(self,path):
        print('__init__call')
        self.file = open(path)
        
    def __enter__(self):
        print('__enter__')
        return self.file
    
    def __exit__(self,type,value,traceback):
        print('__exit__')
        self.file.close()
    
with customOpen('hello.txt') as f:
    print(f.read())
print()