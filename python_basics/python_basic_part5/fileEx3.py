file = open('data/States.txt','r')
ldata1 = [line for line in file]
# print(ldata1)
# ldata1.sort()
# print(ldata1)
file.close()

# outfile1 = open('StatesAlpha.txt','w')
# outfile1.writelines(ldata1)
# outfile1.close()

outfile2 = open('StatesLen.txt','w')
# ldata1.sort(key=lambda x:len(x),reverse=True)
ldata1.sort(key=len,reverse=True)
# for i in range(0,len(ldata1)-1):
#     for j in range(i,len(ldata1)):
#         if len(ldata1[i]) > len(ldata1[j]):
#             ldata1[i] , ldata1[j] = ldata1[j], ldata1[i]
# print(ldata1)

outfile2.writelines(ldata1)
outfile2.close()

# 3번째 알파벳의 순서대로 sort
outfile3 = open('StatesSecondChar.txt','w')
ldata1.sort(key=lambda x:x[2])
# print(ldata1)
outfile3.writelines(ldata1)   
outfile3.close() 