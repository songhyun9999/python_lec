def three_multiple():
    x = int(input('3의 배수를 입력하세요 : '))
    if x%3 != 0:
        raise Exception('3의 배수 아님')
    else:
        print(x)
        
try:
    three_multiple()
except Exception as e:
    print('에러발생!!!!',e)
    raise RuntimeError('three_multiple 함수에서 예외가 발생했습니다.')
