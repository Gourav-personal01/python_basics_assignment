#Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
#    you give an example of when you might use one of these functions?

# Solution - 
# There are lot of Function used in pandas dataframe to manipulate the data which are dtypes,head,tail,coloumns etc

# Example - 

import pandas as pd
data_frame = pd.read_excel("LUSID Excel - Setting up your market data.xlsx")
print(data_frame)
print(data_frame.dtypes)
print(data_frame.columns)
print(data_frame.head(2))
print(data_frame.tail(2))
 