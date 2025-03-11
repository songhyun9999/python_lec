'''
여러 줄 주석
'''
# 한줄 주석
"""
또 다른 여러 줄 주석    
"""



ivar = input('값을 입력해주세요:')
print(f'ivar={ivar}')
print(type(ivar))
try:
    ivar2 = int(ivar)
    print(type(ivar2))
except:
    pass
