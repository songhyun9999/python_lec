import os

with open('data/Pre1990.txt','r') as f:
    ans = {data.rstrip() for data in f}

with open('data/Retired.txt','r') as f:
    ret = {data.rstrip() for data in f}
    ans = ans - ret
    
with open('data/Added.txt','r') as f:
    add = {data.rstrip() for data in f}
    ans = ans | add

ans = sorted(list(ans))
ans = '\n'.join(ans)

with open('data/answer.txt','w') as f:
    f.write(ans)

