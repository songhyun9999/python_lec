import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4,4,1024)
y = 0.25 * (x+4) * (x+1) * (x-2)
# plt.text(-0.5,1.25,'black text mark',fontsize=12)
# plt.plot(x,y,c='k')
# plt.show()

box = {
    'facecolor':'g',
    'alpha': 0.5,
    'edgecolor': 'k',
    'boxstyle': 'round'
}

plt.text(-0.5,1.25,'black text mark',bbox = box,fontsize=12)
plt.plot(x,y,c='k')
plt.show()
