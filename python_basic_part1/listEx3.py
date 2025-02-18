import numpy as np

ldata1 = [10,20,30]
b = [500,600]

print(len(ldata1))
ldata1.append(b) # 리스트 자체를 객체로 취급하여 하나의 원소로 추가
print(len(ldata1))

ldata1 += [1,2] # extend 와 같은 로직으로 동작
# ldata1.extend([1,2]) 
print(ldata1)
print()

ldata2 = [100,200]
nparray = np.array(ldata2)
'''
### numpy array 인지 list 인지 확인하는게 중요함 ###
- numpy : array 내부의 값에 3을 곱함
- list  : list를 복제하여 붙히고 return함
'''
print(ldata2 * 3) # 출력 : [100,200,100,200,100,200]
print(nparray * 3)  # 출력 : [300,600]