ivalue = 300
fvalue = 87.2323
svalue = 'kim'
print('ivalue:%d fvalue:%f svalue:%s'%(ivalue,fvalue,svalue))
print('ivalue:{0} fvalue:{1} svalue:{2}'.format(ivalue,fvalue,svalue))
print('ivalue:{2} fvalue:{1} svalue:{0}'.format(ivalue,fvalue,svalue))
print('ivalue:{} fvalue:{} svalue:{}'.format(ivalue,fvalue,svalue))
print(f'ivalue:{ivalue} fvalue:{fvalue} svalue:{svalue}')
print()

print('ivalue:%10d fvalue:%-12f svalue:%5s'%(ivalue,fvalue,svalue))
print('ivalue:{0:<10} fvalue:{1:12f} svalue:{2:5}'.format(ivalue,fvalue,svalue))
print('ivalue:{:10} fvalue:{:<12.2f} svalue:{:>5}'.format(ivalue,fvalue,svalue))
print(f'ivalue:{ivalue:<10} fvalue:{fvalue:12.2f} svalue:{svalue:<5}')
