import re

robj1 = re.search(r'([0-9]+) ([0-9]+)','good 423 122 hello')
print(robj1)
print(robj1.group(0)) # 한꺼번에
print(robj1.group(1)) # 첫번째 그룹
print(robj1.group(2)) # 두번째 그룹
print(robj1.groups()) # 그룹 묶어서 튜플로 반환
print()

# ?P<name> : 그룹에 이름을 할당하여 구분, 그룹이 많아지면 구분하기 어렵기때문에 사용
robj2 = re.search(r'(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<args>\w+)\)','hello _print_info(var22) good job')
print(robj2)
print(robj2.group(1))
print(robj2.group(2))
print(robj2.group('func'))
print(robj2.group('args'))
print()
