#Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.

# Solution-

import pandas as pd

data = [4,8,15,16,23,42]
panda_series_data = pd.Series(data=data,index=[0,1,2,3,4,5])

print(panda_series_data)
print(type(panda_series_data))