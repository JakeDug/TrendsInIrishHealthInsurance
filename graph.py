from numpy import genfromtxt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from os import listdir
from os.path import isfile, join

plotly.tools.set_credentials_file(username='JakeDug', api_key='EOBghCU6WNJz4NJhrTTZ')

x_axis = ["adult" ,"young_adult_age_25", "young_adult_age_24", "young_adult_age_23", "young_adult_age_22", "young_adult_age_21", "young_adult_age_20", "young_adult_age_19", "young_adult_age_18", "child_one", "child_two", "child_three", "child_four", "newborn"]

def readInFiles(filePath):
	""" 
	Given a path to a directory returns a list of files in that directory (Used for testing)
	
	Parameters
	----------
	
	filePath : String
		A string representing the desired path
		
	Returns
	-------
	**retruns** : list
		returns a list of files in the directory given in filePath
	"""
	fileList = [f for f in listdir(filePath) if isfile(join(filePath, f))]
	return fileList

def extractFromCSV(fileName):
	""" 
	Extracts data from a csv file split using | returns this data in a list (Used for testing)
	
	Parameters
	----------
	
	fileName : String
		A string relating to the name of the desired file eg. example.csv
		
	Returns
	-------
	**retruns** : list
		returns a list with each element being a variable from the csv file
	"""
	file_data = genfromtxt(fileName, delimiter = '|', dtype=None, encoding=None) #Specify no encoding in order to stop warnings (leaving blank is deprieciated)
	return file_data

def createPlotGraph(fileName):
	""" 
	Creates a plot graph for the first 2 rows of a csv file given a filename. (For testing)
	
	Parameters
	----------
	
	fileName : String
		A string relating to the name of the desired file eg. example.csv
		
	Returns
	-------
	**retruns** : void
	"""
	file_data = extractFromCSV(fileName)
	x = file_data[0]
	y = file_data[1]
	trace = go.Scatter(x=x, y=y,name=fileName)
	py.plot([trace], filename='numpy-array-ex1')

def createGraphFromSql(queryResult):
	""" 
	Creates a graph of the first row a query returns given an SQLAlchemy object (For testing)
	
	Parameters
	----------
	
	queryResult : sql alchemy obj
		An sql alchemey obj containing data for one row in the database
		
	Returns
	-------
	**retruns** : void
	"""
	planName = queryResult[1]
	y = queryResult
	x = x_axis
	trace = go.Scatter(x=x, y=y,name=planName)
	py.plot([trace], filename='numpy-array-ex1')

def createGraphFromSqlList(queryList):
	""" 
	Given a list of dicts a graph is created using each dict as an input on the graph.
	
	Parameters
	----------
	
	queryList : List
		A list of dicts generated by the row2dict function
		
	Returns
	-------
	**retruns** : void
		
	"""
	
	trace = []
	x = x_axis
	
	for row in range(0,len(queryList)):
		query_data = queryList[row]
		y = [query_data["adult"] ,query_data["young_adult_age_25"], query_data["young_adult_age_24"], query_data["young_adult_age_23"], query_data["young_adult_age_22"], query_data["young_adult_age_21"], query_data["young_adult_age_20"], query_data["young_adult_age_19"], query_data["young_adult_age_18"], query_data["child_one"], query_data["child_two"], query_data["child_three"], query_data["child_four"], query_data["newborn"]]
		
		plan_name = go.Scatter(x=x,y=y, name=query_data["plan_name"] + ' ~ ' + query_data["date"])
		
		trace.append(plan_name)
		layout = go.Layout(
			title='',
			xaxis=dict(
				title='Age Group',
				titlefont=dict(
					family='Courier New, monospace',
					size=18,
					color='#7f7f7f'
				)
			),
			yaxis=dict(
				title='Price',
				titlefont=dict(
					family='Courier New, monospace',
					size=18,
					color='#7f7f7f'
				)
			)
		)
	
	fig = go.Figure(data=trace, layout=layout)
	py.plot(fig, filename='numpy-array-ex1')

def createPlotGroup(fileList):
	""" 
	Given a list of files a graph is created using each file as an input on the graph. (For testing)
	
	Parameters
	----------
	
	fileList : list
		A list of filenames generated by readInFiles function.
		
	Returns
	-------
	**retruns** : void
	"""
	trace = []

	for fileName in range(len(fileList)):
		file_data = extractFromCSV(fileList[fileName])
		x = file_data[0]
		y = file_data[1]

		fileName = go.Scatter(x=x,y=y, name=file_data[1][0] + " - " + fileList[fileName])

		trace.append(fileName)

	py.plot(trace, filename='numpy-array-ex1')
	
	
def createPredictionGraph(priceList, dateList):
	""" 
	Given a list of prices and dates creates a scatter plot. Used to plot predicted prices in the machineLearning module. 
	
	Parameters
	----------
	
	priceList : list
		A list of prices
	
	dateList : list
		A list of dates linked to the prices in priceList
		
	Returns
	-------
	**retruns** : void
	"""
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


