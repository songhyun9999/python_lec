import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(12).reshape(3,4),
                    index=['Ohio','Colorado','New York'],
                    columns=['one','two','three','four'])
print(data.index.map(str.upper))
print()

print(data.rename(index=str.title, columns=str.upper))
print()
print(data.rename(index={'Ohio':'INDIANA'},columns={'three':'peekaboo'}))
