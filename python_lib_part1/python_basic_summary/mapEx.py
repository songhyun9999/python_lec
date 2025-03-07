# scores = list(map(int , input('정수를 여러개 입력하세요:').split()))
# print(scores)


scores = list(map(lambda x : int(x) + 10 , input('정수를 여러개 입력하세요:').split()))
print(scores)