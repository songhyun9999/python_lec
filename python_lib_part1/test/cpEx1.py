################# list 초기화 ######################
# ldata = []
# for i in range(10):
#     ldata.append(i)
#
# print(ldata)
#
# ldata2 = [i for i in range(10)]
# print(ldata2)

################# list 초기화 + 조건문 ###############
# ldata = []
# for i in range(20):
#     if i%2==0:
#         ldata.append(i)
# print(ldata)
#
# ldata2 = [i for i in range(20) if i%2==0]
# print(ldata2)

ldata = []
for i in range(20):
    if i%2==0:
        ldata.append(i)
    else:
        ldata.append(10)
print(ldata)

ldata2 = [i if i%2==0 else 10 for i in range(20) ]
print(ldata2)
