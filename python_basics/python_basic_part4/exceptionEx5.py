class NotThreeMulException(Exception):
    def __init__(self, *args):
        super().__init__('not three multiple Error')
        
def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요'))
        if x % 3 != 0:
            raise NotThreeMulException
        print(x)
    except NotThreeMulException as e:
        print('예외발생',e)
        
three_multiple()