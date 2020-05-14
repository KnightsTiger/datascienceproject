import pandas as pd

df = pd.read_csv('BA.csv')
print(df.head())

#printing the daate coloum
print(type(df.Date[0]))
# currently this is a string. So we need to convert this into a date type

df = pd.read_csv('BA.csv',parse_dates=['Date'])
print(type(df.Date[0]))
