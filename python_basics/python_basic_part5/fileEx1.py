# 파일 쓰기
# file = open('hello.txt','w')
# file.write('hello python~~~')
# file.close()

# 파일 읽기
file2 = open('hello.txt','r')
readStr = file2.read()
print(f'rstr : {readStr}')
file2.close()
