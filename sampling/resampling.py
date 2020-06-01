import pandas as pd

df = pd.read_csv('BA.csv',parse_dates=['Date'],index_col=['Date'])
#converting only to the monthly data
print(df.Close.resample('M').mean())

#%%
import pandas as pd
import matplotlib as mp

df = pd.read_csv('BA.csv',parse_dates=['Date'],index_col=['Date'])
#converting only to the monthly data

df.Close.resample('W').mean().plot()


# %%
#in here kind is bar
df.Close.resample('M').mean().plot(kind="bar")

# %%
df.Close.plot()

# %%



# %%
