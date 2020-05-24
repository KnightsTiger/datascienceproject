#%%
# 1) install statsmodels
# pip install statsmodels
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
import pandas as pd
import matplotlib.pyplot  as plt

df = pd.read_csv('sample1.csv')

#apply Simple Exponential Smoothing

# fit3 = SimpleExpSmoothing(df).fit()
# fcast3 = fit3.forecast(12).rename(r'$\alpha=%s$'%fit3.model.params['smoothing_level'])
# # plot
# fcast3.plot(marker='o', color='green', legend=True)
# fit3.fittedvalues.plot(marker='o', color='green')

# plt.show()





# %%
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.tsa.holtwinters as ets

df = pd.read_csv('sample1.csv',index_col='Date',parse_dates=True)
#print(df)
#Defining the range of the training and testing
spyt = df[:'2020-01-10']
spyf= df['2020-01-11':]

#print(spyt)
#print(spyf)

brownt = ets.ExponentialSmoothing(spyt,trend=None,damped=False,seasonal=None).fit()
brownf = brownt.forecast(steps=len(spyf))
brownf = pd.DataFrame(brownf).set_index(spyf.index)

fig1, ax = plt.subplots()
ax.plot(spyt,label='spyt')
ax.plot(spyf,label='spyf')
ax.plot(brownf,label='brownf')
plt.ylabel('likes')
plt.xlabel('hours')
plt.show()


# %%
