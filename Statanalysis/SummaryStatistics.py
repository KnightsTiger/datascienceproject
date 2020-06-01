#This will provide a graph to view about the data
# if We clearly see the bell curve-like shape of the Gaussian distribution then it is stationary. If not (squashed distribution https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2016/12/Histogram-of-Airline-Passengers.png)some bars are available 
# then this is not stationary.

from pandas import read_csv
from matplotlib import pyplot
series = read_csv('hours.csv', header=0, index_col=0)
series.hist()
pyplot.show()