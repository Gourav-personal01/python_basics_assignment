#Q2. Create a variable of list type containing 10 elements in it, and apply pandas Series function on the
#variable print it.

# Solution - 

import pandas as pd

list_variable = [1,2,3,4,5,6,7,8,9,10]

pandas_series_data = pd.Series(data=list_variable)

print(pandas_series_data)