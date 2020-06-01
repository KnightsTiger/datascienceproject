import pandas as pd


# There is an automatic index coloum in the table. So we need to remove it
df = pd.read_csv('BA.csv',parse_dates=['Date'],index_col=['Date'])
## print(df.head())
#following will help you to find out index value
## print(df.index)
# The advantage of converting into date time is we can filter only some specific date and time.
# See the below example
## print(df["2019-05"])
#Now we can get only a specifilc value
## print(df["2019-05"].Close)
# Further we can perform an operation on there
# Following will return mean value of the closing in may 2019
## print(df["2019-05"].Close.mean()) 
# Extracting on a specific date
print(df["2019-05-01":"2019-05-24"]) 




