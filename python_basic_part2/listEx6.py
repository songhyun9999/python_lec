ldata = [33,22,11,77,99,55]
for val in ldata:
    print(val,end=' ')
print()
print()

for i,val in enumerate(ldata):
    print(f'{i}->{val}')
print()

#enum 시작 번호 지정가능
for i,val in enumerate(ldata,start=3):
    print(f'{i}->{val}')

