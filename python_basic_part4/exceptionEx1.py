try:
    x = int(input('나눌 숫자를 입력하세요:'))
    y = 10 / x
    print(y)
except ZeroDivisionError as e:
    print(e)
except ArithmeticError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
    




