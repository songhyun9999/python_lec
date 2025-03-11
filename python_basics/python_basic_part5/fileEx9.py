import os

if not os.path.isdir('log'): # 디렉토리 존재 유무 판단
    os.mkdir('log')
    
if not os.path.exists('log/count_log.txt'): # 파일 존재 유무 판단
    f = open('log/count_log.txt','w',encoding='utf-8')
    f.write('기록을 시작합니다.\n')
    f.close()

file = open('log/count_log.txt','r',encoding='utf-8')
rstr = file.read()
print(rstr)