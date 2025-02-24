import os

continent = input('input continent name : ')
continent = continent.title() # 첫번째 문자는 대문자 나머지는 소문자로 변환
# print(continent)
abs_path = os.path.dirname(os.path.abspath(__file__))
infile = open(f'{abs_path}/UN.txt','r',encoding='utf-8')

indata = [data.split(',') for data in infile]

for data in indata:
    if data[1] == continent:
        print(data[0])