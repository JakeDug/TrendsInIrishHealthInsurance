from numpy import genfromtxt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from os import listdir
from os.path import isfile, join

plotly.tools.set_credentials_file(username='JakeDug', api_key='EOBghCU6WNJz4NJhrTTZ')

x_axis = ["adult" ,"young_adult_age_25", "young_adult_age_24", "young_adult_age_23", "young_adult_age_22", "young_adult_age_21", "young_adult_age_20", "young_adult_age_19", "young_adult_age_18", "child_one", "child_two", "child_three", "child_four", "newborn"]

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
	planName = queryResult[1]
	y = queryResult
	x = x_axis
	trace = go.Scatter(x=x, y=y,name=planName)
	py.plot([trace], filename='numpy-array-ex1')

def createGraphFromSqlList(queryList):
	trace = []
	x = x_axis
	
	for row in range(0,len(queryList)):
		query_data = queryList[row]
		y = [query_data["adult"] ,query_data["young_adult_age_25"], query_data["young_adult_age_24"], query_data["young_adult_age_23"], query_data["young_adult_age_22"], query_data["young_adult_age_21"], query_data["young_adult_age_20"], query_data["young_adult_age_19"], query_data["young_adult_age_18"], query_data["child_one"], query_data["child_two"], query_data["child_three"], query_data["child_four"], query_data["newborn"]]
		
		plan_name = go.Scatter(x=x,y=y, name=query_data["plan_name"] + ' ~ ' + query_data["date"])
		
		trace.append(plan_name)
		
	py.plot(trace, filename='numpy-array-ex1')

def createPlotGroup(fileList):

	trace = []

	for fileName in range(len(fileList)):
		file_data = extractFromCSV(fileList[fileName])
		x = file_data[0]
		y = file_data[1]

		fileName = go.Scatter(x=x,y=y, name=file_data[1][0] + " - " + fileList[fileName])

		trace.append(fileName)

	py.plot(trace, filename='numpy-array-ex1')
	
	
def createPredictionGraph(priceList, dateList):
	y = dateList
	x = priceList
	
	layout = go.Layout(
		title='',
		xaxis=dict(
			title='Price',
			titlefont=dict(
				family='Courier New, monospace',
				size=18,
				color='#7f7f7f'
			)
		),
		yaxis=dict(
			title='Date',
			titlefont=dict(
				family='Courier New, monospace',
				size=18,
				color='#7f7f7f'
			)
		)
	)
	
	trace = go.Scatter(
	x = priceList,
	y = dateList,
	mode = 'markers'
	)
	
	
	fig = go.Figure(data=[trace], layout=layout)
	
	py.plot(fig, filename='pred-graph')


