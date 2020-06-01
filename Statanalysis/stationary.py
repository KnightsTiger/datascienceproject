#As per the graph we can deside is that stationary or not
from pandas import read_csv
from matplotlib import pyplot
series = read_csv('sample1.csv', header=0, index_col=0)
series.plot()
pyplot.show()
