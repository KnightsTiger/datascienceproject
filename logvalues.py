# In this case if we see a gussian distiribution, then this means it is not stationary
# Note - No Zero values are allowed.
from pandas import read_csv
from matplotlib import pyplot
from numpy import log
series = read_csv('sample1.csv', header=0, index_col=0)
X = series.values
X = log(X)
pyplot.hist(X)
pyplot.show()
pyplot.plot(X)
pyplot.show()