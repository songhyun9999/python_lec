# 기본적으로 얕은복사를 수행
ldata = [0,0,0,0,0]
ldata2 = ldata

ldata2[2]=30000
print(f'ldata1:{ldata} == ldata2:{ldata2}')
print(ldata2 is ldata) # 출력 : True
print()

# 깊은복사 수행을 위해 copy() 함수 사용
ldata3 = ldata.copy()
# 다른 객체를 가리키지만 값은 같음
print(f'ldata1:{ldata} == ldata3:{ldata3}') 
print(ldata == ldata3) # 출력 : True
print(ldata3 is ldata) # 출력 : False

ldata3[2] = 1000
print(f'ldata1:{ldata} != ldata3:{ldata3}')
print(ldata == ldata3) # 출력 : False
