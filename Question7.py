# Create a DataFrame using multiple Series. Explain with an example.

# Solution -

import pandas as pd 

data_frame = pd.read_csv("services.csv")
print(data_frame)

# Multiple Series 

Series1 = data_frame['website']
print(Series1)
print(type(Series1))

Series2 = data_frame['taxonomy_ids']
print(Series2)
print(type(Series2))