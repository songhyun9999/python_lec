def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x
            nonlocal y
            x += 30
            y += 300
            print(x)
            print(y)
        C()
    B()
A()
print()

x = 1
def A2():
    x = 10
    def B():
        x = 20
        def C():
            global x
            x += 30
            print(x)
        C()
    B()
A2()