import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font',family='Malgun Gothic')

# x = np.random.randn(10000)
# plt.hist(x,bins=30)
# plt.hist(x,bins=30,density=True)
# plt.show()

human = pd.read_csv('human_height.csv')
human.info()
man = human['man']
woman = human['woman']
plt.figure(figsize=(7,5))
plt.hist(man,bins=20,alpha=0.5,label='man',rwidth=0.9)
plt.hist(woman,bins=20,alpha=0.5,label='woman',rwidth=0.9)

plt.xlabel('height')
plt.ylabel('frequency')
plt.title('man height distribution')
plt.show()

