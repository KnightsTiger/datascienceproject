'''
p-value > 0.05: Fail to reject the null hypothesis (H0), the data has a unit root and is non-stationary.
p-value <= 0.05: Reject the null hypothesis (H0), the data does not have a unit root and is stationary.

ADF Statistic
if 1% is less than ADF Statistic value. Then that is non-stationary

'''
from pandas import read_csv
from statsmodels.tsa.stattools import adfuller

series = read_csv('sample1.csv', header=0, index_col=0, squeeze=True)
X = series.values
result = adfuller(X)
print('ADF Statistic: %f' % result[0])
# Uncomment for easy use :) 
# if result[1]>0.05:
# 	print("non-stationary")
# else:
# 	print("Stationry")
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))