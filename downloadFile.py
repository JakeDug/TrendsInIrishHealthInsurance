import requests

def downloadFile(downloadUrl):
	response = requests.get(downloadUrl)
	output = open('C:/Users/Jake/OneDrive/4th Year/project/dataFiles/tests.xlsx', 'wb')
	output.write(response.content)
	print(downloadUrl + " downloaded")
	output.close()
