# Create a Pandas DataFrame that contains the following data in the Question3_data file and Then, print the DataFrame.

import pandas as pd 

data_frame = pd.read_csv('Question3_data.csv')
print(data_frame)
print(type(data_frame))