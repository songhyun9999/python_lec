data = {
    'k11' : {'name':'kim','age':20},
    'v42' : {'name':'park','age':30}
}
print(data)
print(data['v42'])
print(data['v42']['name'])

data2 = data
print(data is data2) # 출력 : True
data3 = data.copy()
print(data is data3) # 출력 : False
print()

data['k11']['name'] = 'ch'
print(data)
print(data3) 
# 둘 출력 같음 -> 딕셔너리 안에 선언된 딕셔너리는 같은것을 공유함
print()

import copy
data4 = copy.deepcopy(data) # 딕셔너리 안의 딕셔너리까지 깊은복사

data4['k11']['name'] = 'hyo'
print(data4)
print(data)
