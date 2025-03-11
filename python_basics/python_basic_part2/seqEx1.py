ldata = [10,20,30,40]
tdata = 100,200,300,400
sdata = 'hello'

print(100 in ldata)
print(100 not in ldata)
print(100 in tdata)
print('he' not in sdata)
print()

print(ldata + [100,200])
print(tdata + (100,200)) # 추가만하고 변경 X 이므로 튜플도 가능
print(sdata + 'good')
print()

print(ldata * 2)
print(tdata * 2)
print(sdata * 2)
print()

ld1 = [0,0]
ld2 = [1,1,1]
ld3 = ld1 * 2 + ld2 * 3
print(ld3)