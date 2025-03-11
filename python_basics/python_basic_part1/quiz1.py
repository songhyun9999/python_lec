name = input('이름을 입력하세요 : ')
age = int(input('나이를 입력하세요 : '))
mon = float(input('시작 연봉을 입력하세요 : '))
total = 0

while(age<65):
    total += mon
    mon = mon* 1.05    
    age += 1

total = int(total)
print(f'{name}는 총${total}를 벌 것이다.')