import numpy as np

def adata_reshape(lr):
    arr = np.array(lr,dtype=np.int16).reshape(3,5)
    return arr


def get_data(arr):
    return (arr>7).any(axis=0)


with open('n_quiz1_data.txt','r') as f:
    data = [item.split(',') for item in f]

data = adata_reshape(data)
print(data)
print()
print(data[:,get_data(data)])
