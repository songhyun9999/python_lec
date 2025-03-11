import numpy as np
import matplotlib.pyplot as plt


label_list = ['Iris-setosa','Iris-versicolor','Iris-virginica']

def read_label(label):
    return label_list.index(label)

iris_data = np.loadtxt('iris.data.txt',
                    delimiter=',',
                    converters={4 : read_label})

print(iris_data)
color_set = ('b','g','r')
color_list = [color_set[int(label)] for label in iris_data[:,4]]
print(color_list)
plt.scatter(iris_data[:,0],iris_data[:,1],c=color_list)

import matplotlib.patches as patches
plt.legend(handles=[patches.Patch(color='b',label='iris-setosa'),
                    patches.Patch(color='g',label='iris-versicolor'),
                    patches.Patch(color='r',label='iris-virginica')],
           loc='best',edgecolor='k')

plt.show()


