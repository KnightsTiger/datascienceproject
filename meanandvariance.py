#split the time series into two contiguous sequences
# the mean and variance look very different.Then non-stationary time series
''''
mean1=39.763736, mean2=44.185792
variance1=49.213410, variance2=48.708651
This is stationary - Because both mean and variance values are near values

********************************
mean1=182.902778, mean2=377.694444
variance1=2244.087770, variance2=7367.962191
This is not stationary - Because the values are higly differenced

'''
from pandas import read_csv
series = read_csv('lf1.csv', header=0, index_col=0)
X = series.values
split = round(len(X) / 2)
X1, X2 = X[0:split], X[split:]
mean1, mean2 = X1.mean(), X2.mean()
var1, var2 = X1.var(), X2.var()
print('mean1=%f, mean2=%f' % (mean1, mean2))
print('variance1=%f, variance2=%f' % (var1, var2))
