f1 = open('data/USPres.txt','r')
f2 = open('data/VPres.txt','r')

# pres = [line for line in f1]
# vpres = [line for line in f2]
outfile = open('Both.txt','w')

# for v in vpres:
#     if v in pres:
#         outfile.write(v)       

pres = {line for line in f1}
vpres = {line for line in f2}

ans = pres & vpres
# print(ans)
ans = list(ans)
outfile.writelines(ans)

outfile.close()
f2.close()
f1.close()