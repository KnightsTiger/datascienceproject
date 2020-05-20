import pandas as pd

df = pd.read_csv('pone.csv',parse_dates=['Date'],index_col=['Date'])
print(df)

#%%
import pandas as pd
import matplotlib as mp

df = pd.read_csv('pone.csv',parse_dates=['Date'],index_col=['Date'])

# %%
import matplotlib.pyplot as mp

x = list(range(0,10))
y = list(range(0,10))

mp.plot(x,y)

# %%
