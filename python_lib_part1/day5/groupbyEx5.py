import pandas as pd
import numpy as np

states = ['ohio', 'new york', 'vermont', 'florida',
          'oregon', 'nevada', 'califonia', 'idaho']
group_key = ['East'] * 4 + ['West'] * 4
#print(group_key)
data = pd.Series(np.random.randn(8), index=states)
#print(data)
data[['vermont', 'nevada', 'idaho']] = np.nan
print(data)
print()
print(data.groupby(group_key).mean())
print()

fill_mean = lambda g : g.fillna(g.mean())
print(data.groupby(group_key).apply(fill_mean))
print()

fill_values = {'East':0.5, 'West':-1}
fill_func = lambda g : g.fillna(fill_values[g.name])
print(data.groupby(group_key).apply(fill_func))