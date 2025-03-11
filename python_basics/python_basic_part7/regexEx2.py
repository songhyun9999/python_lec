import re

fdata1 = re.findall(r'[0-9]{3}-[0-9]{4}-[0-9]{4}',
                    'tel:010-1234-1234')
print(fdata1)

fdata1 = re.findall(r'[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}',
                    'tel:010-1234-1234 home:02-1234-1234 p:032-352-1234')
print(fdata1)
print()

fdata2 = re.findall(r'[a-zA-Z]+','232hello Good32 hi')
print(fdata2)

fdata2 = re.findall(r'[A-Z0-9]+','232hello Good32 hi')
print(fdata2)

# 한글만 선택
fdata2 = re.findall(r'[가-힣]+','232heㅎㅎllo G안녕하세요ood32 hi방갑')
print(fdata2)

# 한글자 한글 선택 ㅎㅎ 등
fdata2 = re.findall(r'[ㄱ-ㅎ|-|가-힣]+','232heㅎㅎllo G안녕하ㅎㅇㅎㅇ세요ood32 hi방갑')
print(fdata2)

fdata3 = re.findall(r'[^A-Z]+','HELLO GOOD morning 23232 안녕')
print(fdata3)

fdata3 = re.findall(r'[^가-힣]+','HELLO GOOD morning 23232 안녕')
print(fdata3)
print()

fdata4= re.findall(r'\d{3}-\d{4}-\d{4}','tel:010-1234-1234')
print(fdata4)

fdata5= re.findall(r'\D+','Hello Good moring 2222 하이여')
print(fdata5)

fdata6 = re.findall(r'[a-zA-Z0-9]+','print_info(hello_insa)')
print(fdata6)

fdata6 = re.findall(r'\w+','print_info(hello_insa)')
print(fdata6)

fdata6 = re.findall(r'\W+','print_info(hello_insa)')
print(fdata6)

fdata7 = re.findall(r'[a-zA-Z0-9]+ ','Hello 1234')
print(fdata7)

fdata7 = re.findall(r'[a-zA-Z0-9]+\s','Hello 1234')
print(fdata7)

fdata7 = re.findall(r'[a-zA-Z0-9]+\S','Hello 1234')
print(fdata7)
