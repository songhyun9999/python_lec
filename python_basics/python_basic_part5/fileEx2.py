# infile1 = open('data/FirstPresidents.txt','r') # file 객체는 iterator 지원
# rstr = infile1.read() # 파일을 한번에 읽어옴
# print(rstr) 

# rl = infile1.readline() # 파일의 한줄 읽기
# print(rl)

# for line in infile1:
#     print(line,end='')

infile2 = open('data/FirstPresidents.txt','r')
ldata = [line.rstrip() for line in infile2]
print(ldata)