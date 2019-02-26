from numpy import genfromtxt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from os import listdir
from os.path import isfile, join

plotly.tools.set_credentials_file(username='JakeDug', api_key='EOBghCU6WNJz4NJhrTTZ')

y-axis = ["plan_name" ,"adult" ,"young_adult_age_25", "young_adult_age_24", "young_adult_age_23", "young_adult_age_22", "young_adult_age_21", "young_adult_age_20", "young_adult_age_19", "young_adult_age_18", "child_one", "child_two", "child_three", "child_four", "newborn", "date"]

def readInFiles(filePath):
	fileList = [f for f in listdir(filePath) if isfile(join(filePath, f))]
	return fileList

def extractFromCSV(fileName):
	file_data = genfromtxt(fileName, delimiter = '|', dtype=None, encoding=None) #Specify no encoding in order to stop warnings (leaving blank is deprieciated)
	return file_data
	
def createPlotGraph(fileName):
	file_data = extractFromCSV(fileName)
	x = file_data[0]
	y = file_data[1]
	trace = go.Scatter(x=x, y=y,name=fileName)
	py.plot([trace], filename='numpy-array-ex1')

def createGraphFromSql(queryResult):
	planName = queryResult[0]
	y = y-axis
	x = queryResult
	trace = go.Scatter(x=x, y=y,name=planName)
	py.plot([trace], filename='numpy-array-ex1')

def createPlotGroup(fileList):
	
	trace = []
	
	for fileName in range(len(fileList)):
		file_data = extractFromCSV(fileList[fileName])
		x = file_data[0]
		y = file_data[1]
		
		fileName = go.Scatter(x=x,y=y, name=file_data[1][0] + " - " + fileList[fileName])
		
		trace.append(fileName)
		
	py.plot(trace, filename='numpy-array-ex1')


