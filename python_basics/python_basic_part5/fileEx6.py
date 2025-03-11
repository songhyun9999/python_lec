import pickle

name = 'lee'
age = 20
addr = 'seoul'
score = {'kor':90,'eng':88,'math':77}

file = open('obj_data.p','wb')
pickle.dump(name,file)
pickle.dump(age,file)
pickle.dump(addr,file)
pickle.dump(score,file)
file.close()