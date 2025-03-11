# 같은 역할을 하는 세 구문
ldata = []
for i in range(10):
    ldata.append(i)
    
ldata2 = [i for i in range(10)]
ldata3 = list(i for i in range(10))
print(ldata, ldata2, ldata3,sep='\n')
print()

ldata4 = [i*2 for i in range(10)]
print(ldata4)
print()

ldata5 = [i+2 for i in range(10) if i % 2 == 0 ]
print(ldata5)
print()

# for문을 통해 생성되는 순서는 뒤에서 앞으로
ldata6 = [i*j for j in range(2,10)
              for i in range(1,10)]
# i : (1~9) 생성 -> j가 (2~9) 생성
# i에 j가 생성될때마다 곱해 생성된 값을 리스트에 추가 
print(ldata6)
print()

# else 를 사용할 경우 if문을 앞에 써야함
ldata7 = [i if i%2==0 else 100 for i in range(10)]
print(ldata7)
print()

