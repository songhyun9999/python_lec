i = 0
total = 0
end = input('정수를 입력하세요: ')
while i<=int(end):
    total += i
    i += 1
    
print(f'1부터 {end}까지의 누적합 : {total}')
