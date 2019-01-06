from numpy import genfromtxt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='JakeDug', api_key='EOBghCU6WNJz4NJhrTTZ')

def extractFromCSV(fileName):
	file_data = genfromtxt(fileName, delimiter = '|', dtype=None, encoding=None) #Specify no encoding in order to stop warnings (leaving blank is deprieciated)
	return file_data


my_data = extractFromCSV('VhiJan2018.csv')
my_data2 = extractFromCSV('VhiJuly2018.csv')

x = my_data[0]
y = my_data[1]

x1= my_data[0]
y1 = my_data2[1]

VhiJan2018 = go.Scatter(x=x, y=y,name="Jan 2018")
VhiJuly2018 = go.Scatter(x=x1, y=y1, name="July 2018")
py.iplot([VhiJan2018, VhiJuly2018], filename='numpy-array-ex1')

