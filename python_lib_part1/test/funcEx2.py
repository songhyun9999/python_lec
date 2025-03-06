def print_info(name,age):
    print(name,age)

print_info('kim',30)
print_info(age=20,name='lee')

ddata = {'name':'choi','age':10}
print_info(**ddata)
print()

def print_info2(**data):
    for k,v in data.items():
        print(v,end=' ')


print_info2(name='kim')
print()
print_info2(name='kim',age=20)
print()
print_info2(name='kim',age=20,address='seoul')
print()
print_info2(**ddata)