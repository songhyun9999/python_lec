x=0

def A():
    x = 10
    def B():
        # global x  #전역 변수만 참조하므로 A내의 x는 참조 안함
        nonlocal x # 부모 함수에 있는 지역변수 x를 참조한다는 의미
                   # 함수 여러개면 바로 위의 부모함수부터 참조
        x = 20
    B()
    print(x)
    
A()
print(x)