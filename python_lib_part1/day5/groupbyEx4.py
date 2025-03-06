import numpy as np
import pandas as pd

tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']

def g_func(gdata, n=5, column='tip_pct'):
    return gdata.sort_values(by=column, ascending=False)[:n]

print(tips.groupby('smoker').apply(g_func))
print()
print(tips.groupby(['smoker', 'day']).apply(g_func, n=3, column='total_bill'))