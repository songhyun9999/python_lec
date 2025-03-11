data1 = {'name':'kim', 'age':20, 'addr':'seoul'}
print(data1)
print(type(data1))
print()

data2 = {100:'hundred', False:0, 3.5:[3.5,3.5]}
print(data2)
print()

print(data1['name'])
print(data2[100])
print(data2[False])
print()

# key 값은 str로 변경되어 dict로 생성시 '' "" 추가하면 key에 해당 값도 추가
data3 = dict(name='lim',age = 30)
print(data3)
print()

data4 = dict([('name','choi'),('age',40),('height',180)])
print(data4)
print()

print(data4['name'])
print(data4.get('name'))

# 없는 key 로 가져오려 할 경우 error 발생
# get() 으로 가져오면 오류없으며 없는 값에 대한 default 값 지정 가능
# print(data4['weight'])
print(data4.get('weight')) # 출력 : None
print(data4.get('weight',0)) # 출력 : 0
print()

data4['name'] = 'kim' # value 변경
print(data4)
data4['address'] = 'seoul' # key,value 쌍 추가
print(data4)

data4.setdefault('weight')
print(data4)

data4.setdefault('id',3232)
print(data4)
print()

data5 = {'name':'lee'}
data5.update(age=20,addr='incheon')
print(data5)

data5.update({1:'one',2:'two'})
print(data5)

data5.update([('height',190),('weight',90)])
print(data5)
print(data5.pop('name'))
print(data5)
print(data5.pop('name','noname')) #해당 키 없으면 오류, default 지정해야함
