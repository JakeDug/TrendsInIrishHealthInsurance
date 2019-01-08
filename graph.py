from numpy import genfromtxt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='JakeDug', api_key='EOBghCU6WNJz4NJhrTTZ')

def extractFromCSV(fileName):
	file_data = genfromtxt(fileName, delimiter = '|', dtype=None, encoding=None) #Specify no encoding in order to stop warnings (leaving blank is deprieciated)
	return file_data
	
def createPlotGraph(fileName):
	file_data = extractFromCSV(fileName)
	x = file_data[0]
	y = file_data[1]
	trace = go.Scatter(x=x, y=y,name=fileName)
	py.plot([trace], filename='numpy-array-ex1')

def createPlotGroup(fileList):
	
	trace = []
	
	for fileName in range(len(fileList)):
		file_data = extractFromCSV(fileList[fileName])
		x = file_data[0]
		y = file_data[1]
		
		fileName = go.Scatter(x=x,y=y, name=fileList[fileName])
		
		trace.append(fileName)
		
	py.plot(trace, filename='line-mode')

files = ['VhiJan2018.csv', 'VhiJuly2018.csv']

createPlotGroup(files)
		
	

