try:
    x = int(input('3의 배수를 입력하세요 : '))
    if x % 3 != 0:
        raise Exception('3의 배수가 아닙니다.')
except Exception as e:
    print('three_multiple 함수에서 예외가 발생했습니다.', e)
    raise RuntimeError('three_multiple 함수에서 예외가 발생했습니다.')