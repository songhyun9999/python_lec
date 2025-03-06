import pandas as pd
import numpy as np
np.random.seed(12345)

date = pd.date_range('1/1/2020', periods=100, freq='D')
ts = pd.Series(np.random.randn(100), index=date)
print(ts)
print()
rsdata = ts.resample('M')
print(rsdata)
print()

for data in rsdata:
    print(data, end='\n\n')
print()

print(rsdata.mean())
print()

frame = pd.DataFrame(np.random.randn(2, 4),
                     index=pd.date_range('1/1/2020',
                                         periods=2, freq='W-WED'),
                     columns=['one','two','three','four'])
print(frame)
print()
rsdata2 = frame.resample('D')
for data in rsdata2:
    print(data, end='\n\n')

print()
print(frame.resample('D').ffill())
print()
print(frame.resample('D').ffill(limit=2))