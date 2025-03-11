ldata = [1.2,2.3,3.4,4.5,5.6,6.7]
ldata2 = ldata.copy()
for i in range(len(ldata)):
    ldata[i] = int(ldata[i])
    
ldata2 = list(map(int,ldata2))
print(ldata,ldata2)
print()

idata = list(map(float, input('input data : ').split(' ')))
print(idata)