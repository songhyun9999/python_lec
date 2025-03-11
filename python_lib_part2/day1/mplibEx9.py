import numpy as np
import matplotlib.pyplot as plt

for i in range(1,5):
    plt.subplot(2,2,i)
    plt.plot(np.random.randn(50))
    plt.title(f'axes{i}')

plt.suptitle('multi view',fontsize=16)
# plt.subplots_adjust(hspace=0.4,wspace=0.2)
plt.tight_layout()

plt.show()
