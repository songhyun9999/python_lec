def upper_generator(x):
    for data in x:
        yield data.upper()
    
fruits = ['apple', 'banana', 'grape', 'orange']

for i in upper_generator(fruits):
    print(i)