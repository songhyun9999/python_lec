import matplotlib.pyplot as plt
import pandas as pd

# my_score = [(50,90,95), (60,75,100), (75,85,90), (85,75,90), (95,80,85), (90,85,80), (95,80,75)]
# df = pd.DataFrame(my_score, columns=['kor','math','eng'])
# print(df)
# df.plot(kind='line')
# plt.show()

import numpy as np

x = np.linspace(-np.pi, np.pi, 256)
y1, y2 = np.cos(x), np.sin(x)
# plt.plot(x, y1, ls='--', label='cosine')
# plt.plot(x, y2, ls=':', label='sine')
plt.plot(x, y1, ls='--')
plt.plot(x, y2, ls=':')
plt.xlabel('x axis')
plt.ylabel('result')
plt.legend(['cosine', 'sine'], loc='best', fontsize=14)
plt.show()

# my_score = np.array([(50,90,95), (60,75,100), (75,85,90), (85,75,90), (95,80,85), (90,85,80), (95,80,75)])
# print(my_score)
# plt.plot(my_score)
# plt.show()