tdata1 = (10,20,30,40)
print(tdata1)
print(type(tdata1))

tdata2 = (False,'hello',123,0.123)
print(tdata2)
print()

tdata3 = 10,20,30,40
print(tdata3)
print(type(tdata3))

tdata4 = ()
tdata5 = tuple()
print(tdata4)
print(tdata5)
print()

print(tdata2[0])
print(tdata2[-1])


''' 튜플은 값 변경 불가능 '''
# tdata1[0] = 1000  # TypeError 발생
