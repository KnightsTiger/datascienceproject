#This will provide a graph to view about the data
# if We clearly see the bell curve-like shape of the Gaussian distribution then it is stationary. If not some bars are available 
# then this is not stationary.

from pandas import read_csv
from matplotlib import pyplot
series = read_csv('sample1.csv', header=0, index_col=0)
series.hist()
pyplot.show()