import re
rc =re.compile('world')
rdata1 = re.search(rc,'hello world it is good')
print(rdata1)
print(rdata1.span())
print(rdata1.group(0))
print(rdata1.group())
print()

rdata1 = re.search(pattern=r'world',string='hello world it is good')
print(rdata1)
rdata1 = re.search('world','hello world hello it is good')
print(rdata1)
rdata1 = re.search('world','hello world it is good')
print(rdata1)

rdata2 = re.match(r'hello','hello world hello it is good')
print(rdata2)
rdata2 = re.match(pattern=r'world',string='hello world hello it is good')
print(rdata2)

fdata1 = re.findall(pattern=r'hello',string='hello world hello it is good')
print(fdata1)

rdata3 = re.search(pattern=r'^hello',string='hello world hello it is good')
print(rdata3)
rdata3 = re.search(pattern=r'^world',string='hello world hello it is good')
print(rdata3)
rdata3 = re.search(pattern=r'good$',string='hello world hello it is good')
print(rdata3)
rdata3 = re.search(pattern=r'world$',string='hello world hello it is good')
print(rdata3)
print()

fdata2 = re.findall(r'hello|world','hello world hello it is good hello')
print(fdata2)
print()

fdata3 = re.findall(r'a*b','ab ab bb ccc')
print(fdata3)

fdata3 = re.findall(r'a+b','ab ab bb ccc aab aaa')
print(fdata3)

fdata3 = re.findall(r'a+b*','ab ab bb ccc aab aaa')
print(fdata3)

fdata4 = re.findall(r'[0-9]+','hello 3232 find fx855eeee')
print(fdata4)

fdata5 = re.findall(r'b.d','bed bad bib b@d,beed')
print(fdata5)

