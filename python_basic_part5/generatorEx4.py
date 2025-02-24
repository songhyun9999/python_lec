# def number_generator3():
#     x = [1,2,3,4]
#     yield from x # 리스트의 값을 한번에 전달 for문 생략 가능
    
# for i in number_generator3():
#     print(i)
    
def number_generator4(stop):
    n = 0
    while n<stop:
        yield n
        n += 1
        
def three_generator():
    yield from number_generator4(3)
    
for i in three_generator():
    print(i)