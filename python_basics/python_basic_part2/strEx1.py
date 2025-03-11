ldata = ['red','green', 'blue']
strv = ''

for sd in ldata:
    strv += sd
print(strv)

print(''.join(ldata))
print('-'.join(ldata))
print(','.join(ldata))
print('/'.join(ldata))

str1 = '           python            '
print('-------',str1,'-------',sep = '')
print('-------',str1.strip(),'-------',sep = '')
print('-------',str1.lstrip(),'-------',sep = '')
print('-------',str1.rstrip(),'-------',sep = '')
print()

str2 = ',.python.,'

print(str2.strip(',.'))
print(str2.lstrip(',.'))
print(str2.rstrip(',.'))
print()

str3 = 'python'
print('---',str3.ljust(10),'---',sep='')
print('---',str3.rjust(10),'---',sep='')
print('---',str3.center(10),'---',sep='')
print()

str4 = '35'
print(str4.zfill(4))
print('3.5'.zfill(6))
print('test'.zfill(7))
print()

table = str.maketrans('aeiou','12345')
print('apple'.translate(table))
print()

