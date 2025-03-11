y = [10,20,30]

try:
    index,x = map(int,input('index & number for division: ').split())
    ans = y[index]/x
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
else: # else 문은 try 구문 내에서 오류가 없을 경우에만 실행
    print('예외가 없을 경우 실행')
    print(f'{y[index]} / {x} = {ans}')
finally: # finally 문은 예외 발생 여부와 상관없이 실행하면서 try catch문을 종료
    print('예외 발생 여부와 상관없이 실행')
    
