import pickle

with open('obj_data.p','rb') as f:
    name = pickle.load(f)
    age = pickle.load(f)
    addr = pickle.load(f)
    scores = pickle.load(f)
    
print(name,age,addr)
print(scores)