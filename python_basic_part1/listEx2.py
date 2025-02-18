ldata = [50,30,90,70,60,20,80,10]
print(ldata[1:3])

print(ldata[0:4])
print(ldata[:4]) # 앞을 생략하면 처음부터라는 의미
print(ldata[2:8])
print(ldata[2:]) # 뒤를 생략하면 끝까지 라는 의미
print(ldata[:]) # 전부 생략하면 처음부터 끝까지
print(ldata[5:])
print(ldata[-3:]) # 뒤에서 3번쨰부터 끝까지
print()

ldata2 = ['서울','부산','대구','대전','광주','수원','인천']
print(ldata2[1:6]) 
print(ldata2[1:6:2]) # 1번 인덱스부터 2씩 증가시켜 6번 인덱스전까지
print(ldata2[::-1]) # 처음부터 끝까지 반대 순서로
print()

# 튜플도 같은 로직으로 동작
ldata3 = '서울','부산','대구','대전','광주','수원','인천'
print(ldata3[1:6]) 
print(ldata3[1:6:2]) # 1번 인덱스부터 2씩 증가시켜 6번 인덱스전까지
print(ldata3[::-1]) # 처음부터 끝까지 반대 순서로
print()

# string 도 같은 로직으로 동작
strdata = 'hello'
print(strdata[:2])
print(strdata[::-1])