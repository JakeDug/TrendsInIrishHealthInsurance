from numpy import genfromtxt

def extractFromCSV(fileName):
	file_data = genfromtxt(fileName, delimiter = '|', dtype=None, encoding=None) #Specify no encoding in order to stop warnings (leaving blank is deprieciated)
	return file_data


print(extractFromCSV('test.csv'))


