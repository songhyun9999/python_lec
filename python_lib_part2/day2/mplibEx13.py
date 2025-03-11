import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from matplotlib.pyplot import xlabel

# x=np.linspace(-15,15,1024)
# y=np.sinc(x)
#
# ax = plt.axes()
#
# ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
# ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
# plt.plot(x,y,c='k')
# plt.show()

ax = plt.gca()

def make_label(value,pos):
    return f'{100*value:.1f}%'

ax.xaxis.set_major_formatter(ticker.FuncFormatter(make_label))

x = np.linspace(0,1,256)
plt.plot(x,np.exp(-10*x),c='k')
xlabels = ax.get_xticklabels()
plt.setp(xlabels,rotation=30,fontsize=12)

plt.show()