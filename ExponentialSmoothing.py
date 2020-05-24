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
import statsmodels.tsa.holtwinters as sts

