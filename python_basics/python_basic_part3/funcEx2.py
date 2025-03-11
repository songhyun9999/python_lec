def add(num1,num2):
    total = num1 + num2
    print(f'num1:{num1} num2:{num2} sum:{total}')
    
add(100,200)
add(num1=100,num2=200)
add(num2=200,num1=100)
print()

def personal_info(name,age,address):
    print(f'name:{name} age:{age} address:{address}')

personal_info('kim',30,'busan')    
personal_info(name='kim',age=30,address='busan')
personal_info(address='busan',age=30,name='kim')
print()

data = {'name':'hyo', 'age':10, 'address':'busan'}
personal_info(data['name'],data['age'],data['address'])
personal_info(**data)
# print(*data)
print()

# **data : keyword argument (키워드 인자) -> 딕셔너리만 사용 가능
# **data 의미) name = '~~', age = '~~', address = '~~'
def personal_info2(**kargs): # 키워드 인자 타입으로 받음을 의미 -> kargs:딕셔너리
    for k,value in kargs.items():
        print(k,value,sep=':',end =' ')
    print()

personal_info2(name='kim', age=30, address='busan')
personal_info2(name='kim', age=30)
personal_info2(name='choi', weight=90, height=180)
personal_info(**data)



    
