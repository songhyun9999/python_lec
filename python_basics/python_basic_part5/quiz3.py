president = input('Enter the name of a president : ')

with open('data/Justices.txt','r') as f:
    df = [data.split(',') for data in f if data.split(',')[2] == president]

ans = []
for idx, val in enumerate(df):
    df[idx][-1] = int(df[idx][-1])
    df[idx][-2] = int(df[idx][-2])
    if df[idx][-1] == 0:
        df[idx][-1] = 2015
    work_year = df[idx][-1] - df[idx][-2]
    df[idx].append(work_year)
    ans.append(df[idx])

ans.sort(key=lambda x:x[-1],reverse=True)

justice = []
for idx,val in enumerate(ans):
    justice.append(val[0]+' '+val[1])

print('Justice Appointed:')
for j in justice:
    print(f'{j:^30}')
    
    
        
    
    
    




    