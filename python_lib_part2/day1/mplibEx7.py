import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('sample.txt')
print(data)
print(type(data))
print()

# plt.plot(data[:,0],data[:,1])
# plt.plot(data)
# plt.show()

for col in data.T:
    plt.plot(data[:,0],col)
plt.show()