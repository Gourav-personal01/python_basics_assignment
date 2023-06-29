#Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.

# Solution - 
# Data frame in pandas is defined as the 2 dimentional data structure type which is used to store multiple data (like integers, float values,string etc.)
# Data frame is different from panda series as the datatype inside the data frame is store as Series and Series is quitly equivalent to list in python.

# Example-- 

import pandas as pd 

data_frame = pd.read_csv("services.csv")

print(type(data_frame))

series_data = data_frame['program_id']
print(series_data)
print(type(series_data))